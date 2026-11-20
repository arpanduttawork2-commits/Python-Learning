
start=-2
end=2
while start <= end:
    if start==0:
        start+=1
        continue
    print(10/start)
    start+=1   

i=list(range(0,10,2))
print(i)

for i in range(0,10):
    print(i,end=" ")
print()

s='hello  world'
for i in s.strip(' ').split(' '):
    print(i)
print( (s.strip(' ').split()))

s="kangareoo"

print(sum(list(s.count(c) for c in "aeiou")))
print(list(range(10,1,-1)))
print(list(range(0,10,5)))
s1="hello"
s2="hello"
print(type(s1),type(s2))
l1,l2=[1,2,3],[1,2,3]
print(id(l1), id(l2))
print(l1 is l2)
num=int(input())
print(sum(list(range(0,num+1))))
import math
num=int(input())
if(num>=0):
    if num ==0:
        print(1)
    else:
        print(math.prod(list(range(1,num+1))))
else: 
    print('Not possible')

#Nested

for i in range(1,11,):
    for j in range(1,6):
        print(f"{i}*{j}={i*j}", end=" ")
    print()


num=10
n=1
for i in range(0,num):
    print(str(n)*n, end=" ")
    print()
    n+=1
