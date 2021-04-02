##############################################
# select_screen
#
# In this iteration, we display the full menu (no animation) and stall. 
#
# Future versions will timeout back to the splash screen, and advance to 
# game on button presses.
#############################################

from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class select_screen:
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.image = Image.open("converted-gifs/Top/GameMenu/gamemenu.gif04.gif").convert("RGB")

    ###############################################
    # run()
    ###############################################
    def run(self):
      
      self.rgbmatrix.SetImage(self.image,0,0)
      while True:
        # wait forever.
        pass
