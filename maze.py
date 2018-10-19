from PIL import Image

# a class to represent a maze that was generated from a .png image
class Maze:

    # initializes the maze, setting variables and decoding the input image to a list of rgb values
    def __init__(self, image):

        self.image = Image.open(image, 'r')
        self.outputimage = self.image.load()
        self.pixels = self.image.getdata()

        self.width = self.image.width
        self.height = self.image.height
        print("maze of size: ", self.width, "x", self.height)

        # determining validity of the maze
        if not self.isvalid():
            print("invalid maze, exiting...")
            print("hint:")
            print("\ta valid maze consists of white pixels graphing the path, and black pixels displaying the walls.")
            print("\ta valid maze has a one pixel wide layer of wall around it, leaving only two gaps for "
                  "entry and exit in the first and last row respectively.")
            exit()

    # checks if a given index is a field (true) or a wall (false)
    def free(self, x: int) -> bool:
        return self.pixels[x][0] != 0 if 0 < x < (self.width * self.height) else False

    # transforms an index on the array to a coordinate point
    def indextopoint(self, i):
        return i % self.width, int(i / self.height)

    # checks validity of the maze
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

    # returns the index of the mazes entrance
    def findstart(self) -> int:
        for i in range(self.width):
            if self.free(i):
                print("start at {}".format(self.indextopoint(i)))
                return i

    # returns the index of the mazes exit
    def findgoal(self) -> int:
        for i in range(self.width * (self.height - 1), self.width * self.height):
            if self.free(i):
                print("goal at {}".format(self.indextopoint(i)))
                return i
