import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()
orange_color = (255,123,10)
green_color = (0,255,0)
black_color = (0,0,0)
blue_color = (15,15,255)
red_color = (213,50,80)
display_width = 600
display_height = 600
dis = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake game')
snake_block = 10

snake_list = []

def snake_structure(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange_color, [x[0],x[1], snake_block, snake_block])
def snake_game():
    game_over = False
    game_end = False
    snake_speed = 10
    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0
    snake_head = []
    length_of_snake = 1
    foodx = round(random.randrange(0,display_width - snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_end == True:
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 35)
            value = score_font.render("your score" + str(score),True,green_color)
            dis.blit(value,[display_width/3,display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end= False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
            if y1  < 0 or x1 < 0 or   y1 > display_height or x1  > display_width:
                game_end = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black_color)
        pygame.draw.rect(dis,green_color,(foodx,foody,snake_block,snake_block))
        snake_head =  []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[0:-1]:
            if x == snake_head:
                game_end = False
        snake_structure(snake_block,snake_list)
        pygame.display.update()
        
        if x1 == foodx  and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake +=1
            snake_speed = snake_speed + 5
            
            
            
            
        clock.tick(snake_speed)
        print(snake_speed)
    pygame.quit()
    quit()
snake_game()
