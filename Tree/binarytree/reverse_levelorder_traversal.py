from unittest import result
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

class Stack():
    def __init__(self) -> None:
        self.items=[]
    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def __len__(self):
        return len(self.items)
class Node():
    def __init__(self, value) -> None:
        self.value=value
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self,root) -> None:
        self.root=Node(root)
    def reverse_level_order_traversal(self,start):
        """
        Use queue to traverse the tree from top to bottom like what we do in regular BFS
        Use a stack to store visited nodes so we can reverse the order
        P.S it is also possible to do the regular level order traversal, and reverse the result list
        """
        if start:
            result=[]
            queue=Queue()
            queue.enqueue(start)
            stack=Stack()
            while not queue.is_empty():
                cur=queue.dequeue()
                stack.push(cur)
                if cur.right:
                    queue.enqueue(cur.right)
                if cur.left:
                    queue.enqueue(cur.left)

            while len(stack)>0:
                cur=stack.pop()
                result.append(cur.value)
            return result
        else:
            return 

if __name__=='__main__':
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    a=tree.reverse_level_order_traversal(tree.root)
    print(a)

