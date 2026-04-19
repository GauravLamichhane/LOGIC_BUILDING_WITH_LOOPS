n = int(input("Enter the number: "))
odd_sum = 0
even_sum = 0
while True:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n = n // 10
    if n <= 0:
        break
print(even_sum)
print(odd_sum)
