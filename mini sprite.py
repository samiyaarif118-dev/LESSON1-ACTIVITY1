import pygame
def mini():
    pygame.init()

    screen_width , screen_height = (500,500)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mini Sprite Adventure")

    x, y = 50, 50
    sprite_width, sprite_height = 60,70
    speed = 4 

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    current_color = white 

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            x -= speed

        if pressed [pygame.K_RIGHT]:
            x += speed 

        if pressed [pygame.K_UP]:
            y -= speed

        if pressed [pygame.K_DOWN]:
            y += speed

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)


        if x == 0:
            current_color = blue 

        elif x == screen_width - sprite_width:
            current_color = yellow 

        elif y == 0:
            current_color = red 

        elif y == screen_height - sprite_height:
            current_color = green 

        else:
            current_color = white

        screen.fill(black)

        pygame.draw.circle(screen,green,(420, 320), 35)
        pygame.draw.circle(screen,blue,(80, 320), 35, 4)

        sprite_rect = pygame.Rect(x, y, sprite_width, sprite_height)

        pygame.draw.rect(screen,current_color, sprite_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": 
     mini()
