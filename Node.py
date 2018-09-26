import Point


class Node:
    def __init__(self, position : int, lastdirection : int) -> object:
        self.position = position
        self.checkedDirections = []
        self.lastdirection = lastdirection


