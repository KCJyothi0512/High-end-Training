class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x): #self cannot receive None
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def inorder(self,root):
        if root: # or if(root)
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def sumnodes(self,root):
        if root==None:
            return 0
        return root.data+self.sumnodes(root.left)+self.sumnodes(root.right) #preorder traversal sum
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0: 
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if root==None:
            return 0
        if root.data%2!=0: 
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def absolute_diff(self,root):
        if root==None:
            return 0
        if root.data%2==0: 
            return root.data+self.absolute_diff(root.left)+self.absolute_diff(root.right)
        else:
            return self.absolute_diff(root.left)+self.absolute_diff(root.right)-root.data
    def height(self,root): #height of None is -1
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balance(self,root):
        if root==None:
            return 0
        return abs(self.height(root.left)-self.height(root.right)) <= 1
    def leafnodecnt(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodecnt(root.left)+self.leafnodecnt(root.right)
    def leafnodesum(self,root): #search(log.n) # depth of particular node(with the help of search)
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.leafnodesum(root.left)+self.leafnodesum(root.right)
    def search(self,root,x):
        if root==None:
            return 'not found'
        if root.data==x:
            return 'found'
        if root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    def depth(self,root,x,c):
        if root==None:
            return -1
        if root.data==x:
            return c
        if root.data>x:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.left,x,c+1)
    def leftview(self,root,c,s):
        if root==None:
            return 0
        if c not in s:
            s.append(c)
            print(root.data,c)
        self.leftview(root.left,c+1,s)
        self.leftview(root.right,c+1,s)
    def rightview(self,root,c,a):
        if root==None:
            return 0
        if c not in a:
            a.append(c)
            print(root.data,c)
        self.rightview(root.right,c+1,a)
        self.rightview(root.left,c+1,a)
    def topview(self,root,c,d): # left subtree +, right -, curr>root update in dict
        if root==None:
            return 0
        if c not in d:
            d[c]=root.data
        if c>0:
            if d[c]<root.data:
                d[c]=root.data
        self.topview(root.left,c-1,d)
        self.topview(root.right,c+1,d)
        return d
t1=tree()
t1.root=node(10)          #10 5 15 2 7 11 20 3 21 22
t1.create(t1.root,5)
t1.create(t1.root,20) 
t1.create(t1.root,7)
t1.create(t1.root,1)
'''t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,6)
t1.create(t1.root,8)'''

#t1.root=t1.inorder(t1.root)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()
print(t1.sumnodes(t1.root)) #43
print(t1.sumnodes(t1.root.left)) #left subtree
print(t1.sumnodes(t1.root.left)-t1.sumnodes(t1.root.right)) #absolute difference
print(t1.evensum(t1.root))
print(t1.oddsum(t1.root))
print(abs(t1.absolute_diff(t1.root)))
print(t1.height(t1.root))
if t1.balance(t1.root):
    print('balance')
else:
    print('not balance')
print(t1.balance(t1.root))
print(t1.leafnodecnt(t1.root))
print(t1.leafnodesum(t1.root))
print(t1.search(t1.root,30))
print(t1.depth(t1.root,1,0))
#s=set()
t1.leftview(t1.root,0,[])
#a=set()
t1.rightview(t1.root,0,[])
d={}
t1.topview(t1.root,0,d)
for key in d:
    print(d[key])