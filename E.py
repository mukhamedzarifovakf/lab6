def CountDebts(Debts, Bills):
    Debts[Bills[0]-1] -= Bills[2]
    Debts[Bills[1]-1] += Bills[2]
N, K = input().split()
K = int(K)
N = int(N)
Debts = [0]*N
for i in range(K):
    Bills = [int(x) for x in input().split()]
    CountDebts(Debts, Bills)
for x in Debts:
    print(x, end = ' ')
