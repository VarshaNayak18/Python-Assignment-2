# Question 11: Number Pattern Printer
"""
Create a program that prints the following patterns. User should choose which pattern and
height.

Bonus: Add 3 more creative patterns

Pattern 1:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Pattern 2:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Pattern 3:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Pattern 4:
1
121
12321
1234321
123454321

Pattern 5:
1 
2  3 
4  5  6 
7  8  9  10
11 12 13 14 15

Pattern 6:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

Pattern 7:
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
"""

# Display available patterns
print("Available Patterns:")
print("1). Pattern 1:\n    1\n    1 2\n    1 2 3\n    1 2 3 4\n    1 2 3 4 5\n")
print("2). Pattern 2:\n    1\n    2 2\n    3 3 3\n    4 4 4 4\n    5 5 5 5 5\n")
print("3). Pattern 3:\n    5 4 3 2 1\n    4 3 2 1\n    3 2 1\n    2 1\n    1\n")
print("4). Pattern 4:\n    1\n    121\n    12321\n    1234321\n    123454321\n")
print("5). Pattern 5:\n    1\n    2  3\n    4  5  6\n    7  8  9  10\n    11 12 13 14 15\n")
print("6). Pattern 6:\n    1\n    0 1\n    1 0 1\n    0 1 0 1\n    1 0 1 0 1\n")
print("7). Pattern 7:\n    1\n   1 1\n  1 2 1\n 1 3 3 1\n1 4 6 4 1\n")
# Take input from user
pattern = input("Enter your choice of pattern: ")
h = int(input("Enter the height for the selected pattern: "))

if pattern == "1":
    print("Pattern 1:")
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(j, end = " ")
        print()

elif pattern == "2":
    print("Pattern 2:")
    for i in range(1, h+1):
        for j in range(i):
            print(i, end = " ")
        print()

elif pattern == "3":
    print("Pattern 3:")
    for i in range(h, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()

elif pattern == "4":
    print("Pattern 4:")
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(j, end = "")
        for j in range(i-1, 0, -1):
            print(j, end = "")
        print()

elif pattern == "5":
    print("Pattern 5:")
    n = 1
    for i in range(1, h+1):
        for j in range(i):
            print(f"{n:2}", end = " ")
            n += 1
        print()

elif pattern == "6":
    print("Pattern 6:")
    for i in range(1, h+1):
        n = i % 2
        for j in range(i):
            print(n, end=" ")
            n = 1 - n
        print()

elif pattern == "7":
    print("Pattern 7:")
    for i in range(h):
        for j in range(h - i - 1):
            print(" ", end="")

        n = 1
        for j in range(i + 1):
            print(n, end=" ")
            n = n * (i - j) // (j + 1)
        print()

else:
    print("Please select valid pattern number")