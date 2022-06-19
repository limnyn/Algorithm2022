

def mergeSort(arr):   #arr[p----r]을 정렬한다
    if len(arr) < 2:
        return arr

    q= len(arr)//2
    left_arr = mergeSort(arr[:q])
    right_arr = mergeSort(arr[q:])
    
    i = 0
    j = 0
    newList = []
    while i<len(left_arr) and j<len(right_arr):
        if(left_arr[i] <= right_arr[j]):
            newList.append(left_arr[i])
            i+=1
        else:
            newList.append(right_arr[j])
            j+=1
    
    newList+= left_arr[i:]
    newList+= right_arr[j:]
    return newList




    




lst = [0,3,2,4,1]
print(mergeSort(lst))