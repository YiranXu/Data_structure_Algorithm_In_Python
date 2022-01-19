class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        """
        insert an element at the end of the linked list
        """
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    def swap_nodes1(self,key1,key2):
        if key1==key2: return
        cur=self.head
        node1=None
        node2=None 
        prev1=None
        prev2=None
        prev=None
        while cur:
            if cur.data==key1:
                node1=cur
                prev1=prev
            if cur.data==key2:
                node2=cur 
                prev2=prev
            prev=cur
            cur=cur.next
        if not node1 or not node2: return

        if prev1 is None: #node1 is head
            self.head=node2
        else:#node1 is not head
            prev1.next=node2
        if prev2 is None: #node2 is head
            self.head=node1 
        else: #node2 is not head
            prev2.next=node1
        node1.next,node2.next=node2.next,node1.next
    
    def swap_nodes2(self,key1,key2):
        if key1==key2:return
        prev1=None
        curr_1=self.head
        while curr_1 and curr_1.data!=key1:
            prev1=curr_1
            curr_1=curr_1.next
        prev2=None
        curr_2=self.head
        while curr_2 and curr_2.data!=key2:
            prev2=curr_2
            curr_2=curr_2.next
        if not curr_1 or not curr_2: return
        if prev1:
            prev1.next=curr_2
        else:
            self.head=curr_2
        if prev2:
            prev2.next=curr_2
        else:
            self.head=curr_1
        curr_1.next,curr_2.next=curr_1.next,curr_2.next

    def merge_sorted(self,l2):
        """
        merge two sorted linked list
        """           
        p=self.head
        q=l2.head
        prev=None
        if not p:
            return q
        if not q:
            return p
        while p and q:
            if p.data<=q.data:
                if prev:
                    prev.next=p
                prev=p
                p=p.next
            else:
                if prev:
                    prev.next=q
                prev=q
                q=q.next
        #one of the list has been finished
        if not p:
            prev.next=q
        if not q:
            prev.next=p
        #new head            
        if self.head.data>l2.head.data:
            self.head=l2.head

if __name__ == "__main__":
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.append(2)
    llist_1.append(5)
    llist_1.append(7)
    llist_1.append(9)
    llist_1.append(10)

    llist_2.append(1)
    llist_2.append(3)
    llist_2.append(4)
    llist_2.append(6)
    llist_2.append(8)

    llist_1.merge_sorted(llist_2)
    llist_1.print_list()

    #llist.swap_nodes1('C','A')
    #print(llist.print_list())
