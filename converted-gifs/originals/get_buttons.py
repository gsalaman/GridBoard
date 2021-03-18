import serial
import time

def read():
  global ser

  if ser.inWaiting() == 0:
    return None
  
  line = ser.readline()

  # first character for a press is "P", release is "R". All others not valid.
  if ((line[0] == 'P') or (line[0] == 'R')):
    action_type = line[0]
    line = line.strip("PR\n\r ")
    button = line.split(",")
  
    # first check...do we have the right number of chars?
    if len(line) != 3:
      #print("not text we care about")
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
    #print("Unexpected serial command:" + line)
    pass

  ser.flushInput() 

#print("running")
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1) 
#ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1) 

time.sleep(0.01) # wait for serial port to open.
if ser.isOpen():
  print("serial connected!")
