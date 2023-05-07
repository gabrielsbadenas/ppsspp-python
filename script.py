import psp2d
from time import time,localtime,sleep
import random
start = time()
Image = psp2d.Image
Screen = psp2d.Screen
Font = psp2d.Font
Color = psp2d.Color

font = Font("font.png")
image = Image(480, 272)
screen = Screen()
swap = screen.swap

size = 16
horizontal = 480-size
vertical = 272-size

white = psp2d.Color(255,255,255)
light = psp2d.Color(170,170,170)
dark = psp2d.Color(86,86,86)
black = psp2d.Color(0,0,0)
blue = psp2d.Color(164,219,232)
CLEAR_COLOR =black 

image.clear(dark)

gabi = psp2d.Image('gabissineun.png')

sprite = psp2d.Image('baereul.png')

def getTime():
    return str(int(time()-start))
def timer():
    image.clear(dark)
    font.drawText(image, 0, 0, getTime())
    font.drawText(image,random.randint(0,horizontal),random.randint(0,vertical),"'")
    image.fillRect(0,vertical,480,16,psp2d.Color(164,219,232))#blue)
    screen.blit(image)
    render()
    logo()
    swap()
def logo():
    screen.blit(gabi,0,0,16,16,480/2,272/2,True)
def render():
    screen.blit(sprite, 0, 0, 16,16, int(getTime()), 272-32, True)

def main():
    x = True
    while x == True:
        #sleep(1/24)
        timer()
        #render()
        pad = psp2d.Controller()
        if pad.circle:
            font.drawText(image, 0, 60, "Goodbye!")
            screen.blit(image)
            swap()
            x = False

main()
