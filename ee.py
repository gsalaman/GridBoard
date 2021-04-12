from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class ee():
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.seconds_per_screen = 1
        self.last_update_time = datetime.now()
        self.home_image_index = 0
       
        # okay, I can't bring myself to type or copy 14 filenames.  
        self.home_images = []
        for i in range(1,15):
          filename = "ee/ee"+str(i)+".png"
          tmp_image = Image.open(filename)
          self.home_images.append(tmp_image)

        self.num_home_images = len(self.home_images)

    ###############################################
    # run()
    ###############################################
    def run(self):
      press_detected = False
      while press_detected == False:  
        current_time = datetime.now()
        deltaT = current_time - self.last_update_time

        # check to see if it's time to switch the animated gif
        if deltaT.total_seconds() > self.seconds_per_screen:
            # only update until we hit the last image...then we'll hold there.
            if (self.home_image_index < self.num_home_images):
              self.home_image_index = self.home_image_index + 1 
              self.rgbmatrix.SetImage(self.home_images[self.home_image_index],0,0)
            self.last_update_time = current_time

        # check for button presses
        my_button = read()
        if (my_button != None):
          print("button event")
          if my_button[2] == 'P':
            print("Press detected!")
            press_detected = True

        # allow for other processes to run
        time.sleep(0.01)

      # once we have a button press, exit back to the splash screen
      return "splash"
