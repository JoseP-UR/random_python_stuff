def move_up(speed):
    if (speed[1] > 0):
        speed[1] = -speed[1]
    return speed


def move_down(speed):
    if (speed[1] < 0):
        speed[1] = -speed[1]
    return speed

def move_left(speed):
    if (speed[0] > 0):
        speed[0] = -speed[0]
    return speed

def move_right(speed):
    if (speed[0] < 0):
        speed[0] = -speed[0]
    return speed