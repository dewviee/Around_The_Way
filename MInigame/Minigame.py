import pgzrun
from random import randint
WIDTH = 1280
HEIGHT = 720
fix_game = Actor('fix_engine_screen')
fix_game2 = Actor('fix_engine_screen_layer2')
hp = 0
fixing_sound = False
def draw():
    screen.draw.text("Press SPACE BAR to repair Spaceship",topleft=(10,10),fontsize=30,color='White')
    fix_game.draw()  
    if hp < 100:
        screen.draw.filled_rect(Rect((345,385),(350,-hp*2)),'red')
    elif hp == 100:
        screen.draw.filled_rect(Rect((345,385),(350,-248)),'red')
    fix_game2.draw()
def on_key_down(key,mod,unicode):
    global hp, fixing_sound
    if key == keys.SPACE:
        hp += randint(1,5)
    if hp > 100:
        hp = 100

    
    if fixing_sound == False:
        fixing_sound = True
        sounds.fixing_engine.play()
        if hp == 100:
            sounds.fixing_engine.stop()
        clock.schedule(fixing_sound_delay,4)
        
def fixing_sound_delay():
    global fixing_sound
    fixing_sound = False

    
pgzrun.go()
