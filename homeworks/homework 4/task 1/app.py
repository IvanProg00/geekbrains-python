list_1_size = int(input("Enter the size of the first array: "))
list_2_size = int(input("Enter the size of the second array: "))

list_1 = []
for i in range(list_1_size):
    num = int(input("Enter the number for the first array: "))
    list_1.append(num)

list_2 = []
for i in range(list_2_size):
    num = int(input("Enter the number for the second array: "))
    list_2.append(num)

s = set(list_1)
s.update(list_2)

res = list(s)
res.sort()

print(f"Result: {res}")
