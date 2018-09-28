from PIL import Image
import Node
import Maze
import Point


class Solver(object):
    m = Maze.Maze()
    width = m.width
    height = m.height
    start = Point.Point(m.findstart(), 0)
    goal = Point.Point(m.findgoal(), height)

    def __init__(self):
        self.solve(self.m)

    def solve(self, m):
        print("hello there")
        nodes = []
        nodecounter = 0
        currentindex = m.findstart()
        direction = 2
        while nodecounter < 4:
            print("currently at: ", self.indextopoint(currentindex))
            nodecounter = nodecounter + 1
            nodes.append(Node.Node(currentindex, self.oppositedirection(direction)))
            currentindex = self.moveUntilNewNode(currentindex, direction)


        print(nodes)

    def moveUntilNewNode(self, index: int, direction: int) -> int:
        while True:
            print("moving into direction ", direction, " at point ", self.indextopoint(index))
            index = self.movedirectional(index, direction)
            if self.m.shouldbenode(index):
                print("new node at index ", index)
                return index

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

    def indextopoint(self, i: int) -> Point:
        return Point.Point(i%self.width, int(i/self.height))

s1 = Solver()
