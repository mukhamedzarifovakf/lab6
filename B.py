N = int(input())
n = [int(x) for x in input().split()]
requiredcoins = 0
availiblecoins = 0
for i in range(N):
    if n[i] == 5:
        availiblecoins += 1
    else:
        availiblecoins -= (n[i] - 5) / 5
        if availiblecoins < 0:
            requiredcoins -= availiblecoins
            availiblecoins = 0
else:
    print(int(requiredcoins))
