title = "capiTalIze tHe titLe"
l=list()

s=title.split()
print(s)
for i in s:
    if len(i)>2:
        l.append(i.title())
        print(l)
    else:
        l.append(i.lower())
        print(l)
print(" ".join(l))