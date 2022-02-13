class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation
    """
    class _Node:
        __slots__='_element','_prev','_next'
        def __init__(self,element,prev,next):
            self._element=element
            self._prev=prev
            self._next=next
    def __init__(self):
        self._header=self._Node(None,None,None)
        self._trailer=self._Node(None,None,None)
        self._header._next=self._trailer
        self._trailer._prev=self._header
        self._size=0
    def __len__(self):
        """Return the number of elements in the list"""
        return self._size
    def is_empty(self):
        return self.__size==0
    def print_list(self):
        
        cur = self._header
        while cur:
            print(cur._element)
            cur = cur._next
    
    def _insert_between(self,e,predecessor,successor):
        """
        Add element e between two existing nodes and return new node
        """
        newest=self._Node(e,predecessor,successor)
        predecessor._next=newest
        successor._prev=newest
        self._size+=1
        return newest
    def _delete_node(self,node):
        """
        delete nondummy node from the list and return its element
        """
        node._prev._next=node._next
        node.next._prev=node._prev
        self._size-=1
        element=node.element
        node._prev=node._next=node._element=None #deprecate node
        return element
    def _append(self,e):
        return self._insert_between(e,self._trailer._prev,self._trailer)
    def reverse(self):
        cur=self._header
        while cur:
            #temp=cur._prev
            cur._prev,cur._next=cur._next,cur._prev
            cur=cur._prev
        self._trailer,self._header=self._header,self._trailer
        
    
if __name__ == "__main__":
    dllist = _DoublyLinkedBase()
    dllist._append(1)
    dllist._append(2)
    #dllist._append(3)
    #dllist._append(4)
    dllist.print_list()

    dllist.reverse()
    print("reverse")
    dllist.print_list()