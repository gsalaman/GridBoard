## This is the main program running the gridboard ##

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

from startScreen import startScreen
from selectScreen import selectScreen

##RGB Matrix Standards
# Size of one panel
matrix_rows = 32 
matrix_columns = 32 

# How many mattixes stacked horizontally and vertically
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
options.gpio_slowdown = 2
options.pixel_mapper_config = 'U-mapper'

matrix = RGBMatrix(options = options) #making the matrix for all programs

blankscreen = Image.new('RGB', (128, 128))

start = startScreen(matrix, total_rows, total_columns)
select = selectScreen(matrix, total_rows, total_columns)
screens = {
  "splash": start,
  "select": select
}

currentScreen = start

def drawBlank():
    global matrix
    matrix.SetImage(blankscreen,0,0)

if __name__ == '__main__':
    print("initalized")

    while True:
      nextScreen = currentScreen.run()
      drawBlank()  #may not be necessary...could require screens to do this
      currentScreen = screens[nextScreen]
