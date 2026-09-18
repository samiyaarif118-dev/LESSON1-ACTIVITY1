import pygame 

pygame.init()
screen = pygame.display.set_mode((300, 400))

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(screen, (0, 255, 0),pygame.Rect(30,30, 60, 60))
    pygame.draw.circle(screen, (255, 0, 0), (150 , 200 ), 30 , 6)

    
    pygame.display.flip()




