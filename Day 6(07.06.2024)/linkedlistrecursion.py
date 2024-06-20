'''
ip:
  3 4 5 6 2 1 8 7
  op:
  return differnce of evensum and oddsum
  4+6+2+8=20
  3+5+1+7=16
  |evensum-oddsum|
'''

'''
  ip:"(([{}]))"
  op:-1 if balanced
  return position if it is not balanced return position
  
  ip:"[()]()"
  op:-1
'''

class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.nxt=node(x)
            self.tail.nxt.prev=self.tail
            self.tail=self.tail.nxt
            
            '''we can write this too
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt'''
    

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def diff(self,t,esum,osum):
        if t==None:
            return abs(esum-osum)

        if t.data%2==0:
            esum=esum+t.data
        else:
            osum=osum+t.data
        return self.diff(t.nxt,esum,osum)
       
        
        
            
l1=dll()
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.addback(6)
l1.addback(2)
l1.addback(1)
l1.addback(8)
l1.addback(7)

l1.display()
print(l1.diff(l1.head,0,0))









