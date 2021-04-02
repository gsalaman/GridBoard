from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class splashApp():
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.seconds_per_screen = 1
        self.last_update_time = datetime.now()
        self.home_image_index = 0
       
        home1 = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif01.gif").convert("RGB")
        home2 = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif02.gif").convert("RGB")
        self.home_images = (home1, home2)
        self.num_home_images = len(self.home_images)

    ###############################################
    # run()
    #
    # This function cycles through all the animated gifs until a button is 
    # pressed.
    ###############################################
    def run(self):
      my_button = read()
      while my_button == None:  
        current_time = datetime.now()
        deltaT = current_time - self.last_update_time

        # check to see if it's time to switch the animated gif
        if deltaT.total_seconds() > self.seconds_per_screen:
            self.home_image_index = (self.home_image_index + 1) % self.num_home_images
            self.rgbmatrix.SetImage(self.home_images[self.home_image_index],0,0)
            self.last_update_time = current_time

        # check for button presses
        # right now, any button press will advance us.  Eventually want to 
        # tweak this so that only the right areas of the screen advance.
        my_button = read()

        # allow for other processes to run
        time.sleep(0.01)

      # once we have a button press, exit. From the splash screen we always
      # go to the game select screen.
      return "select"
