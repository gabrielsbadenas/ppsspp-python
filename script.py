import psp2d
font = psp2d.Font("font.png")
image = psp2d.Image(480, 272)
screen = psp2d.Screen()
CLEAR_COLOR = psp2d.Color(0,0,0)
image.clear(CLEAR_COLOR)
font.drawText(image, 0, 0, "Hello World!")
font.drawText(image, 0, 30, "Press Circle to exit")
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
