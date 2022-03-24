import readline


n = int(input())


listL = []
for _ in range(n):
    listL.append(int(input()))
listL.sort()
for i in range(n):
    print(str(listL[i]))

