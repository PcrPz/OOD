class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQueue(self, i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def append(root,data):
            if root == None:
                root = Node(data)
            elif data < root.data:
                root.left = append(root.left,data)
            elif data >= root.data:
                root.right = append(root.right,data)
            return root
        self.root = append(self.root,data)
        return self.root
        
    def breadthFirst(self):
        queueForCheck = Queue()
        queueForCheck.enQueue(self.root)
        listP = []
        while not queueForCheck.isEmpty() :
            n = queueForCheck.deQueue()
            listP.append(str(n.data))
            if n.left != None :
                queueForCheck.enQueue(n.left)
            if n.right != None :
                queueForCheck.enQueue(n.right)
        return print(f"Breadth : {' '.join(listP)}")


    def preOrder(self):
        def repreOrder(root,listP):
            listPrint = listP
            if root is not None:
                listPrint.append(str(root.data))
                repreOrder(root.left,listPrint)
                repreOrder(root.right,listPrint)
            return listPrint
        message = repreOrder(self.root,[])
        print(f"Preorder : {' '.join(message)}")
    
    def postOrder(self):
        def repostOrder(root,listP):
            listPrint = listP
            if root is not None:
                repostOrder(root.left,listPrint)
                repostOrder(root.right,listPrint)
                listPrint.append(str(root.data))
            return listPrint
        message = repostOrder(self.root,[])
        print(f"Postorder : {' '.join(message)}")


    def inOrder(self):
        def reinOrder(root,listP):
            listPrint = listP
            if root is not None:
                reinOrder(root.left,listPrint)
                listPrint.append(str(root.data))
                reinOrder(root.right,listPrint)
            return listPrint
        message = reinOrder(self.root,[])
        print(f"Inorder : {' '.join(message)}")


    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
message = [int(i) for i in input("Enter Input : ").split()]
for i in message:
    root = T.insert(i)
T.preOrder()
T.inOrder()
T.postOrder()
T.breadthFirst()