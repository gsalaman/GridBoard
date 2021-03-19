## This is the main program running the gridboard ##

from rgbmatrix import RGBMatrix, RGBMatrixOptions

import ticTacToeGame #games

import start_screen #UI elements
import game_select

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

if __name__ == '__main__':
    start_screen.mainScreen(matrix)
    print("initalized")


