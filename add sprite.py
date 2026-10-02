import random
import pygame 

pygame.init()
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Game" )

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 5

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5

        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += 5


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 30)
        self.rect.y = random.randint(50, screen_height // 2)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0

clock = pygame.time.Clock()
running = True

while running:
  screen.fill(black)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  all_sprites.update()

  collisions = pygame.sprite.spritecollide(player, enemies, True)
  if collisions:
    score += len(collisions)
    for _ in collisions:
      new_enemy = Enemy()
      all_sprites.add(new_enemy)
      enemies.add(new_enemy)

  all_sprites.draw(screen)
  font = pygame.font.SysFont(None, 36)
  score_text = font.render(f"Score: {score}", True, white)
  screen.blit(score_text, (10, 10))
  pygame.display.flip()
  clock.tick(60)

pygame.quit()