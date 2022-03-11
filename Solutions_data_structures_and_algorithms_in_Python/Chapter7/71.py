#Give an algorithm for finding the second-to-last node in a singly linked
#list in which the last node is indicated by a next reference of None. 
import basics
def second_to_last(ll):
    if len(ll)<=1:
        return None
    s=ll.head
    f=s.next
    while f.next:
        f=f.next
        s=s.next
    return s
if __name__ == "__main__":
    ll1 = basics.SinglyLinkedList()
    ll1=ll1.createLinkedList([1, 2, 8, 9, 12, 16])
    output=second_to_last(ll1)
    print(output.data if output else False)