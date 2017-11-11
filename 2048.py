import pygame
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('2048') 
clock = pygame.time.Clock()
quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True 
    screen.fill((0, 0, 0))
    for i in range (0,5):
    	pygame.draw.line(screen, BLUE, (200,100*(i+1) ), (600, 100*(i+1)))
    	pygame.draw.line(screen, BLUE, (200+100*i,100 ), (200+100*i,500 ))     
        
    textsurface = myfont.render('2048', False, WHITE)
    screen.blit(textsurface,(50,50))           
    textsurface = myfont.render('Score', False, GREEN)
    screen.blit(textsurface,(660,50))       
    textsurface = myfont.render('HighScore', False, RED)
    screen.blit(textsurface,(630,150))
    mouse=pygame.mouse.get_pos()
    if mouse[0]<175 and mouse[0]>50 and mouse[1]<250 and mouse[1]>200:
    	pygame.draw.rect(screen, GREEN,(50,200,125,50))
    else:	
    	pygame.draw.rect(screen, RED,(50,200,125,50))
    textsurface = myfont.render('RESET', False, WHITE)
    screen.blit(textsurface,(55,210))  
    pygame.display.update()
    clock.tick(60)
def initial ():
    a=[2,4]
    m=random.choice(a)
    n=random.choice(a)
    x=[200,300,400,500]
    y=[100,200,300,400]
    inx=random.choice(x)
    iny=random.choice(y)
pygame.quit()

