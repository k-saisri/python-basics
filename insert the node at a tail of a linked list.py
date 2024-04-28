# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    newnode=SinglyLinkedListNode(data)
    if head==None:
        return newnode
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=newnode
    return head
