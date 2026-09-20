import pygame
import random

pygame.init()

car_color_change_event = pygame.USEREVENT + 1 
signal_change_event = pygame.USEREVENT + 2

road = pygame.Color("gray")
purple = pygame.Color("purple")
lightpurple = pygame.Color("pink")
lightpink = pygame.Color("lightpink")
white = pygame.Color("white")


red = pygame.Color("red")
green = pygame.Color("green")

class car(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.velocity = [3, 0]

    def update(self):

        self.rect.move_ip(self.velocity)
        sensor_triggered = False


        if self.rect.left <= 0 or self.rect.right >= 600:
            self.velocity[0] = -self.velocity[0]
            sensor_triggered = True


        if sensor_triggered:
            pygame.event.post(pygame.event.Event(car_color_change_event))
            pygame.event.post(pygame.event.Event(signal_change_event))


    def change_color(self):
        self.image.fill(random.choice([lightpurple,purple,lightpink,white]))


def change_signal():
    global signal_color 

    if signal_color == red:
        signal_color = green
    else: 
        signal_color = red 

all_sprite = pygame.sprite.Group()

mycar = car(purple, 70, 35)

mycar.rect.x = 50
mycar.rect.y = 300

all_sprite.add(mycar)

screen = pygame.display.set_mode((600, 400))

pygame.display .set_caption("smart traffic signal simulator")

signal_color = red 

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == car_color_change_event:
            mycar.change_color()

        elif event.type == signal_change_event:
            change_signal()

    all_sprite.update()
    screen.fill(road)

    for x in range(0, 600, 80):
        pygame.draw.rect(screen, white,(x, 345, 45, 5))


    pygame.draw.rect(screen, pygame.Color("black"),(275, 40, 50, 90))

    pygame.draw.circle(screen,signal_color,(300, 85), 20)

    all_sprite.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit() 

                                          













