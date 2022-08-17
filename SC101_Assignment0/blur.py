"""
File: blur.py
Name: 李知穎
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    TODO: This program blurs the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    # show the original image for later comparison
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        # blur the image for multiple times
        blurred_img = blur(blurred_img)
    # shows the blurred image
    blurred_img.show()


def blur(img):
    """
    :param img: the original image
    :return: the blurred image
    """
    # create a blank new image
    new_image = SimpleImage.blank(img.width, img.height)
    # get each pixels through their x and y coordinate
    for x in range(new_image.width):
        for y in range(new_image.height):
            p_new = new_image.get_pixel(x, y)
            # set the initial value of the rgb
            n_red = 0
            n_blue = 0
            n_green = 0
            # get the surrounding pixels
            for x1 in range(-1, 2):
                for y1 in range(-1, 2):
                    # avoid getting invalid coordination
                    if not (x == 0 and x1 == -1) and not (y == 0 and y1 == -1):
                        if not (x == img.width - 1 and x1 == 1) and not (y == img.height - 1 and y1 == 1):
                            img_p = img.get_pixel(x + x1, y + y1)
                            n_red += img_p.red
                            n_blue += img_p.blue
                            n_green += img_p.green
            if (x == 0 or x == img.width-1) and (y == 0 or y == img.height-1):
                # the pixel is in the corner
                pixels = 4
            elif x == 0 or x == img.width-1 or y == 0 or y == img.height-1:
                # the pixel is on the side
                pixels = 6
            else:
                # the pixel is not in the corner nor on the side
                pixels = 9
            # get the average of the pixel and its surrounding
            p_new.blue = int(n_blue / pixels)
            p_new.red = int(n_red / pixels)
            p_new.green = int(n_green / pixels)
    return new_image


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
