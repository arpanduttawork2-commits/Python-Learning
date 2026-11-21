l1=[1,2,3]
print(l1)
l1=["Arpan", 23, 'Dutta',l1]
print(l1)
print(l1[len(l1)-2][::-1]) #Slicing

#Concatenation

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
print(l1*3)


#Membership
l1=[4,2,3,[1,3,0]]
print(1 in l1)
print(1 in l1[len(l1)-1])

#Iterable
for i in l1[0:len(l1)-1]:
    print(i, end="...")
print(l1[len(l1)-1])


#Basic List Functions

l1=[1,2,4,[9,9,9]]
#print(max(l1))

