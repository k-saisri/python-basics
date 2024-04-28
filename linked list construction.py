class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def insertAtEndOfTail(head,ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newBlock
    return head

def printlist(head):
    #below line of code is assigning head to curr variable
    curr=head
    
    #below line is checking whether curr reached to None
    while curr!=None:
        
        # here we are trying to print data in curr
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)    
