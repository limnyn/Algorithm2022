# 바이너리 서치
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.



def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None
# 이진 검색 재귀
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)



# 정렬

# 버블 정렬후 정렬 반환
def bubble_Sort(arr):
    n = len(arr)
    for i in range(n):              #배열의 크기만큼 반복
        for j in range(0, n-i-1):   #배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]         #서로 위치를 변환
    return 


# 삽입 정렬후 반환
def insertion_sort(arr):
    n = len(arr)
    for a in range(1, n):
        for b in range(a, 0,-1):
            if arr[b] < arr[b-1]:
                arr[b],arr[b-1] = arr[b-1], arr[b]
            else:
                    break
    return 
# 선택 정렬후 반환
def selection_sort(arr):
    n = len(arr)
    for a in range(n - 1):
        min = a
        for b in range(a + 1, n):
            if arr[b] < arr[min]:
                min = b
        arr[min], arr[a] = arr[a], arr[min]
    return 





#분할정복법

#합병 정렬후 반환
#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merge_list = []
    left_id, right_id = 0, 0
    
    #case1 left, right
    while len(left) > left_id and len(right) > right_id:
        if left[left_id] > right[right_id]:
            merge_list.append(right[right_id])
            right_id += 1
        else:
            merge_list.append(left[left_id])
            left_id += 1
    
    #case2 left
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id += 1
    
    #case3 right
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id += 1
    
    return merge_list

#퀵 정렬 후 반환, 피벗은 배열의 제일 마지막 수로 설정, 재귀적 방식
def quick_sort(arr, p ,r):
    
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q, r)

def partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1  #arr[r]이 자리한 위치 반환

def partition_medianOfThree(arr,p,r):
    
    #제일앞, 뒤, 중간값을 뽑아 정렬후 가운데 순위 값을 피벗으로 설정
    motList = [arr[p],arr[(p+r)//2],arr[r]]
    motList.sort()
    if motList[1] != arr[r]:
        arr[motList[1]],arr[r] = arr[r],arr[motList[1]]

    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1  #arr[r]이 자리한 위치 반환


# #Quick Sort 파이썬버전 간결한 버전, 
# def quick_Sort(array):
#     if len(array) <= 1:
#         return array
    
#     left, right = [], []
#     pivot = array[0]
    
#     for a in range(1, len(array)):
#         if pivot < array[a]:
#             right.append(array[a])
#         else:
#             left.append(array[a])
    
#     return quick_Sort(left) + [pivot] + quick_Sort(right)


# # heapsort

# # max - heapify
# def max_heapify(arr, i,size): #노드 i를 루트로하는 서브트리를 heapify
#     if  i*2 > size:
#         return
#     if (arr[2*i] >=arr[2*i+1]):
#         k = 2*i
#     else:
#         k = 2*i+1
#     if arr[i] >= arr[k]:
#         return
#     arr[i], arr[k] = arr[k], arr[i]
#     max_heapify(arr,k,size)

# def heap_sort(arr):
#     size=len(arr)-1

#     for i in range(size//2,-1,-1):  #정렬할 배열 힙으로 만들기 
#         max_heapify(arr,i,size)

#     for i in range(size,-1,-1):    #끝부터 0까지 역순으로
#         arr[0], arr[i] = arr[i], arr[0]
#         size-=1
#         max_heapify(arr,0,size)

# # heap 삽입, pop함수 추가필요





###heapsort 최대힙, 재귀x구현
def heap_sort(a):
    for i in range(1,len(a)): # 최대 힙 만들기
        c = i
        while c != 0:
            r = (c-1) // 2
            if a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
                
            c = r

    for j in range(len(a)-1,-1,-1): # 힙 만들기
        a[0], a[j] = a[j], a[0]
        r = 0
        c = 1

        while c < j:
            c= 2 * r + 1
            if c < j -1 and a[c] < a[c+1]:
                c += 1
                
            if c < j and a[r] < a[c]:
                a[r], a[c]=a[c], a[r]
                
            r = c 

# b = [5, 2, 3, 9, 6, 1, 8, 4, 7]
# heap_sort(b)

# #최소힙구현
# def heapify(li, idx, n):
#     l = idx * 2;
#     r = idx * 2 + 1
#     s_idx = idx
#     if (l <= n and li[s_idx] > li[l]):
#         s_idx = l
#     if (r <= n and li[s_idx] > li[r]):
#         s_idx = r
#     if s_idx != idx:
#         li[idx], li[s_idx] = li[s_idx], li[idx]
#         return heapify(li, s_idx, n)
 
# def heap_sort(v) :
#     n = len(v)
#     v = [0]+v
 
#     # min heap 생성
#     for i in range(n, 0, -1) :
#         heapify(v, i, n)
 
#     # min element extract & heap
#     for i in range(n, 0, -1) :
#         print(v[1])
#         v[i], v[1] = v[1], v[i]
#         heapify(v, 1, i-1)
 
# heap_sort([5,3,4,2,1])



li = [15,12,2,11,10,6,3,1,8]
heap_sort(li)
print(li)