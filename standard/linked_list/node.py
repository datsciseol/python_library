class Node:
    def __init__(self, objValue = "", nodeNext = "", binHead = False, binTail = False):
        self.objValue = objValue
        self.nodeNext = nodeNext
        self.binHead = binHead
        self.binTail = binTail
    def setValue(self, objValue):
        self.objValue = objValue
    def getValue(self):
        return self.objValue
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def getNext(self):
        return self.nodeNext
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail

node1 = Node(objValue = "a")
nodeTail = Node(binTail = True)
nodeHead = Node(binHead = True, nodeNext = node1)
