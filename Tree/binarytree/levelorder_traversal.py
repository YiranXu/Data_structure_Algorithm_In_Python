class Queue():
    def __init__(self) -> None:
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)
    def levelorder_print(self, start):
        """
        use queue structure. 
        put the root, then dequeue it, add its children, then dequeue the children one by one. 
        Whenever an element was dequeued, its children (if there are) will be added. 
        """
        if start:
            queue=Queue()
            queue.enqueue(start)
            result=[]
            while not queue.is_empty():
                pop=queue.dequeue()
                result.append(pop.value)
                if pop.left:
                    queue.enqueue(pop.left)
                if pop.right:
                    queue.enqueue(pop.right)
        else:
            return        
        return result

if __name__=='__main__':
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    a=tree.levelorder_print(tree.root)
    print(a)
        
