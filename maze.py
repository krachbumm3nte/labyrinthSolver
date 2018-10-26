from PIL import Image

# a class to represent a maze that was generated from a .png image
class Maze:

    # initializes the maze, setting variables and decoding the input image to a list of rgb values
    def __init__(self, image):
        print("loading input image...")
        self.image = Image.open(image, 'r').convert('RGB')
        self.outputimage = self.image.load()
        self.pixels = self.image.getdata()
        self.entrances = []


        self.width = self.image.width
        self.height = self.image.height
        self.size = self.height * self.width
        print("loaded an image of size: ", self.width, "x", self.height)

        # determining validity of the maze
        if not self.isvalid():
            print("invalid maze, exiting...")
            print("hint:")
            print("\ta valid maze consists of white pixels graphing the path, and black pixels displaying the walls.")
            print("\ta valid maze has a one pixel wide layer of wall around it, leaving only two gaps for entry and exit ")
            exit()

    # checks if a given index is a field (true) or a wall (false)
    def free(self, x: int) -> bool:
        return 0 < x < self.size and self.pixels[x][0] != 0

    # transforms an index on the array to a coordinate point
    def indextopoint(self, i):
        return i % self.width, int(i / self.height)

    # checks validity of the maze
    def isvalid(self):
        lastrowindex = self.width * (self.height -1)
        for i in range(self.width):
            if self.free(i):
                self.entrances.append(i)

            if self.free(i + lastrowindex):
                self.entrances.append(i + lastrowindex)

        for i in range(self.height):
            i1 = i*self.width
            if self.free(i1):
                self.entrances.append(i1)
            if self.free(i1+ self.width - 1):
                self.entrances.append(i1 + self.width -1)
        print(f"entrance at {self.indextopoint(self.entrances[0])}, exit at {self.indextopoint(self.entrances[1])}")
        return len(self.entrances) == 2

    # returns the index of the mazes entrance
    def getstart(self) -> int:
        return self.entrances[0]

    # returns the index of the mazes exit
    def getgoal(self) -> int:
        return self.entrances[1]
