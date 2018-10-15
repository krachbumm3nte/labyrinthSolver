import maze
import point
import node


class Solver(object):
    m = maze.Maze()
    width = m.width
    height = m.height
    start = point.Point(m.findstart(), 0)
    goal = point.Point(m.findgoal(), height)

    def __init__(self):
        print(self.m.free(9))
        print(self.indextopoint(27))
        print(self.pointtoindex(11, 1))
        i = self.pointtoindex(13, 2)
        print(self.m.free(i))
        print(self.m.shouldbenode(i))
        self.solve(self.m)

    def solve(self, m):
        print("hello there")
        nodes = []
        nodecounter = 0
        currentindex = m.findstart()
        direction = 2
        while nodecounter < 1:
            print("currently at: ", self.indextopoint(currentindex))
            n = node.Node(currentindex, self.oppositedirection(direction))
            nodes.append(n)
            currentindex = self.moveUntilNewNode(currentindex, direction)
            nodecounter = nodecounter + 1

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

    def indextopoint(self, i: int) -> point:
        return point.Point(i % self.width, int(i / self.height))

    def pointtoindex(self, x: int, y: int) -> int:
        return y * self.width + x


s1 = Solver()
