class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 
    def __len__(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
            if cur==self.head:
                break
        return count
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
        """assuming no duplicates."""
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
    def split_list(self):
        size=len(self)
        if size==0: return None
        if size==1: return self.head
        mid=size//2
        halfcount=0
        cur=self.head
        prev=None

        while halfcount<mid:
            halfcount+=1
            prev=cur
            cur=cur.next
        prev.next=self.head
        
        split_cllist=CircularLinkedList()
        while cur!=self.head:
            split_cllist.append(cur.data)
            cur=cur.next

        self.print_list()
        print('\n')
        split_cllist.print_list()
    def is_circular_linked_list(self, input_list):
        if not self.head:
            return False
        else:
            if self.head==self.head.next:
                return True
            else:
                cur=self.head
                while cur.next!=None:
                    if cur.next==self.head: return True
                    cur=cur.next
                return False

if __name__=='__main__':
    cllist = CircularLinkedList()
    cllist.append("A")
    cllist.append("B")
    cllist.append("C")
    cllist.append("D")
    cllist.append("E")
    #cllist.append("F")

    #cllist.split_list()
    #cllist.remove("A")
    #cllist.remove("C")
    #cllist.print_list()
    
    print(cllist.is_circular_linked_list(cllist))