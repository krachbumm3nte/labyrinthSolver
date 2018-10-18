""" a node class that represents a key point inside the maze
    currently holds information about its position (as index) and the distance to the startpoint
    might eventually be used to create an actual graph, who knows?
"""


class Node:
    def __init__(self, position: int, distance: int, previous):
        self.position = position
        self.distance = distance
        self.previous = previous

    def __str__(self):
        return f"[Node at :{self.position}, distance: {self.distance}]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.position == other.position
        else:
            return False
"""
    def __iter__(self):
        return self

    def __next__(self):
        return self.previous
"""
