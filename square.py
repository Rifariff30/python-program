result = []
for num in range(1000, 10000):
    digits = str(num)
    if all(int(d) % 2 == 0 for d in digits):
        if int(num ** 0.5) ** 2 == num:
            result.append(num)
print(result)