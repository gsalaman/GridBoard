import get_buttons
import time

try:
  print("Press Ctl-C to stop")
  while True:
    button = get_buttons.read()

    if button != None:
      if button[2] == "P":
        print("Button Press. X="+str(button[0])+", Y="+str(button[1]))
      elif button[2] == "R":
        print("Button Release. X="+str(button[0])+", Y="+str(button[1]))
  
    time.sleep(0.01)

except KeyboardInterrupt:
  exit(0)
