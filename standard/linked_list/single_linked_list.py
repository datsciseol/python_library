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
    
class Singlelinkedlist:
    def __init__(self):
        self.nodeTail = Node(binTail = True)
        self.nodeHead = Node(binHead = True, nodeNext = self.nodeTail)
        self.size = 0
    
    def insertAt(self, insertVal, insertIdx):
        nodeNew = Node(objValue = insertVal)
        nodePrev = self.get(insertIdx - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def RemoveAt(self, removeIdx):
        nodePrev = self.get(removeIdx - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
    
    def get(self, idx):
        nodeReturn = self.nodeHead
        for iter in range(idx + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end = " ")
        print()
    
    def getSize(self):
        return self.size

list1 = Singlelinkedlist()
list1.insertAt("a", 0)
list1.insertAt("b", 1)
list1.printStatus()
