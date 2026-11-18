s1="z"
s2="Z"
print(s1>s2)
print(chr(50))


#Logical Operators
a=50
b=60
c=40
print(a>b and b>c)
print(a>b or b>c)
print(not c>b)

print(1==1.0)
print(1=='1')

#Assigning operators

x,y,z=[2,3,4]
print(x,y,z)
x,y,z=2,3,4
print(x,y,z)

x+=4
print(x)
d=4
print(--x)
print(id(z))
print(id(d))

#Identity operator
a=4
b=4
print(a is b)
print(z is d)

l1=[1,3,4]
l2=[1,3,4]
print(id(l1), id(l2))
print(l1 is l2)

#Operator Precedence
op1=2**3**2
print(op1) #Right to left
op2=5*2//3
print(op2)#left to right
