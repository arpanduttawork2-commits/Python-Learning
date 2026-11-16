#Dynamic data types. Can be changed
import sys
a="hello ksadhfknkij  sdfnlnnsdf"
print(sys.getsizeof(a))
print(a, type(a))
a=100
print(a)

#int and float

a=10
b=100.2
print(type(a), type(b))
print(f"djjf {b:.2f}")
print(sys.getsizeof(b))

#complex
c=3+9j
print(c, type(c))
print(f"Real {c.real:.2f} Imaginary {c.imag:.2f}")

#Boolean 
b=True
b=False

comp1= 3>5
print(comp1)