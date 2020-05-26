class Node:
    def __init__(self, name):
        self.children = []
        self.name=name

    def addChild(self, name):
        self.children.append(name)

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        print(array)
        return array


Node.depthFirstSearch([2,3,45,34,2])