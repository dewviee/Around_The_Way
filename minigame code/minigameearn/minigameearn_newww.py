import pgzrun
from random import randint

# Game Window Size
WIDTH = 1280
HEIGHT = 720

#star
sun = Actor('sun',(WIDTH/2,HEIGHT/2))

earth = Actor('earth')

jupiter = Actor('jupiter')

mars = Actor('mars')

mercury = Actor('mercury')

neptune = Actor('neptune')

saturn = Actor('saturn')

uranus = Actor('uranus')

venus = Actor('venus')

planets_reset = planets_pos = planets = []

def planets_reset():
        global planets, planets_pos

        planets_reset = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

        planets_pos = [(457, 156), (220, 169),(349, 359),(176, 474),(790, 130),(1050, 210),(887, 356),(1054, 480)]
        
        planets = planets_reset.copy()

        for i in range(len(planets_pos)):
                print (i)
                temp = randint(0,len(planets_pos)-1)
                planets[i].pos = planets_pos[temp]
                planets_pos.remove(planets_pos[temp])
        

planets_reset()    
               
num = 0
score = 0

#bg
bg = Actor('problem_screen1')
music.play('bgmusic')

def draw():  
        screen.blit('problem_screen1',(0,0))
        screen.draw.text('SCORE : '+str(score),(1006, 75),color='white',fontsize = 40)  
        sun.draw()

        for ppplanet in planets:
            ppplanet.draw()
            
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
    global score,num, planets
    if mercury.collidepoint(pos):
        if (num == 0):
            score = 1
            num = 1
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 0):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if venus.collidepoint(pos):
        if (num == 1):
            score = 2
            num = 2
            sounds.win.play()
            planets.remove(planets[0])            
        elif (num != 1):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if earth.collidepoint(pos):
        if (num == 2):
            score = 3
            num = 3
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 2):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if mars.collidepoint(pos):
        if (num == 3):
            score = 4
            num = 4
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 3):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if jupiter.collidepoint(pos):
        if (num == 4):
            score = 5
            num = 5
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 4):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if saturn.collidepoint(pos):
        if (num == 5):
            score = 6
            num = 6
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 5):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if uranus.collidepoint(pos):
        if (num == 6):
            score = 7
            num = 7
            sounds.win.play()
            planets.remove(planets[0])
        elif (num != 6):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()
    if neptune.collidepoint(pos):
        if (num == 7):
            score = 8
            num = 8
            sounds.win.play()
            planets_reset()
        elif (num != 7):
            score = 0
            num = 0
            sounds.over.play()
            planets_reset()

pgzrun.go()
