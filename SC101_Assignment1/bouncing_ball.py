"""
File: bouncing_ball.py
Name: 李知穎 Anita Lee
-------------------------
TODO: This program animates a bouncing ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 20
GRAVITY = 0.5
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
time = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)
    window.add(ball, x=START_X, y=START_Y)
    ball.filled = True


def bounce(mouse):
    global time
    if ball.x == START_X and ball.y == START_Y and time < 3:
        # the animation can only be performed 3 times
        time += 1
        vertical_velocity = 0
        while True:
            # when going downward: the velocity increases continuously
            # when going upward: the velocity decreases continuously
            vertical_velocity += GRAVITY
            # the ball moves at a constant rate horizontally, but at a changing rate vertically
            ball.move(VX, vertical_velocity)
            if 0 <= (ball.y + SIZE - window.height) < vertical_velocity:
                """
                1. when the ball is lower than the window, the ball bounces and the y velocity is reduced
                2. when the ball is bouncing upward, the velocity decreases while the (ball.y + SIZE - window.height) 
                value increases
                3. during the 2nd and 3rd bounce, the initial value of the velocity is greater than the last bounce, 
                therefore, the 2 values meet at a larger y value, decreasing the height of each bounce
                """
                vertical_velocity = -vertical_velocity
                vertical_velocity *= REDUCE
            pause(DELAY)
            window.add(ball)
            if ball.x + SIZE >= window.width:
                # if the ball bounces out of the window from the right, the animation stops
                window.add(ball, x=START_X, y=START_Y)
                break


if __name__ == "__main__":
    main()
