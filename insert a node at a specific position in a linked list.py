# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    newnode=SinglyLinkedListNode(data)
    if position==1:
        newnode.next=head
        return newnode
    index=1
    cur=llist
    while index!=position:
        cur=cur.next
        index+=1
    newnode.next=cur.next
    cur.next=newnode
    return llist
