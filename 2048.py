import pygame
import random
a=m=n=x=y=inx1=iny1=X=Y=inx2=iny2=0
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
A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def initial():    
    a=[2,4]
    m=random.choice(a)
    n=random.choice(a)
    print (m,n)
    x=[200,300,400,500]
    y=[100,200,300,400]
    inx1=random.choice(x)
    iny1=random.choice(y)
    inx2=random.choice(x)
    iny2=random.choice(y)    
    if inx1 == 200:
        X=0
    if inx1 == 300:
        X=1
    if inx1 == 400:
        X=2
    if inx1 == 500:
        X=3
    if iny1 == 100:
        Y=0
    if iny1 == 200:
        Y=1
    if iny1 == 300:
        Y=2
    if iny1 == 400:
        Y=3
    A[X][Y]=m
    if inx2 == 200:
        X=0
    if inx2 == 300:
        X=1
    if inx2 == 400:
        X=2
    if inx2 == 500:
        X=3
    if iny2 == 100:
        Y=0
    if iny2 == 200:
        Y=1
    if iny2 == 300:
        Y=2
    if iny2 == 400:
        Y=3
    A[X][Y]=n
def draw():
    for i in range (0,4):
        for j in range (0,4):
            if not A[i][j] == 0:
                textsurface = myfont.render(str(A[i][j]), False, WHITE)
                screen.blit(textsurface,((j*100)+200+35,(i+1)*100+35))   
initial()
print (A)        
quit = False
while not quit:
    screen.fill((50, 50, 50))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True 
        print (event)    
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
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                initial()
    else:	
        pygame.draw.rect(screen,RED,(50,200,125,50))   
    textsurface = myfont.render('RESET', False, WHITE)
    screen.blit(textsurface,(55,210))  
    draw()
    pygame.display.update()
    clock.tick(60)
score=0
hscore=0    
pygame.quit()

