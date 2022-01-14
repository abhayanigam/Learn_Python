# Numeric Literals are immutable (unchangeable). 
# Numeric literals can belong to 3 different numerical 
# types: Integer, Float, and Complex.

a = 0b1010 # Binary Literal
b = 100 # Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

# Float literals
# 10.5 and 1.5e2 are floating-point literals.
#  1.5e2 is expressed with exponential and is equivalent to 1.5 * 102.
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a,b,c,d)
print(float_1,float_2)

# 3.14j in variable x. Then we use imaginary literal 
# (x.imag) and real literal (x.real) to create imaginary and 
# real parts of complex numbers.
print(x, x.imag, x.real)