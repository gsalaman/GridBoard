import time 
import datetime
import serial
import get_buttons

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# this is the size of ONE of our matrixes. 
#matrix_rows = 32 
#matrix_columns = 32 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
#matrix_horizontal = 8 
#matrix_vertical = 2
matrix_horizontal = 1 
matrix_vertical = 1

#total_rows = 128 
#total_columns = 128
total_rows = 64 
total_columns = 64 

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular' 
#options.pixel_mapper_config = 'U-mapper'
options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################

icon = Image.open("../icons/ghost.jpg").convert("RGB")
icon = icon.resize((16,16))
blank = Image.new("RGB", (16,16))

# This version only does presses...and toggles the ghost image on and off 
# for each press.  This means we have to remember, for our 8x8 grid, whether
# the square in question is on or off
grid = [[0]*8]*8

print grid

try:
  print("Press CTRL-C to stop")
  while True:
    my_button = get_buttons.wait_for_press()
  
    x = my_button[0] 
    y = my_button[1] 
  
    # if the square is currently off...
    if grid[x][y] == 0:
          # turn on the square.
          matrix.SetImage(icon,x*16,y*16)
          grid[x][y] = 1
     #otherwise turn off that square
    else:
          matrix.SetImage(blank,x*16,y*16)
          grid[x][y] = 0

except KeyboardInterrupt:
  exit(0)

