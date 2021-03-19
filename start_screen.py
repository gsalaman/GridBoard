from PIL import Image, ImageDraw, ImageFont
from get_buttons import read
from datetime import datetime
import time

class start_screen:
    def __init__(self,rgbmatrix,total_rows,total_columns):
        self.rgbmatrix = rgbmatrix
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.seconds_per_screen = 1
        self.last_update_time = datetime.now()
        self.home_image_index = 0
        self.num_home_images = 0
        self.home_images = ()

    def mainScreen(self):

        blank_screen = Image.new("RGB", (total_columns,total_rows))
        home1 = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif01.gif").convert("RGB")
        home2 = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif02.gif").convert("RGB")
        self.home_images
        home_images = (home1, home2)
        self.num_home_images
        num_home_images = len(home_images)
        self.home_image_index

        mainscreen = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif02.gif").convert("RGB")
        rgbmatrix.SetImage(mainscreen,0,0)

    def nextImage(self):
        self.last_update_time
        self.home_image_index
        self.num_home_images
        self.home_images

        current_time = datetime.now()
        deltaT = current_time - last_update_time

        # check to see if it's time to switch the animated gif
        if deltaT.total_seconds() > seconds_per_screen:
            home_image_index = (home_image_index + 1) % num_home_images
            rgbmatrix.SetImage(home_images[home_image_index],0,0)
            last_update_time = current_time
        time.sleep(0.01)

    def mainPress():
        my_button = read()
        if my_button != None:
            print("Main - button x: "+str(my_button[0]))
            print("Main - button y: "+str(my_button[1]))

        x = my_button[0] * 32
        y = my_button[1] * 32

        if my_button[2]=="P":
            return True
        else:
            return False
        return False
