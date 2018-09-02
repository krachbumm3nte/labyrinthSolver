class Node:
    def __init__(self, position):
        self.position = position
        self.otherNodes = [None, None, None, None]

    def addnode(self, node):
        self.otherNodes.append(node)

    def replacenode(self, node1, node2):
        self.otherNodes.remove(node1)
        self.otherNodes.append(node2)

    def removeduplicates(self):
        if len(self.otherNodes) == 2:
            n1 = self.otherNodes[0]
            n2 = self.otherNodes[1]
            n1.replaceNode(self, n2)
            n2.replaceNode(self, n1)
            del self


