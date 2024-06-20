class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if (root==None):
            return node(x)
        elif (root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
             
            
    def inorder(self,root):
        if (root):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)



    def isBalanced(self, root):
        def heightoftree(root):
            if root==None:
                return -1
            return abs(heightoftree(root.left)-heightoftree(root.right))
        if root==None:
            return True
        
        t=heightoftree(root)
        
        if t==1 or t==0:
            print(t)
            return True
        else:
            print(t)
            return False
        
        def heightoftree(root):
            if root==None:
                return -1
            return abs(heightoftree(root.left)-heightoftree(root.right))
        
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)


t1.create(t1.root,20)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,6)
t1.create(t1.root,8)
t1.create(t1.root,9)

print("---INORDER TRAVERSAL-------")
t1.inorder(t1.root)
print()

print(t1.isBalanced(t1.root))