import pgzrun
import time
from random import randint

# Game Window Size
WIDTH = 1280
HEIGHT = 720

#bg
bg = Actor('problem_screen')
music.play('bgmusic')

# Actors
leafAmount = 10
leaf = []
leafDie = []
leaf_model = []
broom = Actor('broom')

# Actors Control
velX = []
velY = []

# Game Control Varibles
score = 0
gameEnd = False


def init_speed_leaf():
    global velX, velY, leafAmount
    
    for index in range(leafAmount):
        velX.append(randint(-5, 5))
        velY.append(randint(-5, 5))
        
        # Check is speed != 0
        while velX[index] == 0 or velY[index] == 0:
            velY[index] = randint(-5, 5)
            velX[index] = randint(-5, 5)
        
def init_leaf():
    global leaf, leafAmount, leafDie

    for index in range(leafAmount):
        leaf.append(Actor(f'leaf{randint(1,4)}'))
        leafDie.append(False)

def init_leaf_position():
    global leaf, leafAmount
    
    for index in range(leafAmount):
        x = randint(90, 400)
        y = randint(90, 300)

        leaf[index].pos = (640,360)

def endgame():
    global gameEnd

    if score == 10:
        gameEnd = True

def actorMove():
    global leaf, leafDie, leafAmount, velX, velY, WIDTH, HEIGHT

    for index in range(leafAmount):
        if not leafDie[index]:
            # Area Check [Left, Right]
            if (leaf[index].left < 90):
                velX[index] = -velX[index]
            elif (leaf[index].right > 1150):
                velX[index] = -velX[index]
            
            # Area Check [Top, Bottom]
            if (leaf[index].top < 56):
                velY[index] = -velY[index]
            elif (leaf[index].bottom > 556):
                velY[index] = -velY[index]

            # Actors Move
            leaf[index].x += velX[index]
            leaf[index].y += velY[index]
            #print(f'#{index+1} ({velX[index]}, {velY[index]})')

def set_leaf_die(leaf):
    global leafDie, leafAmount, score

    for index in range(leafAmount):
        if leaf == index:
            leafDie[index] = True
            break

def countScore():
    global score, gameEnd, leafAmount

    count = 0

    for index in range(leafAmount):
        if(leafDie[index]):
            count += 1

    score = count

    if(score >= leafAmount):
        gameEnd = True

def draw_minigame1():
    global leafDie, leafAmount, gameEnd

    
    screen.blit('problem_screen',(0,0))

    if (not gameEnd):

        for index in range(leafAmount):
            if (not leafDie[index]):
                leaf[index].draw()

        broom.draw()
        
    else:
        music.stop()
        screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)

def draw():
    draw_minigame1()
    

    
def update(delta):
    global score

    endgame()
    countScore()

    actorMove()

def on_mouse_down(pos,button):
    global leaf, leafAmount
    print(pos)
    for index in range(leafAmount):
        if leaf[index].collidepoint(pos):
            sounds.fub.play()
            set_leaf_die(index)
            break

def on_mouse_move(pos,rel,buttons):
    broom.pos = pos

    # Area Check [Left, Right]
    if (broom.x < 100):
        broom.x = 100
    if (broom.x > 1150):
        broom.x = 1150
            
    # Area Check [Top, Bottom]
    if (broom.y < 90):
        broom.y = 90
    if (broom.y > 540):
        broom.y = 540

#Start
init_leaf()
init_leaf_position()
init_speed_leaf()

pgzrun.go()
