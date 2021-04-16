from get_buttons import read_long_short

while True:
  press = read_long_short()
  
  if (press != None):
  
    if (press[2] == "S"):
      print("Short!")
    elif (press[2] == "L"):
      print("Long!")
