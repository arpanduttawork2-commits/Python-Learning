
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



