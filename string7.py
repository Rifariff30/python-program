s = input("Enter string: ")
ch = s[0]
result = ch + s[1:].replace(ch, '$')
print(result)