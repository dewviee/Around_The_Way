import pgzrun

import time

from random import randint


WIDTH = 1280
HEIGHT = 720

''' INIT CONFIG FOR CUSTOM MENU '''

player_speed = 7

enemy_spawn_rate = 20

problem_event_rate = 2

ship_hp = 100

enemy_shoot_rate = 25

problem_rate = 5

# 1 day = 18 
cargoTime = 0

cargoEnd = 180

planet_score = 0

''''''''''''''''''''''''''''''''''''''''''''''''''''''

def time_count():
    global cargoTime
    if not(problem_active):
        cargoTime += 1

######################## MINIGAME1 #######################################
def init_minigame1():
    global bg, leafAmount, leaf, leafDie, leaf_model, broom, velX, velY, score, gameEnd
    #bg
    bg = Actor('problem_screen')

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
    global leafDie, leafAmount, gameEnd, event

    global problem_active, finish_problem 
    
    screen.blit('problem_screen',(0,0))

    if (not gameEnd):

        for index in range(leafAmount):
            if (not leafDie[index]):
                leaf[index].draw()

        broom.draw()
        
    else:
        problem_active = False
        finish_problem = True
        event = 0
        
#####################################################################################################


################################## MINIGAME2 ########################################################

def init_minigame2():
    global velX,velY,gameEnd, Score,bg,minigame2_speed
    
    #set x , y
    velX = []
    velY = []

    #set game controller
    gameEnd = False
    Score = 0

    num = 0
    score = 0

    #bg
    bg = Actor('problem_screen1')
    # INIT SPEED
    minigame2_speed = []
    for i in range(6):
        minigame2_speed.append(randint(3,5))

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

def endgame2():
    global gameEnd,problem_active,finish_problem, event
    if Score >= 50:
        gameEnd = True
        problem_active = False
        finish_problem = True
        event = 0
        

basket = Actor('basket_1',(628, 507))
box = Actor('box_2',(randint(1,1280),0))
shampoo = Actor('shampoo_1',(randint(1,1280),0))
microwave = Actor('microwave_1',(randint(1,1280),0))
mobile = Actor('mobile_1',(randint(1,1280),0))
bag = Actor('bag_1',(randint(1,1280),0))
cat = Actor('cat_1',(randint(1,1280),0))

#####################################################################################################        



###################################### MINIGAME 3 ###################################################

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
    global planets, planets_pos, num, planet_score

    planets_reset = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    planets_pos = [(457, 156), (220, 169),(349, 359),(176, 474),(790, 130),(1050, 210),(887, 356),(1054, 480)]
        
    planets = planets_reset.copy()

    for i in range(len(planets_pos)):
        temp = randint(0,len(planets_pos)-1)
        planets[i].pos = planets_pos[temp]
        planets_pos.remove(planets_pos[temp])

    num = 0
    planet_score = 0
    
planets_reset()    
               


#bg
bg = Actor('problem_screen1')


##################################################################################################### 

def fixing_sound_delay():
    global fixing_sound
    fixing_sound = False

fix_game = Actor('fix_engine_screen')
fix_game2 = Actor('fix_engine_screen_layer2')


display = 'menu'

can_use_shooting = can_use_engine = can_use_problem = False

use_shooting = use_engine = use_problem = use_object = False

problem_active = False

finish_problem = False

fixing_sound = False

# STORE WHAT EVENT THIS TIME
event = -1

# STORE ENEMY DATA
enemys = []

def start_game():
    global can_use_shooting, can_use_engine, can_use_problem
    global use_shooting, use_engine, use_object, day

    global event, enemys, planet_score

    global cargoTime, cargoEnd, ship_hp

    global problem_active, finish_problem, fixing_sound

    ship_hp = 100
    cargoTime = 0

    cargoEnd = 180
    
    can_use_shooting = can_use_engine = can_use_problem = False

    use_shooting = use_engine = use_problem = use_object = False

    problem_active = False

    finish_problem = False

    fixing_sound = False

    # STORE WHAT EVENT THIS TIME
    event = -1

    # STORE ENEMY DATA
    enemys = []
        
    music.play('space_bgm')
    music.set_volume(0.3)

    # Start Game
    clock.schedule_interval(random_event,1.0)
    clock.schedule_interval(problem_active_loop,1.0)
    clock.schedule_interval(time_count,1.0)

    planet_score = 0

def random_event():
    global enemy_spawn_rate, problem_event_rate, ship_hp, problem_active, event

    global bg, leafAmount, leaf, leafDie, leaf_model, broom, velX, velY, score, gameEnd
    
    if randint(1,100) <= enemy_spawn_rate:
        enemys.append(Actor('ufo_shoot3'))

        # Random position of ufo
        enemys[len(enemys)-1].pos = (randint(130,1150),randint(89,409))
    
    for i in range(len(enemys)):
        # Random ENEMY SHOOTING!
        if randint(1,100) < enemy_shoot_rate:
            # Random decrease HP
            ship_hp -= randint(1,5)

    # Random when the event happend
    if problem_active == False:
        if randint(1,100) <= problem_rate:
            gameEnd = False
            problem_active = True
            finish_problem = False
            event = randint(1,3)

            if event == 1:
                init_minigame1()
                
                init_leaf()
                init_leaf_position()
                init_speed_leaf()
                
            elif event == 2:
                init_minigame2()

            elif event == 3:
                planets_reset()

def draw():
    
    # This is for game rendering
    
    if display == 'playing':
        playing()
        if cargoTime < 5:
            screen.draw.text('Take care you ship until day 10!',midbottom = (WIDTH/2,HEIGHT/2),fontsize=50,color = 'blue')
            
    if display == 'menu':
        menu()
    if ship_hp == -100:
        bg_fixing.draw()
        screen.draw.text('You cargo has been destroy by alien! Please "spacebar" to play again',midbottom = (WIDTH/2,HEIGHT/2),fontsize=50,color = 'RED')
        
    if cargoTime == cargoEnd+1:
        bg_fixing.draw()
        screen.draw.text('You cargo has been ship! Please "spacebar" to play again',midbottom = (WIDTH/2,HEIGHT/2),fontsize=50,color = 'green')
    if (can_use_shooting or can_use_problem or can_use_engine) and use_object == False:
        screen.draw.text('E', (player.x + 25,player.y - 70), fontsize=50, color = (255, 255, 255))

    screen.draw.text('THIS GAME IS MAKING FOR KMUTNB Problem and Solving Project', bottomleft = (10,710), fontsize=25, color = (255, 0, 0))
def update():
    global score, cargoTime, ship_hp

    global gameEnd,  problem_active, finish_problem, event, planet_score, event
    
    if display == 'playing':
        player_control()
        can_use_object()

        
        if use_problem and problem_active:
            if event == 1:
                endgame()
                countScore()

                actorMove()

            elif event == 2:
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
                endgame2()

                
            elif event == 3:
                sun.angle += 1
                if (sun.angle == 360):
                    sun.angle = 0  
                    

        if ship_hp <= 0:
            ship_hp = -100
            reset_game()

        
        if cargoTime == cargoEnd:
            cargoTime += 1
            reset_game()
            
        
            
                    
''' MOUSE CLICK '''
def on_mouse_down(pos, button):
    global display
    
    global leaf, leafAmount

    global score,num, planets, planet_score

    global gameEnd, problem_active, finish_problem, event 

    print(planet_score)
    print(pos)
    # if play:
    if display == 'playing':
        
        if use_shooting:
            sounds.laser.play()
            explosion_num = randint(2,3)
            for enemy in enemys:
                if enemy.collidepoint(pos):
                    if explosion_num == 2:
                        sounds.explosion2.play()
                    elif explosion_num == 3:
                        sounds.explosion3.play()
                    print(explosion_num)
                    enemys.remove(enemy)
                    
        if use_problem and problem_active:
            if event == 1:
                for index in range(leafAmount):
                    if leaf[index].collidepoint(pos):
                        sounds.fub.play()
                        set_leaf_die(index)
                        break
            elif event == 3:
                if mercury.collidepoint(pos):
                    if (num == 0):
                        planet_score = 1
                        num = 1
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 0):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if venus.collidepoint(pos):
                    if (num == 1):
                        planet_score = 2
                        num = 2
                        sounds.win.play()
                        planets.remove(planets[0])            
                    elif (num != 1):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if earth.collidepoint(pos):
                    if (num == 2):
                        planet_score = 3
                        num = 3
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 2):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if mars.collidepoint(pos):
                    if (num == 3):
                        planet_score = 4
                        num = 4
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 3):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if jupiter.collidepoint(pos):
                    if (num == 4):
                        planet_score = 5
                        num = 5
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 4):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if saturn.collidepoint(pos):
                    if (num == 5):
                        planet_score = 6
                        num = 6
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 5):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if uranus.collidepoint(pos):
                    if (num == 6):
                        planet_score = 7
                        num = 7
                        sounds.win.play()
                        planets.remove(planets[0])
                    elif (num != 6):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
                if neptune.collidepoint(pos):
                    if (num == 7):
                        planet_score = 8
                        num = 8
                        sounds.win.play()
                        planets_reset()

                        gameEnd = True
                        problem_active = False
                        finish_problem = True
                        event = 0
                    elif (num != 7):
                        planet_score = 0
                        num = 0
                        sounds.over.play()
                        planets_reset()
    
    elif display == 'menu':
        if playbutton.collidepoint(pos):
            display = 'playing'
            start_game()
            
            


''' MOUSE MOVE '''
def on_mouse_move(pos, rel, buttons):
    global playbutton
    if display == 'menu':
        if playbutton.collidepoint(pos):
            playbutton = Actor('playbutton_active', topleft = (530, 332))
        else:
            playbutton = Actor('playbutton_idle', topleft = (530, 332))

    elif display == 'playing':

        if use_shooting:
            gun_left.angle = gun_left.angle_to(pos)
            gun_right.angle = gun_right.angle_to(pos)
            crosshair.pos = pos
        
        elif use_problem and problem_active:
            if event == 1:
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
            if event == 2:
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

def on_key_down(key, mod, unicode):
    global use_shooting, use_engine, use_problem, use_object, player_animation_count
    global ship_hp
    global fixing_sound
    print(key)

    if display == 'playing':
        if (use_shooting or use_engine or use_problem or use_object) == False:
            # WALKING ANIMATION
            if key == keys.D:
                clock.schedule_interval(player_walking_right,0.1)

            if key == keys.A:
                clock.schedule_interval(player_walking_left,0.1)

            
            if key == keys.W:
                clock.schedule_interval(player_walking_up,0.1)

                    
            if key == keys.S:
                clock.schedule_interval(player_walking_down,0.1)

        # fix engine
        if key == keys.SPACE:
            if use_engine:
                ship_hp += randint(1,7)
                if ship_hp > 100:
                    ship_hp = 100

                if fixing_sound == False:
                    fixing_sound = True
                    sounds.fixing_engine.play()
                    if ship_hp == 100:
                       sounds.fixing_engine.stop()
                    clock.schedule(fixing_sound_delay,4)


            if ship_hp == -100 or cargoTime == cargoEnd+1 :
                start_game()

    
                
        
        if key == keys.E:
            
            if can_use_shooting == True and use_shooting == False:
                use_shooting = True
                use_object = True
           
            elif can_use_engine and use_engine == False:
                use_engine = True
                use_object = True
            elif can_use_problem and use_problem == False:
                use_problem = True
                use_object = True

            else:
                # THIS IS FOR CLOSE EVENT SCREEN 
                if use_shooting:
                    use_shooting = False
                    use_object = False
                    
                if use_engine:
                    use_engine = False
                    use_object = False
                    
                if use_problem:
                    use_problem = False
                    use_object = False
                   
        

def on_key_up(key, mod):
    global player_animation_count

    if display == 'playing':
        # WALKING ANIMATION
        if key == keys.D:
            clock.unschedule(player_walking_right)
            player.image = player_animation[0][1]
            player_animation_count = 0
                
        if key == keys.A:
            clock.unschedule(player_walking_left)
            player.image = player_animation[0][0]
            player_animation_count = 0

        if key == keys.W:
            clock.unschedule(player_walking_up)
            player.image = player_animation[0][player_facing]

            player_animation_count = 0
                        
        if key == keys.S:
            clock.unschedule(player_walking_down)
            player.image = player_animation[0][player_facing]

            player_animation_count = 0
    
def menu():
    screen.fill((0, 26, 105))
    playbutton.draw()

'''                    PLAYING FUNCTION                '''

def playing():
    global gameEnd, problem_active, finish_problem, event
    
    spacebg.draw()
    
    shoot_screen_hover.draw()

    for enemy in enemys:
        enemy.draw()

    gun_left.draw()
    gun_right.draw()
    crosshair.draw()
    
    player.draw()

    if not(problem_active):    
        screen.draw.text(f'DAY : {cargoTime//18}',topright = (1250,30),fontsize = 50,color = 'white')
    else:
        screen.draw.text(f'DAY : {cargoTime//18}',topright = (1250,30),fontsize = 50,color = 'red')
    
    screen.draw.text(f'ENGINE HP: {ship_hp}',(1000,500),fontsize = 50,color = 'red')

    #hitbox_draw()

    if problem_active == True and not(use_problem or use_engine or use_shooting):
        problem_hover.draw()

    # DRAW PROBLEM SCREEN
    if use_problem and problem_active:
        
        if event == 1:
            draw_minigame1()
        elif event == 2:
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
                
            else:
                sounds.collect.stop()
                screen.clear()
                screen.blit('problem_screen1',(0,0))
                screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)
        elif event == 3:
            screen.blit('problem_screen1',(0,0))
            screen.draw.text('SCORE : '+str(planet_score),(1006, 75),color='white',fontsize = 40)  
            sun.draw()

            for ppplanet in planets:
                ppplanet.draw()
                
            if (planet_score == 8):

                screen.clear()
                screen.blit('problem_screen1',(0,0))
                screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)
                
    if use_problem and event == 0 :
        screen.blit('problem_screen',(0,0))
        screen.draw.text('Mission Complete',(473, 304),color='white',fontsize = 60)

    if use_engine:
        bg_fixing.draw()
        screen.draw.text("Press SPACE BAR to repair Spaceship",topleft=(10,10),fontsize=30,color='White')
        fix_game.draw()  
        if ship_hp < 100:
            screen.draw.filled_rect(Rect((345,385),(350,-ship_hp*2)),'red')
        elif ship_hp == 100:
            screen.draw.filled_rect(Rect((345,385),(350,-248)),'red')
        fix_game2.draw()

    

def hitbox_draw():
    player_hitbox.draw()
    event_engine_hitbox.draw() 
    event_problem_hitbox.draw()
    event_shoot_screen_hitbox.draw()

    for b in bg_area:
        b.draw()

''' THIS IS FOR CHECK IS PLAYER CAN USE OBJECT '''
def can_use_object():
    global can_use_shooting, can_use_engine, can_use_problem
    if player_hitbox.colliderect(event_problem_hitbox):
        can_use_problem = True
    else:
        can_use_problem = False
        
    if player_hitbox.colliderect(event_engine_hitbox):
        can_use_engine = True
    else:
        can_use_engine = False
        
    if player_hitbox.colliderect(event_shoot_screen_hitbox):
        can_use_shooting = True
    else:
        can_use_shooting = False

    

''' PLAYER CONTROL '''
def player_control():

    # player.x > 1175 and ( player.y > 490 and player.y < 620 ):
    # player.x = player.x

    # Check is playing or not
    if display == 'playing' and (use_shooting == False and use_engine == False and use_problem == False):
        if keyboard.D:
            player.x += player_speed
            player_hitbox.x += player_speed
            ''' fixed engine'''
            if player_hitbox.colliderect(engine_hitbox) or player_hitbox.x > 1245 or player_hitbox.colliderect(shoot_console_hitbox) :
                player.x -= player_speed
                player_hitbox.x -= player_speed
                
            for b in bg_area:
                if player_hitbox.colliderect(b):
                    player_hitbox.x -= player_speed
                    player.x -= player_speed
                    break
                    
        if keyboard.A:
            player.x -= player_speed
            player_hitbox.x -= player_speed
            
            if player_hitbox.colliderect(problem_hitbox) or player_hitbox.x  < 35 or player_hitbox.colliderect(shoot_console_hitbox):
                player.x += player_speed
                player_hitbox.x += player_speed
            for b in bg_area:
                if player_hitbox.colliderect(b):
                    player_hitbox.x += player_speed
                    player.x += player_speed
                    break
              
        if keyboard.S:
            player.y += player_speed
            player_hitbox.y += player_speed
            ''' fixed engine'''
            if player_hitbox.colliderect(engine_hitbox) or player_hitbox.colliderect(problem_hitbox) or player_hitbox.y > 690:
                player.y -= player_speed
                player_hitbox.y -= player_speed
               
            for b in bg_area:
                if player_hitbox.colliderect(b):
                    player_hitbox.y -= player_speed
                    player.y -= player_speed
                    break
            
        if keyboard.W:
            player.y -= player_speed
            player_hitbox.y -= player_speed
            
            ''' fixed engine'''
            if player_hitbox.colliderect(engine_hitbox) or player_hitbox.colliderect(problem_hitbox)or player_hitbox.colliderect(shoot_console_hitbox) or player_hitbox.y < 485:
                player.y += player_speed
                player_hitbox.y += player_speed
                
            for b in bg_area:
                if player_hitbox.colliderect(b):
                    player_hitbox.y += player_speed
                    player.y += player_speed
                    break     

# This is  for store player facing for animation
# 0 = left, 1 = right
player_facing = 1
player_animation_count = 0

# clock.schedule_interval(player_walking,0.25)
def player_walking_left():
    global player_facing, player_animation_count
    player_facing = 0
    player_animation_count += 1
    if player_animation_count > 4:
        player_animation_count = 1
    # Change player piture   
    player.image = player_animation[player_animation_count][0]

    
def player_walking_right():
    global player_facing, player_animation_count
    player_facing = 1
    player_animation_count += 1
    if player_animation_count > 4:
        player_animation_count = 1
    # Change player picture
    player.image = player_animation[player_animation_count][1]

def player_walking_up():
    global player_facing, player_animation_count
    player_animation_count += 1
    if player_animation_count > 4:
        player_animation_count = 1

    # Change player picture
    player.image = player_animation[player_animation_count][player_facing]

def player_walking_down():
    global player_facing, player_animation_count
    player_animation_count += 1
    if player_animation_count > 4:
        player_animation_count = 1
    # Change player picture
    player.image = player_animation[player_animation_count][player_facing]


def problem_active_loop():
    if problem_active:
        if problem_hover.image == 'bg_use2':
            problem_hover.image = 'bg_use1'
            sounds.problem.play()
            
        elif problem_hover.image == 'bg_use1':
            problem_hover.image = 'bg_use2'
        

def reset_game():
    clock.unschedule(random_event)
    clock.unschedule(problem_active_loop)
    clock.unschedule(time_count)

playbutton = Actor('playbutton_active', topleft = (530, 332))

explosion = Actor('explosion')

# This is background while playing
spacebg = Actor('spacebg')
shoot_screen_hover = Actor('shoot_screen_hover', topleft = (0,0))

player = Actor('player_right1', (639, 679))


# HITBOX
player_hitbox = Actor('player_hitbox',(player.x, player.y+20))
engine_hitbox = Actor('fixed_engine_hitbox', topleft = (1054,668))
problem_hitbox = Actor('problem_hitbox', topleft = (0,590))
shoot_console_hitbox = Actor('shoot_screen_hitbox', topleft = (590, 487))

event_engine_hitbox = Actor('event_fixed_engine_hitbox',topleft = (1045, 659))
event_problem_hitbox = Actor('event_fixed_engine_hitbox', topleft = (0,590))
event_shoot_screen_hitbox = Actor('event_shoot_screen_hitbox',topleft = (586, 487))


# LIMIT WALKING AREA 
bg_area = []
bg_area.append( Actor('bg_area_01',topleft= (822,461)))
bg_area.append( Actor('bg_area_02',topleft= (691,477)))
bg_area.append( Actor('bg_area_03',topleft= (571,456)))
bg_area.append( Actor('bg_area_04',topleft= (420,482)))
bg_area.append( Actor('bg_area_05',topleft= (392,450)))
bg_area.append( Actor('bg_area_06',topleft= (76,461)))
bg_area.append( Actor('bg_area_07',topright=(60,470)))
bg_area.append( Actor('bg_area_08',topleft= (-10,681)))
bg_area.append( Actor('bg_area_09',topleft= (81,716)))

bg_fixing = Actor('bg_fixing',topleft = (0,0))

problem_hover = Actor('bg_use1',topleft = (0,0))

gun_left = Actor('gun_left',midbottom=(90, 445))
gun_left.angle = 45
gun_right = Actor('gun_right',midbottom=(1206-20,445))
gun_right.angle = 135
crosshair = Actor('crosshair',(WIDTH/2,HEIGHT/2/2))

player_animation = []
for i in range(5):
    player_animation.append([f'player_left{i+1}', f'player_right{i+1}'])
    

pgzrun.go()




















