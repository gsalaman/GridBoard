from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class msApp():
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.seconds_per_screen = 1 
        self.last_update_time = datetime.now()
        
        self.constr_image = Image.open("under_construction.png")
        self.constr_image = self.constr_image.resize((128,16))

        self.scroll_text = "We're sorry to report that minesweeper has not been coded yet"
        self.scroll_pixels = len(self.scroll_text) * 8

    ###############################################
    # run()
    ###############################################
    def run(self):
      press_detected = False

      text_box = Image.new("RGB", (128,32))
      text_draw = ImageDraw.Draw(text_box)

      self.rgbmatrix.SetImage(self.constr_image, 0, 0)
      scroll_index = 0 

      while press_detected == False:  
        current_time = datetime.now()
        deltaT = current_time - self.last_update_time

        # check to see if it's time to advance our scrolling text 
        if deltaT.total_seconds() > self.seconds_per_screen:
          # scroll index is going to count up from 0, but we'll use it as a 
          # subtractor from 128 (the right edge)
          scroll_index = (scroll_index + 1) % self.scroll_pixels
      
          # blank the old text
          text_draw.rectangle((0,0,128,32) fill = (0,0,0))

          # draw the new text
          text_draw.text((128 - scroll_index, 0), self.scroll_text)
          self.rgbmatrix.SetImage(text_box, 0, 32) 

        # check for button presses
        # right now, any button press will advance us.  Eventually want to 
        # tweak this so that only the right areas of the screen advance.
        my_button = read()
        if (my_button != None):
          print("button event")
          if my_button[2] == 'P':
            print("Press detected!")
            press_detected = True

        # allow for other processes to run
        time.sleep(0.01)

      # once we have a button press, exit. 
      return "splash"
