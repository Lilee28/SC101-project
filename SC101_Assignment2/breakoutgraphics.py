"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program sets up the basic elements for the game "breakout".
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gcolor import GColor
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.brick_offset = brick_offset
        self.ball_radius = ball_radius
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2, y=self.window_height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window_width/2-ball_radius, y=self.window_height/2-self.ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)

        # Draw bricks
        x_value = 0
        y_value = brick_offset
        color = 20
        while y_value < brick_offset + brick_rows * (brick_height + brick_spacing):
            self.brick = GRect(brick_width, brick_height, x=x_value, y=y_value)
            self.brick.filled = True
            self.brick.fill_color = GColor(color, color, color)
            self.window.add(self.brick)
            x_value += brick_width + brick_spacing
            if x_value - brick_spacing == self.window_width:
                x_value = 0
                y_value += brick_height + brick_spacing
                if (y_value - brick_offset) % (2 * (brick_height + brick_spacing)) == 0:
                    color += 510 // brick_rows

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_the_game)

    def move_paddle(self, mouse):
        if mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def start_the_game(self, mouse):
        # redefine the velocities to start moving the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_x_velocity(self):
        # getter function of the x_velocity
        x_velocity = self.__dx
        return x_velocity

    def get_y_velocity(self):
        # getter function of the y_velocity
        y_velocity = self.__dy
        return y_velocity

    def reset_ball(self):
        # when the player dies but still has
        self.ball.x = self.window_width / 2 - self.ball_radius
        self.ball.y = self.window_height / 2 - self.ball_radius
        self.__dx = 0
        self.__dy = 0

