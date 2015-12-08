f=open('input.txt')
N=int(f.readline())
free=0
fives=0
massiv=list(map(int, f.readline().split()))
for i in massiv:
    if i==5:
        free+=1
    else:
        d=(i-5)//5
        if free>0:
            if free>=d: d,free = 0, free-d
            else: d,free = d-free, 0
        fives+=d
            
f=open('output.txt', 'w')    
        

print(fives, file = f)    
f.close()
