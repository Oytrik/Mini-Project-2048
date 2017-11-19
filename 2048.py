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
A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
points=0
def initial():    
    a=[2,2,2,4]
    global points,hscore
    points=0
    m=random.choice(a)
    n=random.choice(a)
    print (m,n)
    x=[0,1,2,3]
    y=[0,1,2,3]
    inx1=random.choice(x)
    iny1=random.choice(y)
    inx2=random.choice(x)
    iny2=random.choice(y)   
    while inx1==inx2 and iny1==iny2:
        inx1=random.choice(x)
        inx2=random.choice(x)
        iny1=random.choice(y)
        iny2=random.choice(y)   
    A[inx1][iny1]=m    
    A[inx2][iny2]=n
    print (A)
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
