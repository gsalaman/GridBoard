# Text-based example of using an array lookup to map physical buttons 
# to logical buttons.

# We've got two ways to represent a button
# The PHYSICAL button identifier is the x,y pair showing the button location,
# where 0,0 is top-left (to match our matrix graphics) and 7,7 is bottom-right.
#
# The LOGICAL button identifier maps these physical buttons to other spaces
# that our program can use.  The array below maps the physical buttons into
# the 1-9 that represent our tic-tac-toe board.
# -1 means that button isn't in use
# 0 is used for our back button.

map_array = \
[
# X= 0   1   2   3   4   5   6   7  
  [  1,  1,  2,  2,  3,  3, -1, -1 ],   # y = 0
  [  1,  1,  2,  2,  3,  3, -1, -1 ],   # y = 1
  [  4,  4,  5,  5,  6,  6, -1, -1 ],   # y = 2
  [  4,  4,  5,  5,  6,  6, -1, -1 ],   # y = 3
  [  7,  7,  8,  8,  9,  9, -1, -1 ],   # y = 4
  [  7,  7,  8,  8,  9,  9, -1, -1 ],   # y = 5
  [ -1, -1, -1, -1, -1, -1, -1, -1 ],   # y = 6
  [  0,  0, -1, -1, -1, -1, -1, -1 ]    # y = 7
]
 
try:
  while True:
    line = input("x,y pair: ")

    print(line)

    x_val = line[0]
    y_val = line[1]

    if (x_val < 0 or x_val > 7 or y_val < 0 or y_val > 7):
      print("need numbers...try again")
      continue

    logical_button = map_array[y_val][x_val]

    print("Logical button: "+str(logical_button)) 

except KeyboardInterrupt:
  exit(0) 
