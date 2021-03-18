#setting up global variables

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

  # Main game loop
  while gameStillGoing:

    # Handle a turn
    handleTurn(currentPlayer)

    # Check if the game is over
    checkGameOver()

    # Flip to the other player
    flipPlayer()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def displayBoard():
  print(tttBoard[0] + " | " + tttBoard[1] + " | " + tttBoard[2] + "     1 | 2 | 3")
  print(tttBoard[3] + " | " + tttBoard[4] + " | " + tttBoard[5] + "     4 | 5 | 6")
  print(tttBoard[6] + " | " + tttBoard[7] + " | " + tttBoard[8] + "     7 | 8 | 9")



# Handle a turn for an arbitrary player
def handleTurn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if tttBoard[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

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
  elif currentPlayer == "O":
    currentPlayer = "X"



playGame()