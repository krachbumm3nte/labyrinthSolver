import maze


class Node:
    def __init__(self, position : int, distance : int):
        self.position = position
        self.distance = distance



    def __str__(self):
        return f"[Node at :{self.position}, distance: {self.distance}]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.position == other.position
        else:
            return False
