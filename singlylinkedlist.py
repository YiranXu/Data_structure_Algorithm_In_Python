from locale import currency


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
    def len_recursive(self,node):
        """
        to get the length of the whole list, head needs to be passed as the parameter
        """
        #base case: empty list
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)
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

    def remove_duplicates(self):
        unique=set()
        cur=self.head
        prev=None
        while cur: 
            if cur.data in unique:
                prev.next=cur.next 
                cur=None #set it to none for better garbage collection
            else:
                unique.add(cur.data) 
                prev=cur 
            cur=prev.next 
    def print_nth_from_last(self,n):
        total_length=self.len_recursive(self.head)
        index=total_length+1-n
        count=1
        cur=self.head
        while cur and count<index:
            cur=cur.next
            count+=1
        if cur is None:
            return
        else:
            print(cur.data)
            return cur.data
    def print_nth_from_last2(self, n):
        total_len = self.len_recursive(self.head)
  
        cur = self.head 
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
             return   
    def print_nth_from_last3(self,n):
        p=self.head
        q=self.head
        if n>0:
            count=0
            while q:
                count+=1
                if count==n:
                    break
                q=q.next
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return
            while p and q.next:
                p=p.next
                q=q.next
            return p.data
        else: 
            return None 
    def count_occurences_iterative(self,data):
        cur=self.head
        count=0
        while cur:
            if cur.data==data:
                count+=1
            cur=cur.next
        return count   

    def count_occurences_recursive(self,node,data):
        if not node:
            return 0
        if node.data==data:
            return 1+self.count_occurences_recursive(node.next,data)
        else:
            return self.count_occurences_recursive(node.next,data)
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.append(6)

    llist_2 = LinkedList()
    llist_2.append(1)
    llist_2.append(2)
    llist_2.append(1)
    llist_2.append(3)
    llist_2.append(1)
    llist_2.append(4)
    llist_2.append(1)
    print(llist_2.count_occurences_iterative(1))
    print(llist_2.count_occurences_recursive(llist_2.head, 1))
    #print(llist.print_nth_from_last3(2))
    #print("Linked List After Removing Duplicates")
    #llist.remove_duplicates()
    #llist.print_list()
    
    #llist_1 = LinkedList()
    #llist_2 = LinkedList()

    #llist_1.append(2)
    #llist_1.append(5)
    #llist_1.append(7)
    #llist_1.append(9)
    #llist_1.append(10)

    # llist_2.append(1)
    # llist_2.append(3)
    # llist_2.append(4)
    # llist_2.append(6)
    # llist_2.append(8)

    # llist_1.merge_sorted(llist_2)
    # llist_1.print_list()

    #llist.swap_nodes1('C','A')
    #print(llist.print_list())
