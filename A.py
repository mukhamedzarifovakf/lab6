N = int(input())
n = input().split()
for i in range(N-1):
    for k in range(i+1, N):
        if n[k] == n[i]:
            print(n[i])
