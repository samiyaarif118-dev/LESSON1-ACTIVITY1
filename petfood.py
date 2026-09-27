import pygame
import random 

screen_width, screen_height = 500, 600
screen_movement = 5
font_size = 75

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("data structure/cat.jpg"),(screen_width,screen_height))

font = pygame.font.SysFont("Arial", font_size)

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change,screen_width - self.rect.width),0)

        self.rect.y = max(min(self.rect.y + y_change,screen_height - self.rect.height),0)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pet food collection game")
all_sprite = pygame.sprite.Group()
pet = sprite(pygame.Color("brown"),40, 40)

pet.rect.x = 30
pet.rect.y = 180

all_sprite.add(pet)
pet_food = sprite(pygame.Color("orange"),30,30)
pet_food.rect.x = random.randint(100, screen_width - pet_food.rect.width)
pet_food.rect.y = random.randint(0, screen_height - pet_food.rect.height)
all_sprite.add(pet_food)

running = True
food_collected = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not food_collected:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - 
                    keys[pygame.K_LEFT]) * screen_movement
            
        y_change = (keys[pygame.K_DOWN] -
                        keys[pygame.K_UP]) * screen_movement

        pet.move(x_change, y_change)

        if pet.rect.colliderect(pet_food.rect):
            all_sprite.remove(pet_food)
            food_collected = True 

    screen.blit(background_image,(0, 0 ))

    all_sprite.draw(screen)

    if food_collected:
        win_text = font.render("food collected!", True, pygame.Color("black"))

        text_x = (screen_width - win_text.get_width()) // 2
        text_y = (screen_height - win_text.get_height()) // 2

        screen.blit(win_text,(text_x,text_y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


    