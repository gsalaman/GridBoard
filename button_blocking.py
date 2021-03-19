import get_buttons
import time

try:
  print("Press Ctl-C to stop")
  while True:
    button = get_buttons.wait_for_press()
    print("Button Press. X="+str(button[0])+", Y="+str(button[1]))
  
    time.sleep(0.01)

except KeyboardInterrupt:
  exit(0)
