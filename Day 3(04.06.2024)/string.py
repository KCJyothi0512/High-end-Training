'''
ip:         
   khoor      bcdmnwc              bvec
   3          9                    4
op:           op:
  hello          student           xray
'''

s=input()
k=int(input())
n=k%26
d=''
for i in s:
    if (ord(i)-n>=97 ):
        d=d+(chr(ord(i)-n))
    else:
        d=d+(chr(ord(i)-n+26))
print(d)          
              
       
       

    