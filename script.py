import psp2d
font = psp2d.Font("font.png")
image = psp2d.Image(480, 272)
screen = psp2d.Screen()
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
screen.blit(image)
screen.swap()
x = True
while x == True:
    pad = psp2d.Controller()
    if pad.circle:
        font.drawText(image, 0, 60, "Goodbye!")
        screen.blit(image)
        screen.swap()
        x = False
