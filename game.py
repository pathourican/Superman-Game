# Patrick Hourican pjh4as CS1111

# Game - KRYPTONITE

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)

bg = gamebox.from_image(400,350, "https://cdn4.vectorstock.com/i/1000x1000/52/03/seamless-cartoon-city-background-with-separate-vector-20085203.jpg")
hero = gamebox.from_image(100, 300, "http://scrollboss.illmosis.net/sprites/superman-arc_superman_stand.png")
e1 = gamebox.from_image(800, random.randint(50,550), "http://scrollboss.illmosis.net/sprites/superman-arc_yellowdrone_forward.png")
e2 = gamebox.from_image(1400, random.randint(50,550), "http://scrollboss.illmosis.net/sprites/superman-arc_reddrone_forward.png")
e3 = gamebox.from_image(1800, random.randint(50,550), "http://scrollboss.illmosis.net/sprites/superman-arc_gunhunter_hover.png")
e4 = gamebox.from_image(2200, random.randint(50,550), "http://scrollboss.illmosis.net/sprites/superman-arc_thunderdrone-gray_hover.png")
coin = gamebox.from_color(800, random.randint(50, 550), "yellow", 20, 20)
dirt = gamebox.from_image(200, 560, "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
dirt2 = gamebox.from_image(600,560, "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
cloud = gamebox.from_image(100, random.randint(95,100), "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
cloud2 = gamebox.from_image(700, random.randint(95,100), "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
lasers=[]

start_screen_blank = gamebox.from_color(400, 300, "cyan", 800,600)
start_screen1 = gamebox.from_text(400,100, "KRYPTONITE - Patrick Hourican ~ pjh4as", 30, "black")
start_screen2 = gamebox.from_text(400,150, "Help Superman defend the city from the invading clones!", 30, "black")
start_screen3 = gamebox.from_text(400,200, "You have three lives available before the clones take over the city.", 30, "black")
start_screen4 = gamebox.from_text(400,250, "After every 1000 points you move on to the next level.", 30, "black")
start_screen5 = gamebox.from_text(400,300, "Collect coins to gain more lives.", 30, "black")
start_screen6 = gamebox.from_text(400, 350, "Press the UP and Down keys to move.", 30, "black")
start_screen7 = gamebox.from_text(400,400, "Press A to shoot, but you only can shoot one at a time.", 30, "black")
start_screen8 = gamebox.from_text(400,450, "Press the SPACE BAR to start!", 30, "black")

score = 0
lives = 3
level = 1
game_on = False

def reset():

    global bg
    global hero
    global e1
    global e2
    global e3
    global e4
    global coin
    global score
    global lives
    global lasers
    global level
    global dirt
    global dirt2
    global cloud
    global cloud2

    bg = gamebox.from_image(400, 350,"https://cdn4.vectorstock.com/i/1000x1000/52/03/seamless-cartoon-city-background-with-separate-vector-20085203.jpg")
    hero = gamebox.from_image(100, 300, "http://scrollboss.illmosis.net/sprites/superman-arc_superman_stand.png")
    e1 = gamebox.from_image(800, random.randint(50, 550),"http://scrollboss.illmosis.net/sprites/superman-arc_yellowdrone_forward.png")
    e2 = gamebox.from_image(1400, random.randint(50, 550),"http://scrollboss.illmosis.net/sprites/superman-arc_reddrone_forward.png")
    e3 = gamebox.from_image(1800, random.randint(50, 550),"http://scrollboss.illmosis.net/sprites/superman-arc_gunhunter_hover.png")
    e4 = gamebox.from_image(2200, random.randint(50, 550),"http://scrollboss.illmosis.net/sprites/superman-arc_thunderdrone-gray_hover.png")
    coin = gamebox.from_color(800, random.randint(50, 550), "yellow", 20, 20)
    dirt = gamebox.from_image(200, 560, "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
    dirt2 = gamebox.from_image(600, 560, "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
    cloud = gamebox.from_image(200, random.randint(95, 100),
                               "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
    cloud2 = gamebox.from_image(500, random.randint(95, 100),
                                "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")

    lasers = []

    score = 0
    lives = 3
    level = 1

def coin_grab():

    global lives

    coin.x -= 2.5

    if hero.touches(coin):
        coin.x = random.randint(800, 2000)
        coin.y = random.randint(50,550)
        lives += 1

def shoot(keys):

    global lasers

    if pygame.K_a in keys and len(lasers) < 1:
        shape = gamebox.from_color(hero.x, hero.y, "red", 20,10)
        lasers.append(shape)

    for laser in lasers:
        camera.draw(laser)
        laser.speedx = 10
        laser.move_speed()
        if laser.touches(e1) or laser.touches(e2) or laser.touches(e3) or laser.touches(e4) or laser.x >=800:
            lasers.remove(laser)
        if e1.touches(laser):
            e1.x = 800
            e1.y = random.randint(50, 550)

        if e2.touches(laser):
            e2.x = 800
            e2.y = random.randint(50,550)

        if e3.touches(laser):
            e3.x = 800
            e3.y = random.randint(50,550)

        if e4.touches(laser):
            e4.x = 800
            e4.y = random.randint(50,550)

def move_hero(keys):

    if pygame.K_UP in keys:
        hero.y -= 8

    if pygame.K_DOWN in keys:
        hero.y += 8

def move_dirt():
    global dirt
    global dirt2

    dirt.x -= 7
    dirt2.x -= 7

    if dirt.x <= 0:
        dirt.x = 800

    if dirt2.x <= 0:
        dirt2.x = 800


def move_cloud():
    global cloud
    global cloud2

    cloud.x -= 4
    cloud2.x -= 4

    if cloud.x <= 0:
        cloud.x = 800

    if cloud2.x <= 0:
        cloud2.x = 800

def move_enemies():

    global score
    global lives
    global level

    e1.x -= level + 1
    e2.x -= level + 1
    e3.x -= level + 1
    e4.x -= level + 1

    if e1.x <= 0:
        lives -= 1
        if lives > 0:
            e1.x = 800
            e1.y = random.randint(50, 550)

    if e2.x <= 0:
        lives -= 1
        if lives > 0:
            e2.x = 800
            e2.y = random.randint(50, 550)

    if e3.x <= 0:
        lives -= 1
        if lives > 0:
            e3.x = 800
            e3.y = random.randint(50, 550)

    if e4.x <= 0:
        lives -= 1
        if lives > 0:
            e4.x = 800
            e4.y = random.randint(50, 550)

    if score % 1000 == 0:
        level += 1

def highscore():

    global max_val
    input = open('game.txt', 'r')

    max_val = 0
    for num in input.readlines():
        num = num.strip()
        if int(num) > int(max_val):
            max_val = num

def tick(keys):

    global game_on
    global score
    global lives
    global max_val

    if game_on == True:
        score += 1
        display_score = gamebox.from_text(700, 25, "Score: " + str(score), 40, "white")
        display_lives = gamebox.from_text(100, 25, "Lives: " + str(lives), 40, "white")
        display_level = gamebox.from_text(400, 25, "Level: " + str(level), 40, "white")

        move_hero(keys)
        move_enemies()
        coin_grab()
        move_dirt()
        move_cloud()

        camera.draw(bg)
        camera.draw(cloud)
        camera.draw(cloud2)
        camera.draw(dirt)
        camera.draw(dirt2)
        camera.draw(e1)
        camera.draw(e2)
        camera.draw(e3)
        camera.draw(e4)
        camera.draw(hero)
        camera.draw(coin)
        camera.draw(display_score)
        camera.draw(display_lives)
        camera.draw(display_level)

        shoot(keys)
        camera.display()

    if lives <= 0:
        with open("game.txt", "a") as myfile:
            myfile.write(str(score) + '\n')
        game_on = False

    if game_on == False:

        highscore()

        high_score = gamebox.from_text(400, 550, "High Score: " + str(max_val), 40, "black")

        camera.draw(start_screen_blank)
        camera.draw(start_screen1)
        camera.draw(start_screen2)
        camera.draw(start_screen3)
        camera.draw(start_screen4)
        camera.draw(start_screen5)
        camera.draw(start_screen6)
        camera.draw(start_screen7)
        camera.draw(start_screen8)
        camera.draw(high_score)
        camera.display()
        reset()
        if pygame.K_SPACE in keys:
            game_on = True

gamebox.timer_loop(144,tick)