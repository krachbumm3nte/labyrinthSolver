from PIL import Image
import Node
import Point


class Maze:


    def __init__(self):

        def indextopoint(i):
            return Point.Point(i%width, int(i/height))

        nodes = []

        im = Image.open('simplemaze.png', 'r')

        pixels = list(im.getdata())
        width = im.width

        height = im.height

        print(width, "x", height)

        for i in range(width):
            if free(pixels[i]):
                print("startpoint at: ", indextopoint(i))
                break

        for i in range(width, width * (height - 1)):
            #print(i-width, i, i+width)
            if free(pixels[i]) and (free(pixels[i+width]) or free(pixels[i-width])) and (free(pixels[i-1]) or free(pixels[i+1])):
                print("node at ", indextopoint(i))


def free(x):
    return x[0] > 0

