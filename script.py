import psp2d

Image = psp2d.Image
Screen = psp2d.Screen
Font = psp2d.Font

font = psp2d.Font("font.png")
image = psp2d.Image(480, 272)
screen = psp2d.Screen()
class Position:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Sprite:
    def __init__(self,path,position):
        self.image = Image(path)
        self.width = self.image.width
        self.height = self.image.height
        self.positionX = position.x
        self.positionY = position.y
        screen.blit(self.image, 0, 0, self.width,self.height, self.position.X, self.position.Y, True)


white = psp2d.Color(255,255,255)
light = psp2d.Color(170,170,170)
dark = psp2d.Color(86,86,86)
black = psp2d.Color(0,0,0)
CLEAR_COLOR =black 

image.clear(CLEAR_COLOR)
font.drawText(image, 0, 0, "hola mundo")
font.drawText(image, 0, 30, "Press Circle to exit")
image.putPixel(200,200,light)
image.fillRect(0,0,16,16,dark)
#actualiza la imagen
sprite = psp2d.Image('gabissineun.png')
screen.blit(sprite,480-16,272-16)
screen.blit(image)
screen.blit(sprite, 0, 0, 16,16, 400, 200, True)
screen.swap()
x = True
while x == True:
    pad = psp2d.Controller()
    if pad.circle:
        font.drawText(image, 0, 60, "Goodbye!")
        screen.blit(image)
        screen.swap()
        x = False
