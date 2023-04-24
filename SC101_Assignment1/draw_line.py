"""
File: draw_line.py
Name: 李知穎 Anita Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
click = 0
window = GWindow()
circle = GOval(10, 10)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click
    click += 1
    if click % 2 != 0:
        # first click: add a circle to indicate the starting point
        window.add(circle, x=mouse.x-circle.width/2, y=mouse.y-circle.height/2)
    else:
        # second click: remove the circle and creates a line connecting the first and second click
        window.remove(circle)
        line = GLine(circle.x+circle.width/2, circle.y+circle.height/2, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
