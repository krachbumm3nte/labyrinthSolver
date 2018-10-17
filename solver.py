import maze
import point
import node


class Solver(object):
    m = maze.Maze()
    width = m.width
    height = m.height
    start = node.Node(m.findstart(),0)
    goal = node.Node(m.findgoal(), -1)
    knownNodes = []
    borderRegion = []

    def __init__(self):
        i = self.pointtoindex(13, 2)
        self.solve(self.m)

    def solve(self, m):

        self.borderRegion.append(self.start)

        while True:
            if len(self.borderRegion) == 0:
                print("error, no elements in the borderRegion")
                exit()

            n = self.pickNextNode()
            self.expand(n)



    def moveUntilNewNode(self, index: int, distance: int, direction: int) -> node.Node:
        addeddistance = 0
        while True:
            if index < 0: return self.start
            index = self.movedirectional(index, direction)
            addeddistance = addeddistance + 1
            if self.m.shouldbenode(index):
                print("new node found at point ", self.indextopoint(index))
                return node.Node(index, distance + addeddistance)


    moveup = lambda self, index: index - self.width
    movedown = lambda self, index: index + self.width
    moveleft = lambda self, index: index - 1
    moveright = lambda self, index: index + 1

    nextdirection = lambda self, direction: (direction + 1) % 4
    oppositedirection = lambda self, direction: (direction + 2) % 4

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

    def pointtoindex(self, x: int, y: int) -> int:
        return y * self.width + x



    def expand(self, n: node):
        print(f"expanding node at {self.indextopoint(n.position)}")
        index = n.position
        directions = self.m.getavailabledirections(index)
        for direction in directions:
            n1 = self.moveUntilNewNode(index,n.distance,direction)
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
        n= self.borderRegion.pop(-1)
        self.knownNodes.append(n)
        return n

    def nodeIsUnknown(self, n: node):
        return not self.borderRegion.__contains__(n) and not self.knownNodes.__contains__(n)

s1 = Solver()
