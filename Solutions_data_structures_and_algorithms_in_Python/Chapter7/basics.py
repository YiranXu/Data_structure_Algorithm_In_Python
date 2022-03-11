
class SinglyLinkedList:
    class _Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    def __init__(self):
        self.head=None
        self._size=0
        
    def __len__(self):
        """Return the number of elements in the list"""
        return self._size
    def createLinkedList(self,arr):
        self.head = None
        tempHead = self.head
        for v in arr:
            if self.head == None:
                self.head =self._Node(v)
                tempHead = self.head
            else:
                self.head.next = self._Node(v)
                self.head = self.head.next
            self._size+=1
        self.head=tempHead
        return self
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    