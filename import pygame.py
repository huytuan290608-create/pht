import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Battle Royale")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tốc độ khung hình
FPS = 60
clock = pygame.time.Clock()

# Lớp Nhân vật
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Lớp Kẻ địch
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

# Tạo đối tượng
player = Player(WIDTH//2, HEIGHT//2)
enemies = pygame.sprite.Group()
for _ in range(5):
    enemy = Enemy(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
    enemies.add(enemy)

# Nhóm tất cả sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

# Vòng lặp chính
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Cập nhật
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemies.update(player)
    
    # Vẽ mọi thứ
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
