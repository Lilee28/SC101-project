"""
File: get_object.py
Name: 李知穎 Anita Lee
----------------------
TODO:This program will generate code to obtain objects.
"""
from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow
from campy.graphics.gcolor import GColor
from campy.graphics.gfont import GFont
from campy.gui.events.mouse import onmouseclicked
image = GImage('eva2.jpeg')
window = GWindow(image.width, image.height)
name = input('name: ')
number = 0
x1 = 0
y1 = 0
mouse_y = 0


def main():
    """
    TODO:
    """
    print(f'{window.width}, {window.height}')
    onmouseclicked(get_object)
    window.add(image)
    print('# ' + str(name))
    print(str(name) + ' = GPolygon()')
    if mouse_y < 0:
        print(str(name) + '.filled = True')
        print(str(name) + '.fill_color = "white"')
        print('window.add('+str(name) + ')')


def get_object(mouse):
    global number, x1, y1, mouse_y
    if number != -1:
        mouse_y = mouse.y
        number += 1
        dx = mouse.x - x1
        dy = mouse.y - y1
        if number == 1:
            print(str(name) + '.add_vertex(point=('+str(mouse.x)+','+str(mouse.y)+'))')
        elif mouse.y < 0:
            print(str(name) + '.filled = True')
            print(str(name) + '.fill_color = "white"')
            print('window.add(' + str(name) + ')')
            number = -1
        else:
            print(str(name) + '.add_edge(' + str(dx) + ',' + str(dy)+')')
        pixel_position1 = GOval(4, 4, x=mouse.x-2, y=mouse.y-2)
        window.add(pixel_position1)
        x1 = mouse.x
        y1 = mouse.y


if __name__ == '__main__':
    main()
