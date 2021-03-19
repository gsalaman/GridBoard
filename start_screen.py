from PIL import Image, ImageDraw, ImageFont

def mainScreen(rgbmatrix):
    mainscreen = Image.open("converted-gifs/Top/Homescreen/Homescreen.gif02.gif").convert("RGB")
    rgbmatrix.SetImage(mainscreen,0,0)
