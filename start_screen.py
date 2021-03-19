from PIL import Image, ImageDraw, ImageFont

from get_buttons import read

def mainScreen(rgbmatrix):
    mainscreen = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif02.gif").convert("RGB")
    rgbmatrix.SetImage(mainscreen,0,0)

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
