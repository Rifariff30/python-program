list1 = input("Enter list1: ").split(',')
list2 = input("Enter list2: ").split(',')
for color in list1:
 if color not in list2:
  print(color)