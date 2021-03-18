from time import sleep
import datetime

import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageSequence, GifImagePlugin, ImageDraw, ImageFont
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

options.pixel_mapper_config='U-mapper'

matrix = RGBMatrix(options = options)

###################################
# Main code 
###################################
image = Image.open("./Minesweeper/MS_How-to.gif")
print("Frames: ",image.n_frames)

exit(0)

# Loop through gif frames and display on matrix.
while True:
  for frame in range(0, image.n_):
      print(image.frame_number)
      image.seek(frame)
      matrix.SetImage(image.convert('RGB'))
      time.sleep(1)

# Handle quiting
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
