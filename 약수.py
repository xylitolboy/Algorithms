a = int(input())

A = list(map(int,input().split()))

A.sort()

N = A[0] * A[-1]
print(N)