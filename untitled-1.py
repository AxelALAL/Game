import pygame
import random
import time
import sys

load_image = pygame.image.load
chan = pygame.transform.scale

                          
if __name__ == '__main__': 
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode((size), 0, 32)
    pygame.display.flip()
    laser = chan(load_image('laser.png'), (4, 8))
    colorkey = laser.get_at((0, 0))
    laser.set_colorkey(colorkey)
    wall = chan(load_image('wall.png'), (20, 20))
    walls = []
    score = 0
    #загрузка всех картинок
    background1 = chan(load_image('background1.jpg'), (800, 450))
    planet1 = chan(load_image('planet1.png'), (30, 30))
    planet2 = chan(load_image('planet2.png'), (30, 30))
    planet3 = chan(load_image('planet3.png'), (30, 30))
    ufo1 = chan(load_image('ufo1.png'), (30, 30))
    ufo2 = chan(load_image('ufo2.png'), (30, 30))
    ufo3 = chan(load_image('ufo3.png'), (30, 30))
    asteroid1 = chan(load_image('asteroid1.jpg'), (30, 30))
    asteroid2 = chan(load_image('asteroid2.jpg'), (30, 30))
    asteroid3 = chan(load_image('asteroid3.jpg'), (30, 30))
    asteroid1.set_colorkey(-1)
    asteroid2.set_colorkey(-1)
    asteroid3.set_colorkey(-1)
    fire1 = chan(load_image('fire1.png'), (20, 20))
    fire2 = chan(load_image('fire2.png'), (20, 20))
    fire3 = chan(load_image('fire3.png'), (20, 20))
    fire4 = chan(load_image('fire4.png'), (20, 20))
    fire5 = chan(load_image('fire5.png'), (20, 20))
    gameover = chan(load_image('gameover.jpg'), (600, 400))
    enemy = [planet1, planet2, planet3, ufo1, ufo2, ufo3, 
             asteroid1, asteroid2, asteroid3]
    fires = [fire1, fire2, fire3, fire4, fire5]
    ship = load_image('ship.png')
    space = load_image('space2.jpg')
    space = chan(space, (200, 200))
    ship = chan(ship, (50, 50))
    expl = pygame.mixer.music.load('expl.mp3')
    text = 0
    x_pos = 400
    y_pos1 = 0
    scores = [0]
    en_y = 0
    v = 900 
    acc = 1
    fps = 120
    clock = pygame.time.Clock()
    sec = 0  
    tm = 0
    gates_x = 0
    gates_y = -600
    gates1 = chan(load_image('gates1.jpg'), (800, 600))    
    starting = True
    bullets = []
    enemies = []
    
    #функции для перехода между окнами, стрельбой и тд
    def game_over():
        global text 
        text = 0
        global score
        scores.append(score)
        score = 0
        global x_pos
        global y_pos1
        x_pos = 400
        y_pos1 = 0        
        global bullets
        global walls
        global enemies
        bullets = []
        walls = []
        enemies = []
        global running
        gates_y = -1800
        global gameover
        global gates_1
        screen.blit(gameover, (100, 100))
        running = False
        closing = True
        while closing:
            screen.blit(gates1, (gates_x, gates_y))
            gates_y += 5
            clock.tick(fps)
            pygame.display.flip()
            if gates_y == 0:
                closing = False
        
        global space
        global fires
        global ship
        global engine_fire
        global tm
        while gates_y != -600:
            engine_fire = random.choice(fires)
            screen.fill((0, 0, 0))
            screen.blit(space, (0, y_pos1 - 199))
            screen.blit(space, (0, y_pos1))
            screen.blit(space, (0, y_pos1 + 199))
            screen.blit(space, (0, y_pos1 - 398))
            screen.blit(space, (0, y_pos1 + 398))
            screen.blit(space, (200, y_pos1 - 199))
            screen.blit(space, (200, y_pos1))
            screen.blit(space, (200, y_pos1 + 199))
            screen.blit(space, (200, y_pos1 - 398))
            screen.blit(space, (200, y_pos1 + 398))
            screen.blit(space, (400, y_pos1 - 199))
            screen.blit(space, (400, y_pos1))
            screen.blit(space, (400, y_pos1 + 199))
            screen.blit(space, (400, y_pos1 - 398))
            screen.blit(space, (400, y_pos1 + 398))
            screen.blit(space, (600, y_pos1 - 199))
            screen.blit(space, (600, y_pos1))
            screen.blit(space, (600, y_pos1 + 199))
            screen.blit(space, (600, y_pos1 - 398))
            screen.blit(space, (600, y_pos1 + 398))
            screen.blit(ship, (x_pos - 25, 510))
            screen.blit(engine_fire, (x_pos - 10, 560))         
            screen.blit(gates1, (gates_x, gates_y))
            gates_y -= 5
            clock.tick(fps)
            pygame.display.flip()
            
        running = True
        while running:
            tm += 1
            engine_fire = random.choice(fires)
            screen.fill((0, 0, 0))
            screen.blit(space, (0, y_pos1 - 199))
            screen.blit(space, (0, y_pos1))
            screen.blit(space, (0, y_pos1 + 199))
            screen.blit(space, (0, y_pos1 - 398))
            screen.blit(space, (0, y_pos1 + 398))
            screen.blit(space, (200, y_pos1 - 199))
            screen.blit(space, (200, y_pos1))
            screen.blit(space, (200, y_pos1 + 199))
            screen.blit(space, (200, y_pos1 - 398))
            screen.blit(space, (200, y_pos1 + 398))
            screen.blit(space, (400, y_pos1 - 199))
            screen.blit(space, (400, y_pos1))
            screen.blit(space, (400, y_pos1 + 199))
            screen.blit(space, (400, y_pos1 - 398))
            screen.blit(space, (400, y_pos1 + 398))
            screen.blit(space, (600, y_pos1 - 199))
            screen.blit(space, (600, y_pos1))
            screen.blit(space, (600, y_pos1 + 199))
            screen.blit(space, (600, y_pos1 - 398))
            screen.blit(space, (600, y_pos1 + 398))
            screen.blit(ship, (x_pos - 25, 510))
            screen.blit(engine_fire, (x_pos - 10, 560))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if x_pos > 46:
                    x_pos -= 2
            if keys[pygame.K_RIGHT]:
                if x_pos < 754:
                    x_pos += 2
            if keys[pygame.K_SPACE]:
                if tm > 50:
                    bullets.append([x_pos - 2, y_pos1 + 360])
                    tm = 0
            if keys[pygame.K_ESCAPE]:
                terminate()
            if int(y_pos1) > 199:
                y_pos1 = 0        
            y_pos1 += v * clock.tick() / 1200
            check_hit() 
            update_bullets()
            update_enemies()    
            create_enemy()
            create_wall()
            check_collision()
            score_text = 'score:' + str(score)
            highest_score_text = 'highest score:' + str(max(scores))
            string_r1 = font.render(score_text, 1, pygame.Color('white'))
            screen.blit(string_r1, (10, 30))
            str_r2 = font.render(highest_score_text, 1, pygame.Color('white'))
            screen.blit(str_r2, (10, 10))             
            clock.tick(fps)
            pygame.display.flip()
        pygame.quit()        
    
    def create_enemy():
        if len(enemies) < 10:
            typ = random.choice(enemy)
            coors = [random.randrange(55, 880, 165), random.randrange(-200, 0)]
            enemies.append([typ, coors])
        
    def create_wall():
        if len(walls) < 1:
            skip = random.randrange(3, 42)
            for i in range(skip - 2):
                coors = [18 * i, -150]
                walls.append([wall, coors])
            for i in range(skip + 3, 45):
                coors = [18 * i, -150]
                walls.append([wall, coors])                
    
    def check_collision():
        for i in enemies:
            a1 = int(x_pos) - int(i[1][0])
            b1 = 510 - int(i[1][1])
            if a1 > -25 and a1 < 55 and b1 > -40 and b1 < 10:
                game_over()
        for i in walls:
            a1 = int(x_pos) - int(i[1][0])
            b1 = 510 - int(i[1][1])            
            if a1 > -25 and a1 < 45 and b1 > -20 and b1 < 10:
                game_over()            
                    
    def check_hit():
        global expl
        for i in bullets:
            for j in enemies:
                a1 = int(i[1]) - int(j[1][1])
                if a1 < 5 and a1 > -5:
                    b1 = int(i[0]) - int(j[1][0])
                    if b1 > 0 and b1 < 30:
                        global score
                        score += 10
                        if j in enemies:    
                            enemies.remove(j)
                        if i in bullets:
                            bullets.remove(i)
                        pygame.mixer.music.play(1)
        for i in enemies:
            for j in enemies:
                a1 = int(i[1][1]) - int(j[1][1])
                if a1 < 30 and a1 > -30:
                    b1 = int(i[1][0]) - int(j[1][0])
                    if b1 > -30 and b1 < 30:
                        if j in enemies:    
                            if i != j:
                                enemies.remove(j)
        for i in enemies:
            for j in walls:
                a1 = int(i[1][1]) - int(j[1][1])
                if a1 < 20 and a1 > -30:
                    b1 = int(i[1][0]) - int(j[1][0])
                    if b1 > -30 and b1 < 30:
                        if i in enemies:    
                            enemies.remove(i)
        for i in bullets:
            for j in walls:
                a1 = int(i[1]) - int(j[1][1])
                if a1 < 5 and a1 > -5:
                    b1 = int(i[0]) - int(j[1][0])
                    if b1 > -10 and b1 < 20:
                        if i in bullets:    
                            bullets.remove(i)

    def update_enemies():
        for i in enemies:
            i[1][1] += 1
            screen.blit(i[0], i[1])
            if i[1][1] > 600:
                enemies.remove(i)
        for i in walls:
            i[1][1] += 1
            screen.blit(i[0], i[1])
            if i[1][1] > 1000:
                walls.remove(i)            
    
    def update_bullets():
        for i in bullets:
            i[1] -= 5
            screen.blit(laser, i)
            if i[1] < 0:
                bullets.remove(i)
                
    #выход из игры
    def terminate():
        pygame.quit()
        sys.exit()    
    i = 0
    t = 0
    while starting:
        sec += 1
        m = ["                                                  SPACE SHOOTER"]
        intro_text = m
        if t == 0:
            fon = chan(load_image('background1.jpg'), (width, height - 150))
            t = 1
            screen.blit(fon, (0, 150))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('blue'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        if sec > 60:
            p_c = pygame.Color
            if i == 0:
                s = font.render("Press SPACE to start", 1, p_c('blue'))
                screen.blit(s, (300, 500))
                i = 1
            elif i == 1:
                s = font.render("Press SPACE to start", 1, p_c('black'))
                screen.blit(s, (300, 500)) 
                i = 0
            sec = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    closing = True
                    starting = False
        pygame.display.flip()
        clock.tick(fps)  
    
    while closing:
        screen.blit(gates1, (gates_x, gates_y))
        gates_y += 5
        clock.tick(fps)
        pygame.display.flip()
        if gates_y == 0:
            closing = False
    
    while gates_y != -600:
        engine_fire = random.choice(fires)
        screen.fill((0, 0, 0))
        screen.blit(space, (0, y_pos1 - 199))
        screen.blit(space, (0, y_pos1))
        screen.blit(space, (0, y_pos1 + 199))
        screen.blit(space, (0, y_pos1 - 398))
        screen.blit(space, (0, y_pos1 + 398))
        screen.blit(space, (200, y_pos1 - 199))
        screen.blit(space, (200, y_pos1))
        screen.blit(space, (200, y_pos1 + 199))
        screen.blit(space, (200, y_pos1 - 398))
        screen.blit(space, (200, y_pos1 + 398))
        screen.blit(space, (400, y_pos1 - 199))
        screen.blit(space, (400, y_pos1))
        screen.blit(space, (400, y_pos1 + 199))
        screen.blit(space, (400, y_pos1 - 398))
        screen.blit(space, (400, y_pos1 + 398))
        screen.blit(space, (600, y_pos1 - 199))
        screen.blit(space, (600, y_pos1))
        screen.blit(space, (600, y_pos1 + 199))
        screen.blit(space, (600, y_pos1 - 398))
        screen.blit(space, (600, y_pos1 + 398))
        screen.blit(ship, (x_pos - 25, 510))
        screen.blit(engine_fire, (x_pos - 10, 560))         
        screen.blit(gates1, (gates_x, gates_y))
        gates_y -= 5
        clock.tick(fps)
        pygame.display.flip()
        
    running = True
    while running:
        tm += 1
        engine_fire = random.choice(fires)
        screen.fill((0, 0, 0))
        screen.blit(space, (0, y_pos1 - 199))
        screen.blit(space, (0, y_pos1))
        screen.blit(space, (0, y_pos1 + 199))
        screen.blit(space, (0, y_pos1 - 398))
        screen.blit(space, (0, y_pos1 + 398))
        screen.blit(space, (200, y_pos1 - 199))
        screen.blit(space, (200, y_pos1))
        screen.blit(space, (200, y_pos1 + 199))
        screen.blit(space, (200, y_pos1 - 398))
        screen.blit(space, (200, y_pos1 + 398))
        screen.blit(space, (400, y_pos1 - 199))
        screen.blit(space, (400, y_pos1))
        screen.blit(space, (400, y_pos1 + 199))
        screen.blit(space, (400, y_pos1 - 398))
        screen.blit(space, (400, y_pos1 + 398))
        screen.blit(space, (600, y_pos1 - 199))
        screen.blit(space, (600, y_pos1))
        screen.blit(space, (600, y_pos1 + 199))
        screen.blit(space, (600, y_pos1 - 398))
        screen.blit(space, (600, y_pos1 + 398))
        screen.blit(ship, (x_pos - 25, 510))
        screen.blit(engine_fire, (x_pos - 10, 560))               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x_pos > 46:
                x_pos -= 2
        if keys[pygame.K_RIGHT]:
            if x_pos < 754:
                x_pos += 2
        if keys[pygame.K_SPACE]:
            if tm > 50:
                bullets.append([x_pos - 2, y_pos1 + 360])
                tm = 0
        if keys[pygame.K_ESCAPE]:
                terminate()
                
        if int(y_pos1) > 199:
            y_pos1 = 0        
        y_pos1 += v * clock.tick() / 1200
        check_hit() 
        update_bullets()
        update_enemies()    
        create_enemy()
        create_wall()
        check_collision()
        score_text = 'score:' + str(score)
        highest_score_text = 'highest score:' + str(max(scores))
        string_r1 = font.render(score_text, 1, pygame.Color('white'))
        screen.blit(string_r1, (10, 30))
        str_r2 = font.render(highest_score_text, 1, pygame.Color('white'))
        screen.blit(str_r2, (10, 10))         
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
