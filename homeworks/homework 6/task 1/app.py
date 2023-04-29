first_num = int(input("Enter the first number of array: "))
diff = int(input("Enter the difference: "))
size = int(input("Enter the number of elements: "))

res = []

for i in range(1, size+1):
    res.append(first_num + (i - 1) * diff)

print(res)
