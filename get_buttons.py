#######################################################
# get_button library
#
# This version of get_button supports both button presses via the serial port
# (from the arduino, processing the button matrix) or virtual button presses
# from MQTT.
#######################################################


import serial
import time
import paho.mqtt.client as mqtt

# queue for storting mqtt button presses.
_mqtt_q = []

#######################################################
# MQTT callback function
#######################################################
def on_message(client, userdata, message):
  global _mqtt_q

  print("Recieved "+message.topic+"    "+message.payload)

  _mqtt_q.append(message.payload)


###########
# Block until button is actually pressed.
############
def wait_for_press():
  current_press = read()
  
  while True:
    current_press = read()
    if current_press == None:
      time.sleep(0.01)
      continue
    elif current_press[2] == "R":
      print("ignoring release")
      time.sleep(0.01)
      continue 
    else:
      return current_press

###########
# Block until button is actually pressed or released.
############
def read_block():
  current_press = read()
  while current_press == None:
    time.sleep(0.01)
    current_press = read()
  return current_press


##############
# read
#############
def read():
  global _ser
  global _ser_enabled
  global _mqtt_q

  press_available = False
  # 1st check:  anything for us in serial land?
  if _ser_enabled:
    if _ser.inWaiting() != 0:
      line = _ser.readline()
      _ser.flushInput() 
      press_available = True
  # 2nd check:  anything for us in mqtt-land?
  if press_available == False and len(_mqtt_q) > 0:
    # don't need an enabled check here...the queue still exists.
    print("got mqtt button press")
    line = _mqtt_q[0]
    del _mqtt_q[0]
    press_available = True


  # okay, we've gone through our potential input sources.  If none of them
  # fired, we just want to return "None" to show no press available.
  if (press_available == False):
    return None
    
  # the rest of this processing is common between serial and mqtt presses.
  # We've gotten a press, so we need to parse it.

  # first character for a press is "P", release is "R". All others not valid.
  if ((line[0] == 'P') or (line[0] == 'R')):
    action_type = line[0]
    line = line.strip("PR\n\r ")
    button = line.split(",")
  
    # first check...do we have the right number of chars?
    if len(line) != 3:
      return None

    # a little check:  the two numbers should be between 0 and 7.
    # fix this:  non int's will crash.  want more robust.
    x_button = int(line[0])
    y_button = int(line[2])
    
    if ((x_button > 7) or (x_button < 0)):
      print("bad x")
      return None
  
    if ((y_button > 7) or (y_button < 0)):
      print("bad y")
      return None
   
    return(x_button,y_button,action_type)
    
  else:
    return None 


##########################################
# Global inits 
#
#    We'll try and enable both the MQTT interface and the serial interface.
###########################################
print("mqtt_inits start")
# MQTT inits
_client = mqtt.Client("Jumbotron")
_client.on_message=on_message
try:
  #_client.connect("broker.hivemq.com")
  _client.connect("mqttbroker")
  _mqtt_enabled = True
  print("mqtt connected")
except:
  print("Unable to connect to MQTT broker")
  _mqtt_enabled = False

if _mqtt_enabled == True:
  _client.loop_start()
  _client.subscribe("jumbotron/button/#")
print("mqtt_inits end")

# Serial inits
_ser_enabled = False
try:
  _ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1) 
  #_ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1) 
  time.sleep(0.01) # wait for serial port to open.
  if _ser.isOpen():
    print("serial connected!")
    _ser_enabled = True
except:
  print("unable to open serial port")

