import sys, pygame, movement

size = width, height = 800, 600
speed = [1, 1]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('intro_ball.gif')
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                movement.move_up(speed)
            if event.key == 274:
                movement.move_down(speed)
            if event.key == 275:
                movement.move_right(speed)
            if event.key == 276:
                movement.move_left(speed)

        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()