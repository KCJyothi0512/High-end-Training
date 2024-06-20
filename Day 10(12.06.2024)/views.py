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
            
    def preorder(self,root):
        if (root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
             
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    
    
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    
    def topview(self,root):
        if root==None:
            return 
        d={}
        q=[(root,0)]
        while(len(q)!=0):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
                
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
                
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
        
                                                                                                                        
    def bottomview(self,root):
        if root==None:
            return 
        d={}
        q=[(root,0)]
        while(len(q)!=0):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
                
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
                
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
        
    
    def leftview(self,root,c,s):
        if root==None:
            return 0
        if c not in s:
            s.add(c)
            print(root.data,c)
        self.leftview(root.left,c+1,s)
        self.leftview(root.right,c+1,s)
            
    
    def rightview(self,root,c,s):
        if root==None:
            return 0
        if c not in s:
            s.add(c)
            print(root.data,c)
        self.rightview(root.right,c+1,s)
        self.rightview(root.left,c+1,s)
        
        
    

    
    
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)


t1.create(t1.root,15)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,11)

t1.create(t1.root,8)
t1.create(t1.root,9)



print("---INORDER TRAVERSAL-------")
t1.inorder(t1.root)
print()

print("---PRE-ORDER TRAVERSAL------")
t1.preorder(t1.root)
print()

print("---POST-ORDER TRAVERSAL------")
t1.postorder(t1.root)
print()

d={}
print()


print("---TOP VIEW------")
t1.topview(t1.root)
print()


print("---BOTTOM VIEW------")
t1.bottomview(t1.root)
print()

s=set()
print("---LEFT VIEW------")
t1.leftview(t1.root,0,s)

a=set()
print("---RIGHT VIEW------")
t1.rightview(t1.root,0,a)

