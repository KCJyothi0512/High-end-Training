'''i/p: 7262 sec     500 sec
   o/p: 2h:1m:2s     0h:8m:20s
'''
sec=int(input())
h=sec//3600
m=(sec%3600)//60
s=sec%60
print(f'{h}h:{m}m:{s}s')