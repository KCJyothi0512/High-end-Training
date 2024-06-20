''' i/p: khoor
         3
    o/p: hello'''

s=input()
key=int(input())
c=key%26
d=''
for i in s:
    if((ord(i)-c) >= 97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)