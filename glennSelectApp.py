##############################################
# UPDATE ME!!!!!
# selectApp
#
# In this iteration, we display the full menu (no animation) and wait for a 
# button press.  On press, we go back to the splash screen.
#
# Future versions will timeout back to the splash screen, and advance to 
# game on button presses.
#############################################

from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class glennSelectApp():
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.image = Image.open("glenn_app_v1.png").convert("RGB")
        self.image = self.image.resize((total_rows+1, total_columns))

    ###############################################
    # run()
    ###############################################
    def run(self):
      
      # we only have one "screen" in this iteration....show it.
      self.rgbmatrix.SetImage(self.image,0,0)
      
      # now wait for a button press
      while True:
        my_button = read()
        if my_button != None:
          print my_button
          if my_button[2]=="P":
            if (my_button[1] == 7):
              if (my_button[0] == 6) or (my_button[0] == 7):
                return "splash"
            elif (my_button[0] == 1 and my_button[1] == 2):
              return "bright"
        time.sleep(0.1)
