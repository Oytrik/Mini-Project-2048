import pygame
pygame.init()
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
    	pygame.draw.line(screen, (0, 0, 255), (200,100*(i+1) ), (600, 100*(i+1)))
    	pygame.draw.aaline(screen, (0, 0, 255), (200+100*i,100 ), (200+100*i,500 ))       
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
