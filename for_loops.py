# 1. Print all numbers from 1 to 10.
# for i in range(1, 11):
#     print(i)

# 2. Print numbers from 10 down to 1 in reverse order.
# for i in range(10, 0, -1):
#     print(i)

# 3. Print all even numbers between 1 and 100.
# for i in range(2, 101, 2):
#     print(i)
# 4. Print all odd numbers between 1 and 100
# for i in range(1, 101, 2):
#     print(i)

# 5. Print the multiplication table of a given no.

# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# 6. Calculate and print the factorial of a given number.
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# 7. Calculate and print the factorial of every number from 1 to n.
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
#     print(f"Factorial of {i}:", fact)

# 8. Print all prime numbers between 1 and 100.
# n = int(input("Enter the number: "))
# for i in range(2, n + 1):
#     is_prime = True
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(i)


# 9. Check whether the given number is  a prime number.
# n = int(input("Enter the number: "))
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if n < 2:
#     print("not prime")
# elif is_prime:
#     print("PRIME")
# else:
#     print("Not Prime")

# 10. Print the Fibonacci series up to the required number of terms.
# n = int(input("Enter the number: "))
# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     a, b = b, a + b

# 11. Find and print the sum of the Fibonacci series.

# 10. Print the Fibonacci series up to the required number of terms.
# n = int(input("Enter the number: "))
# a = 0
# b = 1
# sum_n = 0
# for i in range(n):
#     print(a)
#     sum_n += a
#     a, b = b, a + b

# print(f"SUM: {sum_n}")

# 12. Print all factors of the given number.

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(f"{i} is one of the factor of {n}")


# 13. Find and print the sum of all factors of the given number.

# n = int(input("Enter the number: "))
# sum_n = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         sum_n += i
#         print(f"{i} is one of the factor of {n}")

# print(sum_n)

# 14. Find the HCF (Highest Common Factor) of the given numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# hcf = 1
# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         hcf = i

# print(hcf)

# optimized
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# hcf = 1
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         hcf = i
#         break

# print(hcf)

# 15. Find the LCM (Least Common Multiple) of the given numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# hcf = 1
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         hcf = i
#         break

# print(hcf)
# print(a * b / hcf)

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# lcm = max(a, b)
# for i in range(max(a, b), a * b + 1):
#     if i % a == 0 and i % b == 0:
#         lcm = i
#         break

# print(lcm)

# 16. Print the square of each number from 1 to n.
# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     print(i * i)

# 17. Print the cube of each number from 1 to n.

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     print(i**3)


# 18. Print all numbers between a and b that are divisible by 7.

# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# for i in range(a, b + 1):
#     if i % 7 == 0:
#         print(i)

# 19. Find and print the sum of the first n natural numbers.

# n = int(input("Enter the number: "))
# summ = 0
# for i in range(1, n + 1):
#     summ += i

# print(summ)
# 20. Find and print the sum of all even numbers from 1 up to n.

# n = int(input("Enter the number: "))
# summ = 0
# for i in range(2, n + 1, 2):
#     summ += i

# print(summ)
# 21. Find and print the sum of all odd numbers from 1 up to n.
