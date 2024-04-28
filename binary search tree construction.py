n=int(input())
nums=list(map(int,input().split()))

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertIntoBST(root,value):
    if root==None:
        newnode=TreeNode(value)
        return newnode

    if root.data>value:
        root.left=insertIntoBST(root.left,value)
    else:
        root.right=insertIntoBST(root.right,value)
    return root
def InOrder(root):
    if root==None:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right) 
root=None
for ele in nums:
    root=insertIntoBST(root,ele)

InOrder(root)

