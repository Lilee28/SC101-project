"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    lives = NUM_LIVES
    num_bricks = graphics.brick_rows * graphics.brick_cols
    x_velocity = 0
    y_velocity = 0
    while lives != 0 and num_bricks != 0:
        if x_velocity == 0 and y_velocity == 0:
            x_velocity = graphics.get_x_velocity()
            y_velocity = graphics.get_y_velocity()
        collision_up_l = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        collision_up_r = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y)
        collision_low_l = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius * 2)
        collision_low_r = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y +
                                                        graphics.ball_radius * 2)
    # brick
        if (collision_up_l or collision_up_r or collision_low_l or collision_low_r is True) and \
                graphics.ball.y + graphics.ball_radius * 2 < graphics.paddle.y:
            y_velocity = -y_velocity
            graphics.window.remove(collision_up_l or collision_up_r or collision_low_l or collision_low_r)
            num_bricks -= 1
            if num_bricks == 0:
                x_velocity = 0
                y_velocity = 0
                graphics.reset_ball()
    # paddle
        elif collision_low_l or collision_low_r is True:
            y_velocity = -y_velocity
    # wall
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball_radius * 2 >= graphics.window_width:
            x_velocity = -x_velocity
        if graphics.ball.y <= 0:
            y_velocity = -y_velocity
    # die
        if graphics.ball.y + graphics.ball_radius * 2 >= graphics.window.height:
            lives -= 1
            x_velocity = 0
            y_velocity = 0
            graphics.reset_ball()
        graphics.ball.move(x_velocity, y_velocity)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
