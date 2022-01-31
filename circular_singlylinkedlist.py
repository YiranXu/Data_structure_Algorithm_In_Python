class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 
    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
            
    def prepend(self, data):
        """
        make it the head of the linked list
        """
        new=Node(data)
        new.next=self.head
        if not self.head:
            self.head.next=self.head
        else:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=new 
        self.head=new

    def append(self, data):
        """
        insert new node after the node that was previously pointing to the head
        """
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else:
            new=Node(data)
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=new
            new.next=self.head
    def remove(self,key):
        if not self.head: return
        else:
            cur=self.head
            prev=None
            if self.head.data==key:
                while cur.next!=self.head:
                    cur=cur.next
                cur.next=self.head.next
                if self.head==self.head.next:
                    self.head=None
                else:
                    self.head=cur.next
            else:
                while cur:
                    prev=cur
                    cur=cur.next
                    if cur.data==key:
                        prev.next=cur.next
                        cur=cur.next 
                    if cur.next==self.head:
                        break
                return

if __name__=='__main__':
    cllist = CircularLinkedList()
    cllist.append("A")
    cllist.append("B")
    cllist.append("C")
    cllist.append("A")
    cllist.append("D")

    cllist.remove("A")
    cllist.remove("C")
    cllist.print_list()