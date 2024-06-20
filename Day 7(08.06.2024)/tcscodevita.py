'''
ip:
school
3
L 2
R 3
L 1
op:
Yes

hoc
sub-sequencses from "school"-->sch,cho,hoo,ool

'''

'''s=input()
k=int(input())
l=[]
num=[]
for i in range(k):
    l.append(input())
for item in l:
    num.append(int(item[1:]))
print(num)

s1=''
for i in num:
    s1=s1+s[i]
print(s1)


l1=[]
for i in range(len(s)-2):
    l1.append(s[i:i+k])
print(l1)

l1.sort()
print(l1)

s1=''.join(sorted(s1))
print(s1)

if s1 in l1:
    print("YES")
else:
    print("NO")'''

a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if (b[0]=='L'):
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
#print(str)
str=list(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    #t.sort()
    b.append(t)
print(b)
print(str)
for i in b:
    if i==str:
        print('yes')
        break
else:
    print('no')