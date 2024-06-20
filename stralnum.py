a='f46feLK9y56u#@&56hIjbn6KJhA'
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if i in 'AEIOU':
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()):
        s=s+1
print('Uppercase vowels: ',uv)
print('Uppercase consonants: ',uc)
print('Lowercase vowels: ',lv)
print('Digits: ',d)
print('Special characters: ',s)