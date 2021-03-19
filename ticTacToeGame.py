import get_buttons

#setting up global variables


# Making matrix locations

matXPos = [4, 36, 68,
	   4, 36, 68,
	   4, 36, 68]

matYPos = [4, 4, 4,
	  36, 36, 36,
	  68, 68, 68]
# Will hold our game board data 
tttBoard = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

# Lets us know if the game is over yet
gameStillGoing = True

# Tells us who the winner is
winner = None

# Tells us who the current player is 
currentPlayer = "O"


# Play a game of tic tac toe 
def playGame():

  displayBoard()

  if currentPlayer == 'O':
    matrix.SetImage(smallO,99,110)
  elif currentPlayer == 'X':
    matrix.SetImage(smallX,99,110)
  # Main game loop
  while gameStillGoing:

    # Handle a turn
    handleTurn(currentPlayer)

    # Check if the game is over
    checkGameOver()

    # Flip to the other player
    flipPlayer()

def showWinner():  
  # Since the game is over, print the winner or tie
  if winner == "X":
    print(winner + " won.")
    xWinSequence()
  elif winner == 'O':
    print(winner  +  " won.")
    oWinSequence()
  elif winner == None:
    print("Tie.")
    tieSequence()



# Display the game board to the screen
def displayBoard():
  print(tttBoard[0] + " | " + tttBoard[1] + " | " + tttBoard[2] + "     1 | 2 | 3")
  print(tttBoard[3] + " | " + tttBoard[4] + " | " + tttBoard[5] + "     4 | 5 | 6")
  print(tttBoard[6] + " | " + tttBoard[7] + " | " + tttBoard[8] + "     7 | 8 | 9")


def getPositionButtonArray():
  button = get_button.wait_for_press()
  numButton = button[0] + 8*button[1]
  if numButton == 0 or numButton == 1 or numButton == 8 or numButton == 9:
    position = 1
  elif numButton == 2 or numButton == 3 or numButton == 10 or numButton == 11:
    position = 2
  elif numButton == 4 or numButton == 5 or numButton == 12 or numButton == 13:
    position = 3
  elif numButton == 16 or numButton == 17 or numButton == 24 or numButton == 25:
    psoiton = 4
  elif numButton == 18 or numButton == 19 or numButton == 26 or numButton == 27:
    position = 5
  elif numButton == 20 or numButton == 21 or numButton == 28 or numButton == 29:
    position = 6
  elif numButton == 32 or numButton == 33 or numButton == 40 or numButton == 41:
    position = 7
  elif numButton == 34 or numButton == 35 or numButton == 42 or numButton == 43:
    position = 8
  elif numButton == 36 or numButton == 37 or numButton == 44 or numButton == 45:
    position = 9
  elif numButton == 55 or numButton == 56:
    exit()


def getPositionButton():
  button = get_buttons.wait_for_press()
  position = button[0] + 3*button[1] + 1
  print(position)
  print(button)
  return position


def getPosition():
  global imageX
  global imageO
  global matrix
  global curentPlayer
  # Get position from player
  print(currentPlayer + "'s turn.")
  position = input("Choose a position from 1-9: ")
  return position

# Handle a turn for an arbitrary player
def handleTurn(player):

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:
    position = getPositionButton()
   
    # Make sure the input is valid
    # while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #  position = input("Nope.  Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if tttBoard[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
     
  # Glenn's alt
  if player == 'O':
      temp_image = imageO
  elif player == 'X':
      temp_image = imageX
  matrix.SetImage(temp_image, matXPos[position], matYPos[position])




  # Put the game piece on the board
  tttBoard[position] = player


  # Show the game board
  displayBoard()


# Check if the game is over
def checkGameOver():
  checkWinner()
  checkTie()


# Check to see if somebody has won
def checkWinner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  rowWinner = checkRows()
  columnWinner = checkColumns()
  diagonalWinner = checkDiagonals()
  # Get the winner
  if rowWinner:
    winner = rowWinner
  elif columnWinner:
    winner = columnWinner
  elif diagonalWinner:
    winner = diagonalWinner
  else:
    winner = None

#  if winner == 'X':
#    winningLetter = winnerO
#  elif winner == 'O':
#    winnerX
#  matrix.SetImage(winningLetter,0,0)


# Check the rows for a win
def checkRows():
  # Set global variables
  global gameStillGoing
  # Check if any of the rows have all the same value (and is not empty)
  row1 = tttBoard[0] == tttBoard[1] == tttBoard[2] != "-"
  row2 = tttBoard[3] == tttBoard[4] == tttBoard[5] != "-"
  row3 = tttBoard[6] == tttBoard[7] == tttBoard[8] != "-"
  # If any row does have a match, flag that there is a win
  if row1 or row2 or row3:
    gameStillGoing = False
  # Return the winner
  if row1:
    return tttBoard[0] 
  elif row2:
    return tttBoard[3] 
  elif row3:
    return tttBoard[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def checkColumns():
  # Set global variables
  global gameStillGoing
  # Check if any of the columns have all the same value (and is not empty)
  column1 = tttBoard[0] == tttBoard[3] == tttBoard[6] != "-"
  column2 = tttBoard[1] == tttBoard[4] == tttBoard[7] != "-"
  column3 = tttBoard[2] == tttBoard[5] == tttBoard[8] != "-"
  # If any row does have a match vertically, flag the win
  if column1 or column2 or column3:
    gameStillGoing = False
  # Return the who the winner is
  if column1:
    return tttBoard[0] 
  elif column2:
    return tttBoard[1] 
  elif column3:
    return tttBoard[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def checkDiagonals():
  global gameStillGoing
  # Check if any of the columns have all the same value (and is not empty)
  diagonal1 = tttBoard[0] == tttBoard[4] == tttBoard[8] != "-"
  diagonal2 = tttBoard[2] == tttBoard[4] == tttBoard[6] != "-"
  # If any row does have a match diagonally, flag the win
  if diagonal1 or diagonal2:
    gameStillGoing = False
  # Return the who winner is
  if diagonal1:
    return tttBoard[0] 
  elif diagonal2:
    return tttBoard[2]
  # Or return None if there is no winner so far
  else:
    return None


# Check if there is a tie
def checkTie():

  global gameStillGoing
  # If board is full, return a tied game
  if "-" not in tttBoard:
    gameStillGoing = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flipPlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
    matrix.SetImage(smallO,99,110)
  elif currentPlayer == "O":
    currentPlayer = "X"
    matrix.SetImage(smallX,99,110)


from time import sleep
from datetime import datetime

import random

# Graphics imports, constants and structures
from rgbmatrix import RGBMatrix, RGBMatrixOptions 
from PIL import Image, ImageDraw, ImageFont



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

matrix = RGBMatrix(options = options)

last_update_time = datetime.now()
current_time = datetime.now()
deltaT = current_time = last_update_time

# Putting the images/gifs in
background = Image.open("TTT/Gameboard_TTT.png").convert("RGB")
background = background.resize((total_rows,total_columns))

smallX = Image.open("TTT/X_TTT.png").convert("RGB")
smallX = smallX.resize((16,16))

smallO = Image.open("TTT/O_TTT.png").convert("RGB")
smallO = smallO.resize((16,16))

imageX = Image.open("TTT/X24_24_TTT.png").convert("RGB")
imageX = imageX.resize((24,24))

imageO = Image.open("TTT/O24_24_TTT.png").convert("RGB")
imageO = imageO.resize((24,24))

frameTime = 0.25

def oWinSequence(): 
  global frameTime
 
  oWinScreen1 = Image.open("TTT/Owins_TTT.gif01.gif").convert("RGB")
  oWinScreen1 = oWinScreen1.resize((total_rows,total_columns))

  oWinScreen2 = Image.open("TTT/Owins_TTT.gif02.gif").convert("RGB")
  oWinScreen2 = oWinScreen2.resize((total_rows,total_columns))

  oWinScreen3 = Image.open("TTT/Owins_TTT.gif03.gif").convert("RGB")
  oWinScreen3 = oWinScreen3.resize((total_rows,total_columns))

  oWinScreen4 = Image.open("TTT/Owins_TTT.gif04.gif").convert("RGB")
  oWinScreen4 = oWinScreen4.resize((total_rows,total_columns))

  for times in range(0,5):
    matrix.SetImage(oWinScreen1,0,0)
    sleep(frameTime)

    matrix.SetImage(oWinScreen2,0,0)
    sleep(frameTime)

    matrix.SetImage(oWinScreen3,0,0)
    sleep(frameTime)

    matrix.SetImage(oWinScreen4,0,0)
    sleep(frameTime)


def xWinSequence():
  global frameTime

  xWinScreen1 = Image.open("TTT/Xwins_TTT.gif01.gif").convert("RGB")
  xWinScreen1 = xWinScreen1.resize((total_rows,total_columns))

  xWinScreen2 = Image.open("TTT/Xwins_TTT.gif02.gif").convert("RGB")
  xWinScreen2 = xWinScreen2.resize((total_rows,total_columns))

  xWinScreen3 = Image.open("TTT/Xwins_TTT.gif03.gif").convert("RGB")
  xWinScreen3 = xWinScreen3.resize((total_rows,total_columns))

  xWinScreen4 = Image.open("TTT/Xwins_TTT.gif04.gif").convert("RGB")
  xWinScreen4 = xWinScreen4.resize((total_rows,total_columns))

  for xtimes in range(0,5):
    matrix.SetImage(xWinScreen1,0,0)
    sleep(frameTime)

    matrix.SetImage(xWinScreen2,0,0)
    sleep(frameTime)

    matrix.SetImage(xWinScreen3,0,0)
    sleep(frameTime)

    matrix.SetImage(xWinScreen4,0,0)
    sleep(frameTime)


def tieSequence():
  global frameTime

  tieScreen1 = Image.open("TTT/Tie_TTT.gif01.gif").convert("RGB")
  tieScreen1 = tieScreen1.resize((total_rows,total_columns))

  tieScreen2 = Image.open("TTT/Tie_TTT.gif02.gif").convert("RGB")
  tieScreen2 = tieScreen2.resize((total_rows,total_columns))

  tieScreen3 = Image.open("TTT/Tie_TTT.gif03.gif").convert("RGB")
  tieScreen3 = tieScreen3.resize((total_rows,total_columns))

  tieScreen4 = Image.open("TTT/Tie_TTT.gif04.gif").convert("RGB")
  tieScreen4 = tieScreen4.resize((total_rows,total_columns))

  tieScreen5 = Image.open("TTT/Tie_TTT.gif05.gif").convert("RGB")
  tieScreen5 = tieScreen5.resize((total_rows,total_columns))

  tieScreen6 = Image.open("TTT/Tie_TTT.gif06.gif").convert("RGB")
  tieScreen6 = tieScreen6.resize((total_rows,total_columns))

  for tieTimes in range(0,4):
    matrix.SetImage(tieScreen1,0,0)
    sleep(frameTime)

    matrix.SetImage(tieScreen2,0,0)
    sleep(frameTime)

    matrix.SetImage(tieScreen3,0,0)
    sleep(frameTime)

    matrix.SetImage(tieScreen4,0,0)
    sleep(frameTime)

    matrix.SetImage(tieScreen5,0,0)
    sleep(frameTime)

    matrix.SetImage(tieScreen6,0,0)
    sleep(frameTime)


'''
#oWinImages = (oWinScreen1, oWinScreen2, oWinScreen3, oWinScreen4)
xWinImages = (xWinScreen1, xWinScreen2, xWinScreen3, xWinScreen4)
tieImages = (tieScreen1, tieScreen2, tieScreen3, tieScreen4, tieScreen5, tieScreen6)

#num_o_images = len(oWinImages)
#num_x_images = len(xWinImages)
#num_tie_images = len(tieImages)

o_image_index = 0
x_image_index = 0
tie_image_index = 0

def show_gif(image_list, time_between_images, num_cycles):
  current_cycle = 0 
  num_frames = len(image_list)
  current_frame = 0
  last_update_time = datetime.now()

  matrix.SetImage(image_list[current_frame],0,0)

  while True:

    current_time = datetime.now()
    deltaT = current_time - last_update_time

    if deltaT.total_seconds() > time_between_images:
       print("frame "+str(current_frame)+" cycle "+str(current_cycle))
       current_frame = (current_frame + 1)
       if current_frame == num_frames:
         current_cycle = current_cycle + 1
         if current_cycle >= num_cycles:
           return  
         current_frame = current_frame % num_frames 
       matrix.SetImage(image_list[current_frame],0,0)
       last_update_time = current_time

    sleep(0.01)
'''
     
  
  

    




#Placing the first background image

matrix.SetImage(background,0,0)

while True:

  playGame()

  showWinner()

  sleep(5)

  gameStillGoing = True
  winner = None

  tttBoard =["-","-","-",
             "-","-","-",
             "-","-","-"]

  matrix.SetImage(background,0,0)
