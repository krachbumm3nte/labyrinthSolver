from node import Node
import maze


class Mazecrawler:
    def __init__(self, m: maze.Maze):
        self.m = m

    def moveuntilnextnode(self, n: Node, distance: int, direction: int) -> Node:
        addeddistance = 0
        index = n.position
        while True:
            if index < 0:
                return Node(self.m.findstart(), 0, None)
            index = self.movedirectional(index, direction)
            addeddistance = addeddistance + 1
            if self.shouldbenode(index):
                return Node(index, distance + addeddistance, n)

    def moveup(self, index) -> int:
        return index - self.m.width

    def movedown(self, index) -> int:
        return index + self.m.width

    def moveleft(self, index) -> int:
        return index - 1

    def moveright(self, index) -> int:
        return index + 1

    def movedirectional(self, i: int, direction) -> int:
        if direction == 0:
            return self.moveup(i)

        elif direction == 1:
            return self.moveright(i)

        elif direction == 2:
            return self.movedown(i)

        elif direction == 3:
            return self.moveleft(i)

    def expandnode(self, n: Node, func):
        index = n.position
        directions = self.getavailabledirections(index)
        for direction in directions:
            n1 = self.moveuntilnextnode(n, n.distance, direction)
            func(n1)

    # returns all of the directions available at index
    def getavailabledirections(self, index: int):
        directions = []
        if self.m.free(self.moveup(index)):
            directions.append(0)
        if self.m.free(self.moveright(index)):
            directions.append(1)
        if self.m.free(self.movedown(index)):
            directions.append(2)
        if self.m.free(self.moveleft(index)):
            directions.append(3)

        return directions

    # determins if a node should be created at index i
    def shouldbenode(self, index: int) -> bool:
        directions = self.getavailabledirections(index)
        return not (len(directions) == 2 and sum(directions) % 2 == 0)