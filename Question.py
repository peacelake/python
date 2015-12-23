from Queue import Queue

class Node:
    def __init__(self, data):
        self.Data = data
        self.Left = None
        self.Right = None
        self.Parent = None

class TreeQ:
    def set(self):
        self.root = Node(40)
        self.root.Left = Node (20)
        self.root.Left.Parent = self.root
        self.root.Left.Left = Node (10)
        self.root.Left.Left.Parent = self.root.Left
        self.root.Left.Left.Left = Node (4)
        self.root.Left.Left.Left.Parent = self.root.Left.Left
        self.root.Left.Left.Right = Node (15)
        self.root.Left.Left.Right.Parent = self.root.Left.Left
        self.root.Left.Left.Right.Left = Node (11)
        self.root.Left.Left.Right.Left.Parent = self.root.Left.Left.Right
        self.root.Left.Right = Node (30)
        self.root.Left.Right.Parent = self.root.Left
        self.root.Left.Right.Left = Node (25)
        self.root.Left.Right.Left.Parent = self.root.Left.Right
        self.root.Left.Right.Left.Right = Node (27)
        self.root.Left.Right.Left.Right.Parent = self.root.Left.Right.Left
        self.root.Left.Right.Right = Node (35)
        self.root.Left.Right.Right.Parent = self.root.Left.Right
        self.root.Right = Node (60)
        self.root.Right.Parent = self.root
        self.root.Right.Left = Node (50)
        self.root.Right.Left.Parent = self.root.Right
        self.root.Right.Left.Right = Node (55)
        self.root.Right.Left.Right.Parent = self.root.Right.Left
        self.root.Right.Right = Node (80)
        self.root.Right.Right.Parent = self.root.Right
        self.root.Right.Right.Right = Node (90)
        self.root.Right.Right.Right.Parent = self.root.Right.Right
        self.root.Right.Right.Right.Left = Node (85)
        self.root.Right.Right.Right.Left.Parent = self.root.Right.Right.Right
        # print 'set() - done'
        return self.root

    @staticmethod
    def printTree(root):
        if(root == None):
            return
        TreeQ.printTree(root.Left)
        print root.Data,
        TreeQ.printTree(root.Right)
        # print 'done'

    @staticmethod
    def printTreeInLevel(root):
        if(root == Node):
            return
        print
        queue = Queue()
        currLevel = 0
        item = (root, currLevel)
        queue.put(item)
        while(queue.empty() == False):
            # print queue.qsize(),
            item = queue.get()
            node = item[0]
            level = item[1]
            if(level <> currLevel):
                currLevel = level
                print
            print node.Data,
            if node.Left <> None:
                queue.put((node.Left, level + 1))
            if node.Right <> None:
                queue.put((node.Right, level + 1))


    @staticmethod
    def printTreeInLevel2(root):
        if(root == Node):
            return
        print
        queue = Queue()
        currLevel = 0
        item = (root, currLevel)
        queue.put(item)
        stack = []
        while(queue.empty() == False):
            # print queue.qsize(),
            item = queue.get()
            node = item[0]
            level = item[1]
            if(level <> currLevel):
                currLevel = level
                while len(stack) > 0:
                    queue.put(stack.pop())
                print
            print node.Data,
            if(currLevel %2 == 0):
                if node.Left <> None:
                    stack.append((node.Left, level + 1))
                if node.Right <> None:
                    stack.append((node.Right, level + 1))
            else:
                if node.Right <> None:
                    stack.append((node.Right, level + 1))
                if node.Left <> None:
                    stack.append((node.Left, level + 1))                
            if(queue.empty() == True):
                while len(stack) > 0:
                    queue.put(stack.pop())

treeQ = TreeQ();
root = treeQ.set()
# print root.Data
treeQ.printTree(root)
treeQ.printTreeInLevel(root)
treeQ.printTreeInLevel2(root)
