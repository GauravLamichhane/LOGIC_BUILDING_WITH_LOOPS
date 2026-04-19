# 1. Print all numbers from 1 to 10.
# n = 1
# while True:
#     print(n)
#     n += 1
#     if n > 10:
#         break

# 2. Print the multiplication table of a given number.

# n = int(input("Enter the number: "))
# i = 1
# while True:
#     print(f"{n} * {i}:", n * i)
#     i += 1
#     if i > 10:
#         break
# 3. Keep taking numbers from the user until 0 is entered, then print the sum of all
# entered numbers.
# sum = 0
# while True:
#     n = int(input("Enter the number: "))
#     sum += n
#     if n == 0:
#         break
# print(sum)
# 4. Keep taking numbers from the user until 0 is entered, then print the largest number among all inputs
# largest = float("-inf")
# while True:
#     n = int(input("Enter the number"))
#     if n == 0:
#         break
#     if n > largest:
#         largest = n

# print(largest)
# 5. Count and print the number of digits in the given number.
# n = int(input("Enter the number"))
# n = abs(n)
# count = 0
# while True:
#     digit = n % 10
#     count += 1
#     n = n // 10
#     if n <= 0:
#         break
# print(count)

# 6. Reverse the given number and print the reversed value.
# n = int(input("Enter the number"))
# rev = 0
# while True:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
#     if n <= 0:
#         break
# print(rev)

# 7. Check whether the given number is a palindrome.
# n = int(input("Enter the number:"))
# original_n = n
# rev = 0
# while True:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
#     if n == 0:
#         break
# print("PAL" if original_n == rev else "Not")

# 8. Check whether the given number is an Armstrong number.
# n = int(input("Enter the number"))
# original_num = n
# len_n = len(str(n))
# num = 0
# while True:
#     digit = n % 10
#     num += digit**len_n
#     n = n // 10

#     if n <= 0:
#         break

# print("ARMSTRONG" if original_num == num else "NOT")

# 9. Calculate and print the factorial of the given number.

# n = int(input("Enter the number: "))
# fact = 1

# while True:
#     if n <= 1:
#         break
#     fact = fact * n
#     n -= 1
# print(fact)


# 10. Print the Fibonacci series up to the required number of terms.
# Fibonacci series is as 1, 2, 3, 5, 8, 13, 21
# n = int(input("Enter the number: "))
# a = 0
# b = 1
# next = b
# count = 0
# while True:
#     print(next, end=" ")
#     count += 1
#     a, b = b, next
#     next = a + b
#     if count == n:
#         break

# 11. Find the HCF (Highest Common Factor) of the given numbers.
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# result = float("-inf")
# while True:
#     result = a % b
#     a = b
#     b = result
#     if result == 0:
#         break
# print(a)
# 12. Create a menu-driven program that allows the user to choose and perform different
# operations.

# while True:
#     print("\n 1. Add")
#     print("\n 2. Multiply")
#     print("\n 3. Subtract")
#     print("\n 4. Division")
#     print("\n 5. Exit")
#     choice = int(input("Enter the choice: "))

#     if choice == 5:
#         break

#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))

#     if choice == 1:
#         print(a + b)
#     elif choice == 2:
#         print(a * b)
#     elif choice == 3:
#         print(a - b)
#     elif choice == 4:
#         print(a / b)
#     else:
#         print("Invalid choice")


# 13. Keep taking numbers from the user until a negative number is entered, then count
# how many positive numbers were entered.

# count = 0
# while True:
#     n = int(input("Enter the number: "))
#     if n < 0:
#         break
#     count += 1
# print(count)
# 14. Find and print the sum of digits of the given number.
# n = int(input("Enter the number: "))
# n = abs(n)
# sum = 0
# while True:
#     digit = n % 10
#     sum += digit
#     n = n // 10
#     if n <= 0:
#         break
# print(sum)
# 15. Calculate and print the sum of even digits and the sum of odd digits of the given numbers separately.

n = int(input("Enter the number: "))
n = abs(n)
odd_sum = 0
even_sum = 0
while True:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n = n // 10
    if n == 0:
        break
print(even_sum)
print(odd_sum)
