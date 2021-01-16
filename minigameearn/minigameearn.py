import pgzrun

# Game Window Size
WIDTH = 1280
HEIGHT = 720

#star
sun = Actor('sun',(WIDTH/2,HEIGHT/2))

earth = Actor('earth',(457, 156))

jupiter = Actor('jupiter',(220, 169))

mars = Actor('mars',(349, 359))

mercury = Actor('mercury',(176, 474))

neptune = Actor('neptune',(790, 130))

saturn = Actor('saturn',(1050, 210))

uranus = Actor('uranus',(887, 356))

venus = Actor('venus',(1054, 480))

planet_reset = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

planet = planet_reset

num = 0
score = 0

#bg
bg = Actor('problem_screen1')
music.play('bgmusic')

def draw():  
        screen.blit('problem_screen1',(0,0))
        screen.draw.text('SCORE : '+str(score),(1006, 75),color='white',fontsize = 40)  
        sun.draw()
        earth.draw()
        jupiter.draw()
        mars.draw()
        mercury.draw()
        neptune.draw()
        saturn.draw()
        uranus.draw()
        venus.draw()
        if (num == 8):
            music.stop()
            screen.clear()
            screen.blit('problem_screen1',(0,0))
            screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)

def update():
    sun.angle += 1
    if (sun.angle == 360):
        sun.angle = 0

def on_mouse_down(pos,button):
    global score,num
    if mercury.collidepoint(pos):
        if (num == 0):
            score = 1
            num = 1
            sounds.win.play()
        elif (num != 0):
            score = 0
            num = 0
            sounds.over.play()
    if venus.collidepoint(pos):
        if (num == 1):
            score = 2
            num = 2
            sounds.win.play()
        elif (num != 1):
            score = 0
            num = 0
            sounds.over.play()
    if earth.collidepoint(pos):
        if (num == 2):
            score = 3
            num = 3
            sounds.win.play()
        elif (num != 2):
            score = 0
            num = 0
            sounds.over.play()
    if mars.collidepoint(pos):
        if (num == 3):
            score = 4
            num = 4
            sounds.win.play()
        elif (num != 3):
            score = 0
            num = 0
            sounds.over.play()
    if jupiter.collidepoint(pos):
        if (num == 4):
            score = 5
            num = 5
            sounds.win.play()
        elif (num != 4):
            score = 0
            num = 0
            sounds.over.play()
    if saturn.collidepoint(pos):
        if (num == 5):
            score = 6
            num = 6
            sounds.win.play()
        elif (num != 5):
            score = 0
            num = 0
            sounds.over.play()
    if uranus.collidepoint(pos):
        if (num == 6):
            score = 7
            num = 7
            sounds.win.play()
        elif (num != 6):
            score = 0
            num = 0
            sounds.over.play()
    if neptune.collidepoint(pos):
        if (num == 7):
            score = 8
            num = 8
            sounds.win.play()
        elif (num != 7):
            score = 0
            num = 0
            sounds.over.play()

pgzrun.go()
