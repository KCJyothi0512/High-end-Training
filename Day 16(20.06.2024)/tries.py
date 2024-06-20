class node:       #application - autocorrect  #delete word
    def __init__(self):
        self.d={}
        self.flag=0
        #self.d1={} for count
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        if(t.flag==1):
            return True
        return False
    def search_prefix(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return True
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=''
        for i in str:
            if(i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def longest_prefix(self):
        def fun(t, s):
            if t.flag == 1:
                prefix_list.append(s)
            for i in t.d:
                fun(t.d[i], s + i)

        prefix_list = []
        fun(self.root, "")
        return max(prefix_list, key=len)

t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split() #a-num, s- string
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search(s))
    if(a=='3'):
        print(t1.search_prefix(s))
    if(a=='4'):
        t1.print_all_prefix(s)
    if a =='5':
        t1.print_all_prefix(s)
        print("Longest prefix:", t1.longest_prefix())
'''t1.insert("world")
t1.insert("word")
t1.insert("apple")
t1.insert("woo")
t1.insert("wo")
t1.insert("w")
print(t1.search("word"))
print(t1.search_prefix("wor"))'''
'''
print all prefix input  
7
1 word
1 words
1 worlds
1 wor
1 apple
1 wood
4 wor                              
'''