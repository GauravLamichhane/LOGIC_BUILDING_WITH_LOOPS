# 1. Print the multiplication tables for all numbers from 1 to 10.

# for i in range(1, 10 + 1):
#     for j in range(1, 10 + 1):
#         print(f"{i} x {j} = {i*j}")
#     print("\n")

# 2. Print all possible pairs (i, j) where both i and j range from 1 to n.

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print((i, j))
# 3. For every number from 1 to n, count and print the total number of its factors.

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     fact_num = 0
#     for j in range(1, n + 1):
#         if i % j == 0:
#             fact_num += 1
#     print(f"Factors of {i}: {fact_num}")

# 4. Print all prime numbers up to n using nested loop checking.

# n = int(input("Enter the number: "))
# for i in range(2, n + 1):
#     count = 0
#     for j in range(1, n + 1):
#         if i % j == 0:
#             count += 1

#     if count == 2:
#         print(i)

# 5. Print the Fibonacci pattern row by row, where each row prints the next Fibonacci numbers


# 6. Generate and print a number triangle pattern using nested loops.

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):  # rows
#     for j in range(1, i + 1):  # number in rows
#         print(j, end=" ")
#     print()


# 7. Print a matrix, then calculate and display the sum of each row and the sum of
# each column.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

for row in matrix:
    print("Row sum:", sum(row))

for col in range(len(matrix[0])):
    col_sum = 0
    for row in range(len(matrix)):
        col_sum += matrix[row][col]
    print("Column sum:", col_sum)

# 8. Print all Pythagorean triplets whose values are less than or equal to n.


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for col in range(len(matrix[0])):
#     col_sum = 0
#     for row in range(len(matrix)):
#         col_sum += matrix[row][col]
