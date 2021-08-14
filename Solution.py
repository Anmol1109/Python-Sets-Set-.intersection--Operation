# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(input().split())

m = int(input())
B = set(input().split())

print(len(A.intersection(B)))
