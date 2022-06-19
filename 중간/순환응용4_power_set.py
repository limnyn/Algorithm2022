
data = ['a','b','c','d']
n = len(data)
include =[0,0,0,0]

print(include)

def powerSet(k):
    if(k==n):
        for i in range(n):
            if(include[i]):print(data[i], end=" ")
        print()
        return
    include[k]= 0
    powerSet(k+1)
    include[k]=1
    powerSet(k+1)

powerSet(0)