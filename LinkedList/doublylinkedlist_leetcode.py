#https://leetcode-cn.com/leetbook/read/linked-list/jy291/
#https://leetcode.com/problems/design-linked-list/
"""
在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/linked-list/jy291/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.prev,self.next=None,None

class MyLinkedList:
    #doubly linked list
    def __init__(self):
        self.head=None
        # sentinel nodes as pseudo-head and pseudo-tail
        # self.head,self.tail=Node(0),Node(0)
        # self.head.next=self.tail
        # self.tail.prev=self.head
        # self.size=0
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        else:
            if index+1<self.size-index: #faster to get from the head
                cur=self.head
                for _ in range(index+1):
                    cur=cur.next
            else:
                cur=self.tail
                for _ in range(self.size-index):
                    cur=cur.prev
            return cur.data
        # cur=self.head
        # pos=0
        # while cur:
        #     if pos==index:
        #         return cur
        #     cur=cur.next
        #     pos+=1
        # return -1

    def addAtHead(self, val: int) -> None:
        new=Node(val)
        if not self.head:
            self.head=new
        else:
           self.head.prev=new
           new.next=self.head
           self.head=new 

    def addAtTail(self, val: int) -> None:
        new=Node(val)
        if not self.head:
            self.head=new
        else:
            #find tail
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur

    def addAtIndex(self, index: int, val: int) -> None:
        if index<=0:#在头部插入节点
            self.addAtHead(val)
        else:
            new=Node(val)
            cur=self.head
            pos=0
            while cur:
                if pos==index:
                    new.next=cur
                    cur.prev.next=new
                    new.prev=cur.prev
                    cur.prev=new
                    return 
                cur=cur.next
                pos+=1
            if pos+1==index:
                cur.next=new
                new.prev=cur
            
    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=None

        elif index>0:
            cur=self.head
            pos=0
            while cur:
                if pos==index:
                    cur.prev.next=cur.next
                    cur.next.prev=cur.prev
                    cur=None 
                    return
                cur=cur.next
                pos+=1
if __name__=='__main__':
    linkedList =MyLinkedList();
    linkedList.addAtHead(1);
    #linkedList.addAtTail(3);
    #linkedList.addAtIndex(1,2);   #链表变为1-> 2-> 3
    #linkedList.get(1);            #返回2
    linkedList.deleteAtIndex(0);  #现在链表是1-> 3
    linkedList.get(1);            #返回3

