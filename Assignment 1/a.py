"""
Problem A: Max

Given a collection of n  integers, your program should output the maximum element of the collection.

Input
The input consists of an integer n that specifies the size of the collection, followed by the n integers themselves,
one per line.

Output
The output should be the maximum element from the collection, followed by a newline character.

Example
Sample Input
4
2
-3
21
8

Sample Output
21
"""


nums = []
print("Enter a number:")
length = int(input(''))

for i in range(length):
    new = input('')
    nums.append(new)

print(max(nums))
