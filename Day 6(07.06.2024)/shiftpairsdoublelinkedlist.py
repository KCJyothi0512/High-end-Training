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
    
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.head.prev=node(x)
            self.head.prev.nxt=self.head
            self.head=self.head.prev
            
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.nxt
        print()
        
    def shift(self):
        t=self.head
        t1=t.nxt
        t3=None
        while(t!=None):
            if t==self.head:
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t3
                t.prev=t1
                
                self.head=t1
                #print(t.data,t1.data)
                t,t1=t1,t
                #print(t.data,t1.data)
                t3=t1
                
                if(t1.nxt==None):
                    break
                t=t.nxt.nxt
                t1=t1.nxt.nxt
                
            else:
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t3
                t.prev=t1
                t3.nxt=t1
                #print(t.data,t1.data)
                t,t1=t1,t
                #print(t.data,t1.data)
                t3=t1
                
                if(t1.nxt==None):
                    break
                t=t.nxt.nxt
                t1=t1.nxt.nxt
                
                #l1.display()
        
              
                        
l1=dll()        

#l1.head=node(5)
#l1.tail=l1.head
'''l1.addfront(1)
l1.addfront(2)
l1.addfront(3)
l1.addfront(4)
l1.addfront(1)
#l1.addfront(1)
#l1.addfront(67)'''



l1.addback(5)
l1.addback(7)
l1.addback(8)
l1.addback(2)
l1.addback(1)
l1.addback(4)


l1.display()
l1.shift()
l1.display()




