import maze


class Node:
    def __init__(self, position : int, lastdirection : int):
        self.position = position
        self.checkedDirections = []
        self.checkedDirections.append(lastdirection)



    def __str__(self):
        return f"Node at :{self.position}"

    def __repr__(self):
        return self.__str__()

