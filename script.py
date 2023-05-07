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
sonsu = Image('sonsu.png')
sprite = psp2d.Image('baereul.png')

def getTime():
    return str(int(time()-start))

def timer():
    image.clear(dark)
    font.drawText(image, 0, 0, getTime())
    font.drawText(image, 200, 100, 'press o to start')
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
class Pos:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Space(Pos):
    def __init__(self,x,y,data):
        super(Space, self).__init__(x,y)
        self.data=data
        self.position = Pos(x*16,y*16)
    def draw(self):
        if self.data=='player':
            player(self.position.x,self.position.y)

def matrix():
    rows = 30
    cols = 16
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append([i, j, False])
        matrix.append(row)
    return matrix

def searchMatrix(matriz):
    for i in range(30):
        for j in range(16):
            tmp = matriz[i][j]
            if tmp[2]:
                player(tmp[0]*16,tmp[1]*16)

def player(x,y):
    screen.blit(sonsu,0,0,16,16,x,y,True)
def scene():
    running = True
    spaces = matrix()
    spaces[1][0][2]=True
    while running==True:
        pad2 = psp2d.Controller()
        image.clear(black)
        font.drawText(image, 0, 100, str(spaces[0][0][2]))
        screen.blit(image)
        logo()
        #player(0,0)
        searchMatrix(spaces)
        swap()
        if pad2.circle:
            running = False
            break

def main():
    x = True
    while x == True:
        #sleep(1/24)
        timer()
        #render()
        pad1 = psp2d.Controller()
        if pad1.circle:
            font.drawText(image, 0, 60, "starting")
            screen.blit(image)
            swap()
            sleep(1)
            x = False
            break

main()
scene()
