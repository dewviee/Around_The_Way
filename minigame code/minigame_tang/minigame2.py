import pgzrun
from random import randint

# Game Window Size
WIDTH = 1280
HEIGHT = 720

#set x , y
velX = []
velY = []

#set game controller
gameEnd = False
Score = 0


#bg
bg = Actor('problem_screen1')
music.play('bgmusic')

# INIT SPEED
minigame2_speed = []
for i in range(6):
    minigame2_speed.append(randint(3,5))

def draw():
    if (not gameEnd):
        screen.blit('problem_screen1',(0,0))
        Score_string = "Get 50 objects to complete the task : " + str(int(Score))
        screen.draw.text(Score_string, topright=(WIDTH - 10, 10), color='green', fontsize=28)
        basket.draw()
        box.draw()
        shampoo.draw()
        microwave.draw()
        mobile.draw()
        bag.draw()
        cat.draw()
        endgame()
    else:
        sounds.collect.stop()
        music.stop()
        screen.clear()
        screen.blit('problem_screen1',(0,0))
        screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)
        

def place_box():
    box.x = randint(95,WIDTH - 95)
    box.y = 64
    box.left < 56
    box.right > 556

def place_shampoo():
    shampoo.x = randint(95,WIDTH - 95)
    shampoo.y = 64
    shampoo.left < 56
    shampoo.right > 556
def place_microwave():
    microwave.x = randint(95,WIDTH - 95)
    microwave.y = 64
    microwave.left < 56
    microwave.right > 556
def place_mobile():
    mobile.x = randint(95,WIDTH - 95)
    mobile.y = 64
    mobile.left < 56
    mobile.right > 556
def place_bag():
    bag.x = randint(95,WIDTH - 95)
    bag.y = 64
    box.left < 56
    box.right > 556    
def place_cat():
    cat.x = randint(95,WIDTH - 95)
    cat.y = 64
    cat.left < 56
    cat.right > 556
def random_speed():
    cat.y += minigame2_speed[0]
    bag.y += minigame2_speed[1]
    mobile.y += minigame2_speed[2]
    microwave.y += minigame2_speed[3]
    shampoo.y += minigame2_speed[4]
    box.y += minigame2_speed[5]

def on_mouse_move(pos,rel,buttons):
    basket.pos = (pos[0],500)

    # Area Check [Left, Right]
    if (basket.x < 100):
        basket.x = 100
    if (basket.x > 1150):
        basket.x = 1150
            
    # Area Check [Top, Bottom]
    if (basket.y < 90):
        basket.y = 90
    if (basket.y > 540):
        basket.y = 540

    
def update():
    global Score
    random_speed()
    if(cat.y > 527):
        place_cat()
        minigame2_speed[0] = randint(3,5)
    if(bag.y > 510):
        place_bag()
        minigame2_speed[1] = randint(3,5)
    if(shampoo.y > 510):
        place_shampoo()
        minigame2_speed[2] = randint(3,5)
    if(microwave.y > 510):
        place_microwave()
        minigame2_speed[3] = randint(3,5)
    if(mobile.y > 510):
        place_mobile()
        minigame2_speed[4] = randint(5,7)
    if(box.y > 510):
        place_box()
        minigame2_speed[5] = randint(5,7)

    basket_collected = basket.colliderect(cat)
    if(basket_collected):
        place_cat()
        Score += 1
        sounds.collect.play()
        
    basket_collected = basket.colliderect(box)
    if(basket_collected):
        place_box()
        Score += 1
        sounds.collect.play()
        
    basket_collected = basket.colliderect(bag)
    if(basket_collected):
        place_bag()
        Score += 1
        sounds.collect.play()
        
    basket_collected = basket.colliderect(shampoo)
    if(basket_collected):
        place_shampoo()
        Score += 1
        sounds.collect.play()
        
    basket_collected = basket.colliderect(microwave)
    if(basket_collected):
        place_microwave()
        Score += 1
        sounds.collect.play()
        
    basket_collected = basket.colliderect(mobile)
    if(basket_collected):
        place_mobile()
        Score += 1
        sounds.collect.play()
        
def endgame():
    global gameEnd
    if Score == 50:
        gameEnd = True


def on_mouse_down(pos,button):
    print(pos)
    




basket = Actor('basket_1',(628, 507))
box = Actor('box_2',(randint(1,1280),0))
shampoo = Actor('shampoo_1',(randint(1,1280),0))
microwave = Actor('microwave_1',(randint(1,1280),0))
mobile = Actor('mobile_1',(randint(1,1280),0))
bag = Actor('bag_1',(randint(1,1280),0))
cat = Actor('cat_1',(randint(1,1280),0))
pgzrun.go()
