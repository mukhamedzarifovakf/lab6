k, n = input().split()
k = int(k)
n = int(n)
Minimums = [int(x) for x in input().split()]
for i in range (k-1):
    Current_tempretures = [int(x) for x in input().split()]
    for i in range(n):
        if Minimums[i] > Current_tempretures[i]:
            Minimums[i] = Current_tempretures[i]
for x in Minimums:
    print(x, end = ' ')
