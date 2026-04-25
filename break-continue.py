# 1. Print numbers from 1 to 100, and stop the loop as soon as a number divisible by 17 is encountered.

# for i in range(1, 101):
#     print(i)
#     if i % 17 == 0:
#         break

# 2. Print numbers from 1 to 100, but skip all numbers that are divisible by 5 and continue printing the rest.

# for i in range(1, 101):
#     if i % 5 == 0:
#         continue
#     print(i)

# 3. Take 5 numbers as input, skip any number that is 0 using continue, and calculate the sum of the remaining numbers.
# i = 0
# summ = 0
# while i < 5:
#     n = int(input("Enter the number: "))
#     i += 1
#     if n == 0:
#         continue
#     summ += n

# print(summ)

# 4. Search for a specific number in a list of inputs, and terminate the loop immediately when the number is found.

# n = [1, 2, 3, 4, 5]
# target = int(input("Enter the target: "))
# for num in n:
#     if target == num:
#         print(f"{target} found.")
#         break

# 5. Keep taking numbers from the user and print them until a negative number appears, then stop the loop.

# while True:
#     n = int(input("Enter the number: "))
#     if n < 0:
#         break
#     print(n)

# 6. Skip all odd numbers and print only the even numbers.
# while True:
#     n = int(input("Enter the number: "))
#     if n == -1:
#         break
#     if n % 2 != 0:
#         continue
#     print(n)

# 7. Continuously add numbers in a loop and stop the loop when the sum becomes greater than 100

summ = 0
while True:
    n = int(input("Enter the number: "))
    summ += n
    print(f"Current SUM:{summ}")
    if summ > 100:
        break
print(summ)
