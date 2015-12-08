f=open('input.txt')
N=int(f.readline()) 
massiv=f.readline().split()
vedro=set()
for i in massiv:
   if i not in vedro:
       vedro.add(i)
   else:   
      f=open('output.txt', 'w')
      print(i, file=f)
      f.close()
