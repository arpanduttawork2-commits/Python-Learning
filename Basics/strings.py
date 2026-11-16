s="a"
print(type(s))

s="helloworld"
for i in s:
    print(ord(i), chr(ord(i)))

#Indexing
print(s[0])
print(s[-2])
print(s[-len(s)])


#concatenation
s1="1"
s2="3"
s3=s1+3*s2
print(s3)
words=["hello", "world"]
s4=";".join(words)
print(s4)


