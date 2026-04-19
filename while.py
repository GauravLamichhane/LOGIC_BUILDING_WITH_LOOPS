# n = int(input("Enter the number: "))
# i = 2
# summ = 0
# while i <= n:
#     if i % 2 == 0:
#         summ += i
#     i += 2
# print(summ)

# n = int(input("Enter the number: "))

# print(n * (n + 1) // 2)

# n = int(input("Enter the number: "))
# i = 1
# summ = 0
# while i <= n:
#     summ += i
#     i += 2
# print(summ)

# n = int(input("Enter the number: "))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1

# print(fact)

# 10. Find and print the product of all digits of a given number.
# n = int(input("Enter the number: "))
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n = n // 10

# print("Product of digits", product)

# 11. Find and print the product of all digits of a given number.

# n = int(input("Enter the number: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1

# print("Count is as:", count)

# 12. Reverse the given number and print the reversed value.

# n = int(input("Enter the number:"))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print(rev)

# 13. Check whether the given number is a palindrome.
# n = int(input("Enter the number:"))
# rev = 0
# original = n
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev)
# if rev == original:
#     print("palindrome")
# else:
#     print("not")

# 14. Find and print the sum of digits of the given number.
# n = int(input("Enter the number:"))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10
# print(sum)

# 15. Check whether the given number is an Armstrong number.

# n = int(input("Enter the number: "))
# original = n
# arm = 0
# digits = len(str(n))
# while n > 0:
#     digit = n % 10
#     arm += digit**digits
#     n = n // 10

# if original == arm:
#     print("Armstrong")
# else:
#     print("Not")

# 16. Check whether the given number is a Perfect number.

# n = int(input("Enter the number: "))
# sum = 0
# i = 1
# while i < n:
#     if n % i == 0:
#         sum += i
#     i += 1

# if sum == n:
#     print("Perfect number")
# else:
#     print("Not perfect number")

# 17. Print all prime numbers between 1 and 100.
# n = 2
# count = 0
# while n < 100:
#     if n == 2:
#         print(f"{n} is prime number")
#     if n % 2 != 0:
#         print(f"{n} is a prime number")
#     n += 1
#     count += 1

# print(f"{count}")

# 19. Print the Fibonacci series up to n terms.


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

# 21. Print the square of each number from 1 to n.

# n = int(input("Enter the number:"))
# i = 1
# while i <= n:
#     print(f"Square of {i}: {i * i}")
#     i += 1

# 23. Print all numbers between a and b that are divisible by 7.
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# i = a
# while i <= b:
#     if i % 7 == 0:
#         print(f"{i}")
#     i += 1

# Finding the factorial of a number
# n = int(input("Enter the number: "))
# i = 2 can be 1 also 2 because anything mul by 1 is that same no
# ans = 1
# while i <= n:
#     ans *= i
#     i += 1

# print(ans)

# 24. Print all factors of the given number.
# n = int(input("Enter the number: "))
# i = 1
# summ = 0
# while i <= n:
#     if n % i == 0:
#         summ += i
#         print(f"{i} is the factor of {n}")
#     i += 1
# print("Sum:", summ)

# 26. Find the HCF (Highest Common Factor) of two given numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# op = 0
# while b > 0:
#     op = a % b
#     a = b
#     b = op
# print("HCF:", a)

# 27. Find the LCM (Least Common Multiple) of two given numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# p = a * b
# temp_a, temp_b = a, b
# while temp_b > 0:
#     op = temp_a % temp_b
#     temp_a = temp_b
#     temp_b = op
# hcf = temp_a
# print("HCF:", hcf)
# print("LCM:", p / temp_a)

# 28. Find the smallest digit in the given number.
# n = int(input("Enter the number: "))
# smallest = 9
# while n > 0:
#     digit = n % 10
#     if digit < smallest:
#         smallest = digit
#     n = n // 10

# print(smallest)

# print(9 // 10)

# 29. Find the largest digit in the given number.
n = int(input("Enter the number: "))
largest = 1
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print(largest)
