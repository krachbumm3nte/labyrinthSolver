from PIL import Image
import point


class Maze:

    def __init__(self):

        image = Image.open('simplemaze.png', 'r')

        self.pixels = list(image.getdata())

        self.width = image.width
        self.height = image.height
        self.size = self.width * self.height
        print("maze of size: ", self.width, "x", self.height)

        # determining validity of the maze
        if not self.isvalid():
            print("invalid maze, exiting...")
            print("hint:")
            print("\ta valid maze consists of white pixels graphing the path, and black pixels displaying the walls.")
            print("\ta valid maze has a one pixel wide layer of wall around it, leaving only two gaps for "
                  "entry and exit in the first and last row respectively.")
            exit()

    def free(self, x: int) -> bool:
        return self.pixels[x][0] != 0 if 0 < x < (self.width * self.height) else False

    def indextopoint(self, i):
        return point.Point(i % self.width, int(i / self.height))

    def isvalid(self):
        entriesfound = 0
        exitsfound = 0
        for i in range(self.width):
            if self.free(i): entriesfound = entriesfound + 1
            if entriesfound > 1: return False

        for i in range(self.width * (self.height - 1), self.width * self.height):
            if self.free(i): exitsfound = exitsfound + 1
            if exitsfound > 1: return False

        for i in range(self.height):
            if self.free(i * self.width) or self.free(i * self.width + self.width - 1): return False

        return entriesfound == 1 and exitsfound == 1

    def findstart(self) -> int:
        for i in range(self.width):
            if self.free(i):
                print("start at {}".format(self.indextopoint(i)))
                return i

    def findgoal(self) -> int:
        for i in range(self.width * (self.height - 1), self.width * self.height):
            if self.free(i):
                print("goal at {}".format(self.indextopoint(i)))
                return i

    def moveup(self, index: int) -> int:
        return index - self.width

    def movedown(self, index: int) -> int:
        return index + self.width

    def moveleft(self, index: int) -> int:
        return index - 1

    def moveright(self, index: int) -> int:
        return index + 1

    def shouldbenode(self, i: int) -> bool:
        directions = self.getavailabledirections(i)
        return len(directions) == 1 or sum(directions)% 2 != 0 or len(directions) > 2


    def getavailabledirections(self, index: int):
        directions = []
        if self.free(self.moveup(index)):
            directions.append(0)
        if self.free(self.moveright(index)):
            directions.append(1)
        if self.free(self.movedown(index)):
            directions.append(2)
        if self.free(self.moveleft(index)):
            directions.append(3)

        return directions
