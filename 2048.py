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
hscore=0
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
    global hscore,points
    for i in range (0,4):
        for j in range (0,4):
            if not A[i][j] == 0:
                textsurface = myfont.render(str(A[i][j]), False, WHITE)
                screen.blit(textsurface,((j*100)+200+35,(i+1)*100+35))
    textsurface = myfont.render(str(points), False, WHITE)
    screen.blit(textsurface,(680,100))
    textsurface = myfont.render(str(hscore), False, WHITE)
    screen.blit(textsurface,(680,200))
def right():
    global points,hscore		
    for r in range(0,4):            
            for c in range(0,3):
                if(A[r][c]!=0 and A[r][c+1]==0):
                    A[r][c+1]=A[r][c]
                    A[r][c]=0
                    for i in reversed(range(1,c+1)):
                        A[r][i]=A[r][i-1]
                        A[r][i-1]=0               
            for c in reversed(range(1,4)):
                if(A[r][c]!=0 and A[r][c]==A[r][c-1]):
                    A[r][c]=A[r][c]*2
                    points=points+A[r][c]
                    A[r][c-1]=0
                    for k in reversed(range(0,c)):
                        for i in reversed(range(1,k+1)):
                            A[r][i]=A[r][i-1]
                            A[r][i-1]=0                    
                 
    if hscore<points:
        hscore=points
    add()
def left():
    global points,hscore
    for r in range(0,4):
            for c in reversed(range(1,4)):
                if(A[r][c]!=0 and A[r][c-1]==0):
                    A[r][c-1]=A[r][c]
                    A[r][c]=0
                    for i in range(c,3):
                        A[r][i]=A[r][i+1]
                        A[r][i+1]=0
                
               
            for c in range(0,3):
                if(A[r][c]!=0 and A[r][c]==A[r][c+1]):
                    A[r][c]=A[r][c]*2
                    points=points+A[r][c]
                    A[r][c+1]=0
                    for k in range(c+1,4):
                        for i in range(k,3):
                            A[r][i]=A[r][i+1]
                            A[r][i+1]=0
            
    if hscore<points:
        hscore=points
    add()             
def up():
    global points,hscore
    for c in range(0,4):
            for r in reversed(range(1,4)):
                if(A[r][c]!=0 and A[r-1][c]==0):
                    A[r-1][c]=A[r][c]
                    A[r][c]=0
                    for i in range(r,3):
                        A[i][c]=A[i+1][c]
                        A[i+1][c]=0  
                          
                    
            for r in range(0,3):
                if(A[r][c]!=0 and A[r][c]==A[r+1][c]):
                    A[r][c]=A[r][c]*2
                    A[r+1][c]=0
                    points=points+A[r][c]
                    for k in range(r+1,4):
                        for i in range(k,3):
                            A[i][c]=A[i+1][c]
                            A[i+1][c]=0                
    if hscore<points:
        hscore=points
    add()
def down():
    global points,hscore
    for c in range(0,4):
            for r in range(0,3):
                if(A[r][c]!=0 and A[r+1][c]==0):
                    A[r+1][c]=A[r][c]
                    A[r][c]=0
                    for i in reversed(range(1,r+1)):
                        A[i][c]=A[i-1][c]
                        A[i-1][c]=0
                
               
            for r in reversed(range(1,4)):
                if(A[r][c]!=0 and A[r-1][c]==A[r][c]):
                    A[r][c]=A[r][c]*2
                    A[r-1][c]=0
                    points=points+A[r][c]
                    for k in reversed(range(0,r)):
                        for i in reversed(range(1,k+1)):
                            A[i][c]=A[i-1][c]
                            A[i-1][c]=0
                
    if hscore<points:
        hscore=points
    add()
def add():
    a=[2,4]
    m=random.choice(a)
    while 1:
        i=int(random.uniform(0,4))
        j=int(random.uniform(0,4))
        if(A[i][j]==0):
            A[i][j]=m
            break
        
def reset():
    for i in range (0,4):
        for j in range (0,4):
            A[i][j]=0
    initial()
initial()
print (A)
quit = False
while not quit:
    screen.fill((50, 50, 50))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True 
        
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                right()
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                left()
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                up()               
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                down()                                 
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
    click=pygame.mouse.get_pressed()
    if mouse[0]<175 and mouse[0]>50 and mouse[1]<250 and mouse[1]>200:
        pygame.draw.rect(screen, GREEN,(50,200,125,50))
        if click[0]==1:
            reset()            
    else:	
        pygame.draw.rect(screen,RED,(50,200,125,50))   
    textsurface = myfont.render('RESET', False, WHITE)
    screen.blit(textsurface,(55,210))  
    draw()
     
    pygame.display.update()
    clock.tick(60) 
pygame.quit()

