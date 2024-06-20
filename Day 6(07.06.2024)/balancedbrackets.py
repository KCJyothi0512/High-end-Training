'''a=input()
s=[]
f=0
c=0
for i in a:
    if i in '{[(':
        s.append(i)
    elif not s:
        if i=='}' and s[-1]=='{' or i==']' and s[-1]=='[' or i==')' and s[-1]=='(':
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break'''
  
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
        
    def parenthesis(self):
        l=[]
        c=0
        t=self.head
        flag=0
        while t!=None:
            if t.data in '{[(':
                l.append(t.data)
                t=t.nxt
                c=c+1
            elif l:
                if (t.data==')' and l[-1]=='(') or (t.data==']' and l[-1]=='[') or (t.data=='}' and l[-1]=='{'):
                    l.pop()
                    t=t.nxt
                    c=c+1
                else:
                    print(c+1)
                    flag=1
                    break
                    
            else:
                print(c)
                flag=1
                break
            
            
        if flag==0:
            print("-1")
            
            
l1=dll()
s=input()
for i in range(len(s)):
    l1.addback(s[i])


l1.display()
l1.parenthesis()        