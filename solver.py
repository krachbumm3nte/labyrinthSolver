import maze
import point
import node


# a class that implements the main functionality of iterating through a maze, until the exit is found



class Solver(object):

    def __init__(self):
        self.m = maze.Maze()
        self.width = self.m.width
        self.height = self.m.height
        self.start = node.Node(self.m.findstart(), 0, None)
        self.goal = node.Node(self.m.findgoal(), -1, None)
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

    def moveuntilnewnode(self, n: node.Node, distance: int, direction: int) -> node.Node:
        addeddistance = 0
        index = n.position
        while True:
            if index < 0:
                return self.start
            index = self.movedirectional(index, direction)
            addeddistance = addeddistance + 1
            if self.m.shouldbenode(index):
                print("new node found at point ", self.indextopoint(index))
                return node.Node(index, distance + addeddistance, n)

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
            n1 = self.moveuntilnewnode(n, n.distance, direction)
            if self.nodeIsUnknown(n1):
                if n1.__eq__(self.goal):
                    self.goal = n1

                    print("whoop whoop")
                    print(f"known nodes: {self.knownNodes}")
                    print(f"border region: {self.borderRegion}")
                    print(self.retracepath(n))
                    print("hello")
                    exit()
                self.borderRegion.append(n1)

    # choses wich node to expand next (only depth-first so far)
    def pickNextNode(self):
        n = self.borderRegion.pop(-1)
        self.knownNodes.append(n)
        return n

    # determines if a maze has not been discovered yet
    def nodeIsUnknown(self, n: node):
        return not self.borderRegion.__contains__(n) and not self.knownNodes.__contains__(n)

    def retracepath(self, n: node.Node):
        return self.listPreviousNodes(n)

    def listPreviousNodes(self, n: node.Node) -> list:
        nodes = []
        nodes.append(n)
        n = n.previous
        while n.previous is not None:
            nodes.append(n)
            n = n.previous
        return nodes



s1 = Solver()
