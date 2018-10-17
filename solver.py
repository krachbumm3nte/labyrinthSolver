import maze
import point
import node


# a class that implements the main functionality of iterating through a maze, until the exit is found
class Solver(object):

    def __init__(self):
        self.m = maze.Maze()
        self.width = self.m.width
        self.height = self.m.height
        self.start = node.Node(self.m.findstart(), 0)
        self.goal = node.Node(self.m.findgoal(), -1)
        self.knownNodes = []
        self.borderRegion = []

        self.solve()

    def solve(self):

        self.borderRegion.append(self.start)

        while True:
            if len(self.borderRegion) == 0:
                print("error, no elements in the borderRegion")
                exit()

            n = self.pickNextNode()
            self.expand(n)

    def moveuntilnewnode(self, index: int, distance: int, direction: int) -> node.Node:
        addeddistance = 0
        while True:
            if index < 0:
                return self.start
            index = self.movedirectional(index, direction)
            addeddistance = addeddistance + 1
            if self.m.shouldbenode(index):
                print("new node found at point ", self.indextopoint(index))
                return node.Node(index, distance + addeddistance)

    def moveup(self, index) -> int:
        return index - self.width

    def movedown(self, index) -> int:
        return index + self.width

    def moveleft(self, index) -> int:
        return index - 1

    def moveright(self, index) -> int:
        return index + 1

    def nextdirection(self, direction) -> int:
        return (direction + 1) % 4

    def oppositedirection(self, direction) -> int:
        return (direction + 2) % 4

    def previousdirection(self, direction: int) -> int:
        newdir = direction - 1
        return 3 if newdir < 0 else newdir

    def movedirectional(self, i: int, direction) -> int:
        if direction == 0:
            return self.moveup(i)

        elif direction == 1:
            return self.moveright(i)

        elif direction == 2:
            return self.movedown(i)

        elif direction == 3:
            return self.moveleft(i)

    def indextopoint(self, i: int) -> point:
        return point.Point(i % self.width, int(i / self.height))

    def expand(self, n: node):
        print(f"expanding node at {self.indextopoint(n.position)}")
        index = n.position
        directions = self.m.getavailabledirections(index)
        for direction in directions:
            n1 = self.moveuntilnewnode(index, n.distance, direction)
            if self.nodeIsUnknown(n1):
                if n1.__eq__(self.goal):
                    x = n1.distance
                    self.goal.distance = x

                    print("whoop whoop")
                    print(f"known nodes: {self.knownNodes}")
                    print(f"border region: {self.borderRegion}")

                    exit()
                self.borderRegion.append(n1)

    def pickNextNode(self):
        n = self.borderRegion.pop(-1)
        self.knownNodes.append(n)
        return n

    def nodeIsUnknown(self, n: node):
        return not self.borderRegion.__contains__(n) and not self.knownNodes.__contains__(n)


s1 = Solver()
