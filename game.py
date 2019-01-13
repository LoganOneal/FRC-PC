import pygame
from networktables import NetworkTables

pygame.init()

NetworkTables.initialize(server='10.39.66.2')
smartdashboard = NetworkTables.getTable('SmartDashboard')
window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("FRC PC MASTER RACE")
 
black = (0,0,0)
white=(255,255,255)
 
x,y=0,0
 
moveX,moveY=0,0
 
clock = pygame.time.Clock()
 
gameLoop=True
while gameLoop:
    pygame.time.delay(20)
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT or event.key == ord('a')):
                smartdashboard.putBoolean('A', True)
                moveX = -5

            if (event.key==pygame.K_RIGHT or event.key == ord('d')):
                smartdashboard.putBoolean('D', True)
                moveX = 5

            if (event.key==pygame.K_UP or event.key == ord('w')):
                smartdashboard.putBoolean('W', True)
                moveY = -5

            if (event.key==pygame.K_DOWN or event.key == ord('s')):
                smartdashboard.putBoolean('S', True)
                moveY = 5

        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT or event.key == ord('a')):
                smartdashboard.putBoolean('A', False)
                moveX=0

            if (event.key==pygame.K_RIGHT or event.key == ord('d')):
                smartdashboard.putBoolean('D', False)
                moveX=0

            if (event.key==pygame.K_UP or event.key == ord('w')):
                smartdashboard.putBoolean('W', False)
                moveY=0
 
            if (event.key==pygame.K_DOWN or event.key == ord('s')):
                smartdashboard.putBoolean('S', False)
                moveY=0
            if event.type == pygame.MOUSEMOTION:
                # gets the mouse position
                x, y = pygame.mouse.get_pos()
                print(x)
    
 
    window.fill(black)
 
    x+=moveX
    y+=moveY
 
    pygame.draw.rect(window,white,(x,y,50,50))
 
    clock.tick(50)
 
    pygame.display.flip()
    pygame.event.pump()
 
pygame.quit()