import pygame as py

py.init()
screen = py.display.set_mode((400, 300))
clock = py.time.Clock()

paddle_x = 200
ball_x, ball_y = 50, 25
ball_dx, ball_dy = 3, -3

game_over = False
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[py.K_RIGHT] and paddle_x < 350:
        paddle_x += 5

    if not game_over:
        ball_x += ball_dx
        ball_y += ball_dy

    if ball_x <= 0 or ball_x >= 380:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    if (ball_y >= 270 and paddle_x <= ball_x <= paddle_x+50):
        ball_dy = -abs(ball_dx)

    if ball_y > 300:
        game_over = True

    screen.fill((0,0,0))

    py.draw.rect(screen, (255, 255, 255), (paddle_x, 280, 50, 10))
    py.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), 10)

    py.display.flip()
    clock.tick(60)

py.quit()