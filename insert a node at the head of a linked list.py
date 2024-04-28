# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    newNode = SinglyLinkedListNode(data)
    if llist == None:
        return newNode
    newNode.next = llist
    return newNode
