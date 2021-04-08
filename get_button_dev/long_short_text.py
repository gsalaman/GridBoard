#  Show long vs short presses via text messages.

import get_buttons
from datetime import datetime
import time

# press_time contains when the press occured for a given button, or "None"
# if that button isn't currently pressed.
press_time = [[None for i in range(8)] for j in range(8)]

long_press_duration = 2     # 2 seconds for a long press

while True:
  press = get_buttons.read()
  if (press != None):
    if (press[2] == "P"):
      print("Press detected: "+str(press[0])+","+str(press[1]))
      if press_time[press[0]][press[1]] != None:
        # This shouldn't happen, but all is not lost if it does. 
        # Just print and go on.
        print("Press whilst still pressed.")

      # Mark the timestamp
      press_time[press[0]][press[1]] = datetime.now()

    elif (press[2] == "R"):
      curr_time = datetime.now()
      print("Release detected: "+str(press[0])+","+str(press[1]))

      start_time = press_time[press[0]][press[1]]
      if start_time == None:
        print("No corresponding press (?!?)")
        continue

      deltaT = curr_time - start_time
      if deltaT.total_seconds() > long_press_duration:
        print("Long press!")
      else:
        print("Short press!")

