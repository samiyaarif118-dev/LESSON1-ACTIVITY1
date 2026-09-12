import pygame 
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.display.flip()
pygame.quit()
