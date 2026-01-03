a = int(input("Enter A: "))
b = int(input("Enter B: "))
while b != 0:
 a, b = b, a % b
 print(a)
