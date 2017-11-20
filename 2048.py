#Importing required modules
import pygame
import random

#Initializing pygame modules
pygame.init()

#Initializing font module
pygame.font.init()

#Creating fonts 
myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont_win=pygame.font.SysFont('Times New Roman', 80)

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
GOLD=( 230, 215, 0)


screen = pygame.display.set_mode((800,600)) #Initialzing a screen for display
pygame.display.set_caption('2048') 
clock = pygame.time.Clock() 

#Lists to store game matrices
A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
A1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Initializing variables
points=0
uscore=0
c=0

try:
    a=open("highscore.txt","r")#Opening file    
    x=a.readlines()#Reading file
    hscore=int(x[0])#Storing high score
    a.close()#Closing file

except:
    hscore=0 

#Initialzing variables
w=x=y=z=1

#To set initial state of game matrix and score.
def initial(): 

    #Initializing variables   
    a=[2,2,2,4]
    global points,hscore,uscore
    uscore=0
    points=0

    #Choosing elements from list a at random
    m=random.choice(a)
    n=random.choice(a)    

    x=[0,1,2,3]
    y=[0,1,2,3]

    #Choosing elements from lists x and y at random
    #To be used as coordinates
    inx1=random.choice(x)
    iny1=random.choice(y)
    inx2=random.choice(x)
    iny2=random.choice(y)   

    while inx1==inx2 and iny1==iny2:
    #Ensuring no two x and y coordinates are the same
        inx1=random.choice(x)
        inx2=random.choice(x)
        iny1=random.choice(y)
        iny2=random.choice(y)   

    #Setting initial elements of matrix at random
    A[inx1][iny1]=m    
    A[inx2][iny2]=n    

#To draw the game matrix, scores and required buttons
def draw():
    mouse=pygame.mouse.get_pos()#To get the mouse cursor position    
    click=pygame.mouse.get_pressed()#To get the state of the mouse buttons
    screen.fill((50, 50, 50)) #Fill screen to grey
    #Drawing the game matrix
    for i in range (0,5):
    	pygame.draw.line(screen, BLUE, (200,100*(i+1) ), (600, 100*(i+1)))
    	pygame.draw.line(screen, BLUE, (200+100*i,100 ), (200+100*i,500 ))          

    #Displaying the name of game, 'Score' and 'High Score'
    textsurface = myfont.render('2048', False, WHITE)
    screen.blit(textsurface,(50,50))           

    textsurface = myfont.render('Score', False, GREEN)
    screen.blit(textsurface,(660,50))            

    textsurface = myfont.render('HighScore', False, RED)
    screen.blit(textsurface,(630,150)) 

    
    if mouse[0]<175 and mouse[0]>50 and mouse[1]<250 and mouse[1]>200:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(50,200,125,50))#Change button colour to green
        if click[0]==1: #If button is clicked
            reset() # Reset the matrix by calling reset() function
            
    else:#Display colour of button as red	
        pygame.draw.rect(screen,RED,(50,200,125,50))   

    #Display 'RESET' on the button
    textsurface = myfont.render('RESET', False, WHITE)
    screen.blit(textsurface,(55,210))
 
   
    if mouse[0]<175 and mouse[0]>50 and mouse[1]<350 and mouse[1]>300:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(50,300,125,50)) #Change button colour to green
        if click[0]==1:#If button is clicked
            undo() #Undo the prevoius move by calling undo() function

    else:#Display colour of button as blue.	
        pygame.draw.rect(screen,BLUE,(50,300,125,50))   

    #Display 'UNDO' on the button
    textsurface = myfont.render('UNDO', False, WHITE)
    screen.blit(textsurface,(60,310))    

    global hscore,points

    for i in range (0,4):
        for j in range (0,4):

            if not A[i][j] == 0:
                if A[i][j]<1000:
                    textsurface = myfont.render(str(A[i][j]), False, WHITE)
                    screen.blit(textsurface,((j*100)+200+35,(i+1)*100+35))

                else:
                    textsurface = myfont.render(str(A[i][j]), False, WHITE)
                    screen.blit(textsurface,((j*100)+200+15,(i+1)*100+35))

    #Displaying score
    textsurface = myfont.render(str(points), False, WHITE)
    screen.blit(textsurface,(680,100))

    #Displaying high score
    textsurface = myfont.render(str(hscore), False, WHITE)
    screen.blit(textsurface,(680,200))

    a=open("highscore.txt","w")#Opening file    
    a.writelines(str(hscore))#Writing high score to file
    a.close()#Closing file    

    #Initialzing variable
    m=n=o=0      

    #If two adjacent horizontal elements are equal
    for i in range(0,4):
        for j in range(0,3):
            if A[i][j]==A[i][j+1]:
                m=1

    #If two adjacent vertical elements are equal
    for i in range(0,4):
        for j in range(0,3):
            if A[j][i]==A[j+1][i]:
                n=1

    #If game matrix is empty (game has just started)
    for i in range(0,4):
        for j in range(0,4):
            if A[i][j]==0:
                o=1                   

    if m==0 and n==0 and o==0:#If no adjacent elements are equal nor has game just started
                              #That is, there are no further moves
  
        #Display "Game Over!!!' on screen
        textsurface = myfont.render("Game Over !!!", False, RED)
        screen.blit(textsurface,(300,50)) 

#To undo the previous move
def undo():

    global A,points,uscore
    points=uscore #Restoring the score to the prevoius score
    A=[[i for i in x] for x in A1] #Restoring game matrix to its state one move prior

#To move elements of game matrix right when right arrow is clicked
def right():
    #Initialzing variables	
    global w,points,hscore,uscore
    w=0
    uscore=points		

    for i in range (0,4):
        for j in range (0,4):

            if A[i][j] != 0:
                for k in range(j+1,4):
                    if A[i][k] == 0:
                        w=1
                        break

                    else:
                        try:
                            if A[i][j] == A[i][j+1]:
                                w=1
                                break
                        except:
                            w=0    

    if w==1:
        global A1
        A1=[[i for i in x] for x in A]

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
                                if A[r][i]==0:
                                    A[r][i]=A[r][i-1]
                                    A[r][i-1]=0                    
 
        if hscore<points:
            hscore=points

        add()

def left():
    
    global x,points,hscore,uscore
    x=0
    uscore=points		

    for i in range (0,4):
        for j in range (0,4):
            if A[i][j] != 0:
                for k in range(0,j):
                    if A[i][k] == 0:
                        x=1
                        break

                    else:
                        try:
                            if A[i][j] == A[i][j-1]:
                                x=1
                                break
                        except:
                            x=0   

    if x==1:
        global A1 
        A1=[[i for i in x] for x in A]
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
                                if A[r][i]==0:
                                    A[r][i]=A[r][i+1]
                                    A[r][i+1]=0
 
        if hscore<points:
            hscore=points

        add()             

def up():
        
    global y,points,hscore,uscore
    y=0
    uscore=points		

    for i in range (0,4):
        for j in range (0,4):
            if A[j][i] != 0:
                for k in range(0,j):
                    if A[k][i] == 0:
                        y=1
                        break

                    else:
                        try:
                            if A[j][i] == A[j-1][i]:
                                y=1
                                break
                        except:
                            y=0        

    if y==1:
        global A1
        A1=[[i for i in x] for x in A]

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
                                if A[i][c]==0:
                                    A[i][c]=A[i+1][c]
                                    A[i+1][c]=0                

        if hscore<points:
            hscore=points        

        add()

def down():
    
    global z,points,hscore,uscore
    z=0
    uscore=points		

    for i in range (0,4):
        for j in range (0,4):
            if A[j][i] != 0:
                for k in range(j+1,4):
                    if A[k][i] == 0:
                        z=1
                        break

                    else:
                        try:
                            if A[j][i] == A[j+1][i]:
                                z=1
                                break
                        except:
                            z=0    

    if z==1:
        global A1
        A1=[[i for i in x] for x in A]

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
                                if A[i][c]==0:
                                    A[i][c]=A[i-1][c]
                                    A[i-1][c]=0
 
        if hscore<points:
            hscore=points

        add()

def add():
    a=[2,2,2,4]
    m=random.choice(a)

    while 1:
        i=int(random.uniform(0,4))
        j=int(random.uniform(0,4))

        if(A[i][j]==0):
            A[i][j]=m
            break    

#To reset the game matrix to initial state 
def reset():
    
    #Setting all game matrix elements back to zero
    for i in range (0,4):
        for j in range (0,4):
            A[i][j]=0

    initial()#Calling initial() function to restart the game

#To display a welcome message at the start of the game
def welcome_message():
    global quit, d

    mouse=pygame.mouse.get_pos()#To get the mouse cursor position    
    click=pygame.mouse.get_pressed()#To get the state of the mouse buttons  
    
    #Fill the screen black
    screen.fill(BLACK)
    
    #Display '2048'
    textsurface=myfont_win.render('2048', False, GOLD)
    screen.blit(textsurface, (300, 200))    
    
 
    if mouse[0]<450 and mouse[0]>330 and mouse[1]<450 and mouse[1]>400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(310,400,130,50))#Change button colour to green 
        if click[0]==1:#If button is clicked 
           d+=1
           draw() #Draw the game matrix, thereby startng the game
 
    else:#Display colour of button as blue	
        pygame.draw.rect(screen,BLUE,(310,400,130,50))

    #Display 'PLAY' on the button
    textsurface = myfont.render('PLAY', False, WHITE)
    screen.blit(textsurface,(330,410)) 

#To display a victory message when 2048 is achieved 
def win_message():
    global quit, c

    mouse=pygame.mouse.get_pos()#To get the mouse cursor position    
    click=pygame.mouse.get_pressed()#To get the state of the mouse buttons      

    #Fill the screen to black
    screen.fill(BLACK)

    #Display 'You won!' on screen
    textsurface=myfont_win.render('You Won!', False, GOLD)
    screen.blit(textsurface, (250, 200))    

    if mouse[0]<375 and mouse[0]>200 and mouse[1]<450 and mouse[1]>400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(200, 400,125,50))#Change button colour to green 
        if click[0]==1:#If button is clicked 
            quit=True #Change quit to true, thereby quitting the game
 
    else:#Display colour of button as red	
        pygame.draw.rect(screen,RED,(200,400,125,50))   

    #Display 'QUIT' on the button
    textsurface = myfont.render('QUIT', False, WHITE)
    screen.blit(textsurface,(220,410))
 
    if mouse[0]<650 and mouse[0]>430 and mouse[1]<450 and mouse[1]>400:#If mouse hovers over button
        pygame.draw.rect(screen, GREEN,(410,400,220,50))#Change button colour to green  
        if click[0]==1:#If button is clicked 
           c=1
           draw()#Draw the game matrix, therby continuing the game
 
    else:#Display colour of button as blue	
        pygame.draw.rect(screen,BLUE,(410,400,220,50))   

    #Display 'CONTINUE' on the button
    textsurface = myfont.render('CONTINUE', False, WHITE)
    screen.blit(textsurface,(430,410)) 

initial() #Calling initial() function, thereby beginning the game
#Dispaying welcome message

quit = False #Initialzing variable  
d=0
while not quit: #While game is running
    global c,d

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#If user quits game
            quit = True
 
        if event.type ==pygame.KEYDOWN:           
            if event.key==pygame.K_RIGHT:#If user presses right arrow key
                right()

        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:#If user presses left arrow key
                left()

        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_UP:#If user presses up arrow key
                up()               

        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:#If user presses down arrow key
                down()
  
    if d==0:
        welcome_message()
    if d>0:
        draw() #Draw game matrix
    #If user achieves 2048
    if c==0:         
        for i in range(0,4):
            for j in range(0,4):

                if A[i][j]==2048: #Checking if any element in game matrix is equal to 2048               
                    win_message()#Displaying victory message by calling win_message() function                   

    pygame.display.update() #Update portions of the screen for software displays  

pygame.quit() #Uninitialize all pygame modules
