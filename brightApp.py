##############################################
# brightApp
#
# This app is used to set the screen brightness
#############################################

from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class brightApp():
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.image = Image.new("RGB", (total_columns, total_rows))

    ###############################################
    # run()
    ###############################################
    def run(self):
      

      current_brightness = self.rgbmatrix.brightness
      draw = ImageDraw.Draw(self.image)
      draw.text((20,0),"Brightness Test")
      draw.rectangle((0,32,31,63), fill=(255,255,255))
      draw.rectangle((32,32,63,63), fill = (255,0,0))
      draw.rectangle((64,32,95,63), fill = (0,255,0))
      draw.rectangle((96,32,127,63), fill = (0,0,255))

      draw.rectangle((0,64,31,95), outline = (255,0,0))
      draw.text((13,74),"-", fill = (255,0,0)) 
      draw.rectangle((96,64,127,95), outline = (0,255,0))
      draw.text((110,74),"+", fill = (0,255,0))

      draw.rectangle((0,112,31,127), outline = (255,255,255))
      draw.text((5,113), "back")
      draw.text((100,100),str(current_brightness))
      self.rgbmatrix.SetImage(self.image,0,0)

      # now wait for a button press
      while True:
        my_button = read()
        if my_button != None:
          if (my_button[2] == "P"):
            # clear old brightness 
            draw.rectangle((100,100,127,127), fill=(0,0,0))

            #ugly first take!!!
            if ( 
                 ((my_button[0] == 0) and (my_button[1] == 4)) or
                 ((my_button[0] == 0) and (my_button[1] == 5)) or
                 ((my_button[0] == 1) and (my_button[1] == 4)) or
                 ((my_button[0] == 1) and (my_button[1] == 5))      ):
              current_brightness = current_brightness - 10

            elif (
                   ((my_button[0] == 6) and (my_button[1] == 4)) or
                   ((my_button[0] == 6) and (my_button[1] == 5)) or
                   ((my_button[0] == 7) and (my_button[1] == 4)) or
                   ((my_button[0] == 7) and (my_button[1] == 5))      ):
              current_brightness = current_brightness + 10

            elif (
                   ((my_button[0] == 0) and (my_button[1] == 7)) or
                   ((my_button[0] == 1) and (my_button[1] == 7))      ):
              return "splash" 


            if (current_brightness > 100):
              current_brightness = 100
            if (current_brightness < 10):
              current_brightness = 10
            draw.text((100,100),str(current_brightness))
            self.rgbmatrix.brightness = current_brightness
            self.rgbmatrix.SetImage(self.image,0,0)

          print my_button

        time.sleep(0.1)
