# Make a 2-player ping pong game!

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Ping Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
PADDLE_SPEED = 10

BALL_SIZE = 10
ball_speed_x = 3
ball_speed_y = 1

paddleL = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddleR = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and paddleL.top > 0:
        paddleL.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddleR.bottom < HEIGHT:
        paddleL.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddleR.top > 0:
        paddleR.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddleR.bottom < HEIGHT:
        paddleR.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(paddleL) or ball.colliderect(paddleR):
        ball_speed_x *= -1

    pygame.draw.rect(screen, WHITE, paddleL)
    pygame.draw.rect(screen, WHITE, paddleR)
    pygame.draw.ellipse(screen, WHITE, ball)

    pygame.display.flip()
    clock.tick(60)