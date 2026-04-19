n = int(input("Enter the number"))
a = 0
b = 1
next = b
sum = 0
count = 1
while count <= n:
    print(next, end=" ")
    sum += next
    count += 1
    a, b = b, next
    next = a + b
print(f"\nSum: {sum}")