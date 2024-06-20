class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            '''self.tail.next=node(x) 
            self.tail.next.prev=self.tail
            self.tail=self.tail.next'''
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while t:
            print(t.data,end="->")
            t=t.next
        print()
    def rev_display(self):
        t=self.tail
        while t:
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        t1=self.tail
        while t!=t1 and t!=t1.next:
            if t.data==x or t1.data==x:
                return "found"
            t=t.next
            t1=t1.prev
        if t.data==x:
            return "found"
        return "not found"
    def length(self):
        t=self.head
        t1=self.tail
        while t!=t1:
            if t1.next==t:
                return 'even'
            t=t.next
            t1=t1.prev
        return 'odd' 
        '''while t!=t1 and t!=t1.next:
            t=t.next
            t1=t1.prev
        if t==t1:
            return "odd"
        else:
            return "even" '''
    def palindrome(self):
        t=self.head
        t1=self.tail
        while t!=t1 and t1!=t1.next:
            if t.data==t1.data:
                return 'palindrome'
            t=t.next
            t1=t1.prev
        return 'not palindrome'
    def join(self):
        t=self.head
        t1=self.tail
        '''while t!=t1.next:
            t=t.next
            t1=t1.prev
        t2=self.tail
        while t1!=None:
            t2.data,t1.data=t1.data,t2.data
            t1=t1.prev
            t2=t2.prev'''
        fast=self.head
        slow=self.head
        while fast!=None:
            fast=fast.next.next
            slow=slow.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.next=None
        slow.prev=None
        self.head=slow
        self.tail=t1
    '''def shift(self):
        t=self.head
        t3.head=None'''
    '''def balbrackets(self):
        l=[]
        c=0
        t=self.head
        flag=0
        while t!=None:
            if t.data=='[' or t.data=='{' or t.data=='(':
                l.append(t.data)
                t=t.next
                c+=1
            elif t.data==')' and l[-1]==')' or t.data=='{' and l[-1]=='}' or t.data=='[' and l[-1]==']':
                l.pop()
                c+=1
                t=t.next
            else:
                c+=1
                break
        if flag==0:
            print("-1")'''
    '''def parenthesis(self):
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
          print("-1")'''
    def sumdiff(self,t,es,os):  # 3 4 5 6 2 1   4 5 7 6 4 3 2 
        if t==None:
            return abs(es-os)
        if t.data%2==0:
            es=es+t.data
        else:
            os=os+t.data
        return self.sumdiff(t.next,es,os)
    def prime(self,t,c):
        if t==None:
            return c
        def primeornot(s,n,c1):
            if(s>(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return primeornot(s+1,n)
        if(pnt(2,t.data)):
            c+=1
        return self.prime(t.next,c)
l1=dll()
l1.addback(4)
#l1.addfront(10)
l1.addback(5)
l1.addback(7)
l1.addback(6)
l1.addback(4)
l1.addback(3)
l1.addback(2)
#l1.addfront(50)
l1.display()
l1.rev_display()
print(l1.search(5))
print(l1.length())
print(l1.palindrome())
#l1.join()
l1.display()
print(l1.sumdiff(l1.head,0,0))
print(l1.prime())