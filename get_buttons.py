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
from datetime import datetime

# queue for storting mqtt button presses.
_mqtt_q = []

# time array to detect long and short presses
press_time = [[None for i in range(8)] for j in range(8)]

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

############################
# read_long_short
#
# For the purposes of this function, a press gets catagorized upon release.
# A short press is if the button was held down for less than 1.5s.
# A long press is if the button was held down for longer than 1.5s.
#
# This function will either return:
#   - None if there was no press 
#   or a tuple with:
#     index 0 for x location
#     index 1 for y location
#     index 2 with either:
#        "S" for short press
#        "L" for long press
########################################
def read_long_short():
  global press_time

  long_press_duration = 1.5

  press = read()
  if (press == None):
    return None
  
  if (press[2] == "P"):
    print("Press Detected: "+str(press[0])+","+str(press[1]))
    if press_time[press[0]][press[1]] != None:
      # This shouldn't happen...
      print("Press whilst still pressed.")

    # Mark the timestamp
    press_time[press[0]][press[1]] = datetime.now()

  elif (press[2] == "R"):
    curr_time = datetime.now()
    print("Release Detected: "+str(press[0])+","+str(press[1]))

    start_time = press_time[press[0]][press[1]]
    if start_time == None:
      print("No corresponding press (?!?)")
      return Noone

    deltaT = curr_time - start_time
    press_time[press[0]][press[1]] = None
    

    if deltaT.total_seconds() > long_press_duration:
      ret_val = (press[0],press[1],"L")
    else:
      print("Short press!")
      ret_val = (press[0],press[1],"S")
 
    return ret_val


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
      #_ser.flushInput() 
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
    #print("no press")
    time.sleep(0.01)
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
  #_client.connect("matrix-pi1.local")
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
  time.sleep(1) # wait for serial port to open.
  if _ser.isOpen():
    print("serial connected!")
    _ser_enabled = True
except:
  print("unable to open serial port")
