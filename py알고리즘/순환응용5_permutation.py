# 임의의 집합 data에 대해서 원소들의 모든 가능한 순열을 출력하라

data = ['a','b','c','d']

n = 4

def swap(a, b):
    temp = data[a]
    data[a] = data[b]
    data[b] = temp

def perm(k):
    if(k==n):
        print(data[0:n])
        return
    for i in range(k,n):
        swap(k,i)
        perm(k+1)
        swap(k,i)


perm(0)