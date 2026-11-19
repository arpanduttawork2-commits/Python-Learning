#Method 1 with %
a='hello'
b='world'
c=4
d='%s %s %i'%(a,b,c)
print(d)
print(f"{c}")

#with format()

name="Arpan"
age=23
s="The name is {0} and the age is {1} and {1}".format(name, age) #can be used multiple times
print(s)

#using f-string
s=f"{name} is {age} years old"
print(s)