'''i/p: placements
   o/p: plAcEmEnts
   ----------------
   i/p: school
   o/p: schOOl
'''
str=input()
s=''
for i in str:
    if i in 'aeiou'or i in 'AEIOU':
        i=i.upper()
        s=s+i
    else:
        i=i.lower()
        s=s+i
print(s)
