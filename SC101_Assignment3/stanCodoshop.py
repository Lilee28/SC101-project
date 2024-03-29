"""
File: stanCodoshop.py
Name: 李知穎
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(result.width):
        for y in range(result.height):
            # find the best rgb value for each pixel (x, y)
            pixel = result.get_pixel(x, y)
            pixels = []
            for image in images:
                # set up a list of pixels at certain x & y value from different images
                pixels.append(image.get_pixel(x, y))
            # get the best pixel with the smallest distance from the average
            best_pixel = get_best_pixel(pixels)
            # redefine the rgb value of the blank image
            pixel.red = best_pixel.red
            pixel.blue = best_pixel.blue
            pixel.green = best_pixel.green

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # set the initial value of the distance for later comparison process
    dist = float('inf')
    best = pixels[0]
    for pixel in pixels:
        # compare the pixel from different image one by one
        dist_new = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        if dist > dist_new:
            dist = dist_new
            best = pixel
    return best


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # calculate the distance from each pixel to the average
    dist = math.sqrt((red - pixel.red) ** 2 + (blue - pixel.blue) ** 2 + (green - pixel.green) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    pixel_red = 0
    pixel_green = 0
    pixel_blue = 0
    for pixel in pixels:
        # get the total value of the rgb value of each pixel from different image
        pixel_green += pixel.green
        pixel_red += pixel.red
        pixel_blue += pixel.blue
    # set up a list of the average rgb value
    avg_l = []
    avg_l.append(pixel_red // len(pixels))
    avg_l.append(pixel_green // len(pixels))
    avg_l.append(pixel_blue // len(pixels))
    return avg_l


if __name__ == '__main__':
    main()
