import maze
import node
from mazecrawler import Mazecrawler
import timeit


# a class that implements the main functionality of iterating through a maze, until the exit is found


class Solver:

    def __init__(self, args):
        self.algorithm = args[0]
        self.m = maze.Maze(args[1])
        self.start = node.Node(self.m.findstart(), 0, None)
        self.goal = node.Node(self.m.findgoal(), -1, None)
        self.knownNodes = []
        self.borderRegion = []
        self.popindex = 0
        self.determinealgorithm()
        self.crawler = None
        self.starttime = 0
        self.solve()

    def solve(self):
        self.crawler = Mazecrawler(self.m)
        print("starting solving-algorithm...")
        self.starttime = timeit.default_timer()
        self.borderRegion.append(self.start)
        while True:
            if len(self.borderRegion) == 0:
                print("error, no elements in the borderRegion")
                exit()
            n = self.pickNextNode()
            self.crawler.expandnode(n, self.explorenewnodes)

    def indextopoint(self, i: int) -> tuple:
        return i % self.m.width, int(i / self.m.height)

    def explorenewnodes(self, node):
        if self.nodeIsUnknown(node):
            if node.__eq__(self.goal):
                self.success(node)
            self.borderRegion.append(node)
        #else :
            #self.cascadenodedistance(node)

    # choses wich node to expand next
    def pickNextNode(self):
        if self.algorithm == '-dj':
            self.borderRegion.sort()

        n = self.borderRegion.pop(self.popindex)
        self.knownNodes.append(n)
        return n

    def success(self, node):
        self.goal = node
        time = timeit.default_timer() - self.starttime
        print("traversal complete!")
        print(f"total nodes visited: {len(self.borderRegion) + len(self.knownNodes)}")
        print(f"total pathlength: {self.goal.distance}")
        print(f"total duration: {time}")
        self.prepareoutput(node)

        exit()

        self.borderRegion.append(node)

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

    def printNodes(self, list):
        for n in list:
            s = 'N:({}),D:({})'.format(self.indextopoint(n.position), n.distance)
            print(s)
            n = s

    def imprintpath(self, node: node.Node):
        list = self.listPreviousNodes(node)
        for node in list:
            n1 = node.previous
            p1 = node.position
            p2 = n1.position
            if ((p1 - p2) / self.m.width).is_integer():
                for i in range(p1, p2, -self.m.width if p1 > p2 else self.m.width):
                    self.m.outputimage[self.indextopoint(i)] = (255, 0, 0)
            else:
                for i in range(p1, p2, -1 if p1 > p2 else 1):
                    self.m.outputimage[self.indextopoint(i)] = (255, 0, 0)

    '''
    paints all of the known nodes to the output-image
    known nodes are blue
    completely explored nodes are green
    start and goal are yellow
    '''

    def paintexplorednodes(self):
        for n in self.knownNodes:
            self.m.outputimage[self.indextopoint(n.position)] = (0, 255, 0)
        for n in self.borderRegion:
            self.m.outputimage[self.indextopoint(n.position)] = (0, 0, 255)
        self.m.outputimage[self.indextopoint(self.start.position)] = (255, 255, 0)
        self.m.outputimage[self.indextopoint(self.goal.position)] = (255, 255, 0)

    def determinealgorithm(self):
        if self.algorithm == '-dj':
            print("solving by dijkstra-algorithm...")
        elif self.algorithm == '-df':
            self.popindex = -1
            print("solving depth-first...")
        elif self.algorithm == '-bf':
            print("solving bredth-first...")
        else:
            print("invalid algorithm: pick between dijkstra (-dj), breadth-first (-bf) or depth-first (-df)")
            exit()

    def prepareoutput(self, node):
        self.crawler.expandnode(node, self.imprintpath)
        self.paintexplorednodes()
        self.m.image.save('solution.png')


    #TODO: proper node distance cascading
    def cascadenodedistance(self, node: node.Node):
        if self.replaceifshorter(node, self.borderRegion) or self.replaceifshorter(node, self.knownNodes):
            self.crawler.expandnode(node, self.cascadenodedistance)

    def replaceifshorter(self, node, nodelist: list):
        print("replacing if shorter")
        for n1 in nodelist:
            if n1 == node:
                if node.distance < n1.distance:
                    nodelist[n1.position] = node
                    return True
                return False


s1 = Solver(("-df", "128x128.png"))
