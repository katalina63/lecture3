print("Hello")
a = input("Enter value a: ")
b = input("Enter value b: ")
c = input("Enter value c: ")
a = int(a)
b = int(b)
c = int(c)

numerator = (a**2 + b**2) / ((3*b) - 4)
denominator = (4 * c**2) / 6

divis1 = int(numerator) // int(denominator)
print("division without remainder:") 
print(divis1)
divis2 = int(numerator) % int(denominator)
print("remainder of the division:" )
print(divis2)
