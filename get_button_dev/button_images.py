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
matrix_rows = 32 
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 8 
matrix_vertical = 2

total_rows = 128 
total_columns = 128

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular' 
options.pixel_mapper_config = 'U-mapper'

matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################

icon = Image.open("../icons/MS_bomb.png").convert("RGB")
blank = Image.new("RGB", (16,16))

try:
  print("Press CTRL-C to stop")
  while True:
    my_button = get_buttons.read()
    if my_button != None:
      print("Main - button x: "+str(my_button[0]))
      print("Main - button y: "+str(my_button[1]))
  
      x = my_button[0] * 32
      y = my_button[1] * 32
  
      if my_button[2]=="P":
        matrix.SetImage(icon,x,y)
      else:
        matrix.SetImage(blank,x,y)

    time.sleep(.01)

except KeyboardInterrupt:
  exit(0)

