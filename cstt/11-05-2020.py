
#QUESTION 1
'''
from collections import Counter

lst=list(map(int,input().split()))
d=Counter(lst)
print(dict(zip(d.values(),d.keys()))[1])
'''
#OUTPUT :
2 2 9 8 9 7 7
8
'''

#QUESTION 2
'''
lst=list(map(int,input().split()))
lst.sort()
s=99
for i in range(len(lst)-1):
    s=min(lst[i]^lst[i+1],s)
print(s)    

OUTPUT :
9 5 3
6

'''

#QUESTION 3
'''
n=int(input())
s=0
ini=0

while s < n:
    ini+=1
    s+=ini
    
if s > n: print(ini-1)
if s == n : print(ini)

##OUTPUT :
10
4

12
4

16
5

15
5
'''

#QUESTION 5
'''
n=int(input())
def squ_root(n):
    return int(n**0.5)

print(squ_root(n))

##OUTPUT :
5
25

27
5
'''
