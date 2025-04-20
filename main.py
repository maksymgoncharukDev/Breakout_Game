import pygame
import random

# Initialize
pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [4, -4]

# Blocks
block_rows, block_cols = 5, 8
block_width = WIDTH // block_cols
block_height = 30
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# Game Loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    SCREEN.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 6
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 6

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Wall collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1

    # Paddle collision
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Block collision
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        del blocks[hit_index]
        ball_speed[1] *= -1

    # Lose condition
    if ball.bottom >= HEIGHT:
        print("Game Over!")
        running = False

    # Drawing
    pygame.draw.rect(SCREEN, BLUE, paddle)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(SCREEN, RED, block)

    pygame.display.flip()

pygame.quit()