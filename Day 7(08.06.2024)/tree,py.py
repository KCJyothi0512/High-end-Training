class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    
    def fun(self,x):
        def fu(t,x):
            if  t==None:
                t=node(x)
                print(1)
            elif(x<t.data):
                l1.fun(t.left,x)
            else:
                l1.fun(t.right,x)
        t=self.root
        fu(t,x)
            
            
    def display(self):
        def dis(t):
            while(t!=None):
                dis(t.left)
                print(t.data)
                dis(t.right)
        t=self.root
        dis(t)

l1=tree()

l1.fun(5)
l1.fun(9)
l1.fun(2)
l1.fun(1)
l1.fun(8)
l1.fun(4)
l1.display()
