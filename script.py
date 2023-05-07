import psp2d
from time import time,localtime,sleep
start = time()
Image = psp2d.Image
Screen = psp2d.Screen
Font = psp2d.Font

font = Font("font.png")
image = Image(480, 272)
screen = Screen()
swap = screen.swap
class Position:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Sprite:
    def __init__(self,path,position):
        self.image = psp2d.Image(path)
        self.width = self.image.width
        self.height = self.image.height
        self.position = position
        self.positionX = position.x
        self.positionY = position.y
        screen.blit(self.image, 0, 0, self.width,self.height, self.positionX, self.positionY, True)
        screen.swap()

white = psp2d.Color(255,255,255)
light = psp2d.Color(170,170,170)
dark = psp2d.Color(86,86,86)
black = psp2d.Color(0,0,0)
CLEAR_COLOR =black 

image.clear(dark)
#font.drawText(image, 0, 0, "hola mundo")
#font.drawText(image, 0, 30, "Press Circle to exit")
#image.putPixel(200,200,light)
#image.fillRect(0,0,16,16,dark)
#actualiza la imagen
sprite = psp2d.Image('gabissineun.png')
#sprite = Sprite('gabissineun.png',Position(480-16,272-16))
#screen.blit(sprite,480-16,272-16)
#screen.blit(image)
#screen.blit(sprite, 0, 0, 16,16, 400, 200, True)
#swap()
def getTime():
    return str(int(time()-start))
def timer():
    image.clear(dark)
    font.drawText(image, 0, 0, getTime())
    screen.blit(image)
    render()
    swap()

def render():
    #sprite = Image('gabissineun.png')
    screen.blit(sprite, 0, 0, 16,16, int(getTime()), 272-16, True)
    #swap()

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
