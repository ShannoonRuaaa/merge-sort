
def mergesort(arr):
    N = len(arr)
    if N <2:
        return arr
    arr1 = mergesort(arr[0:int (N/2)])
    arr2 = mergesort(arr[int(N/2):N])
    ans = []
    index1 = 0
    index2 = 0
    len1 = len(arr1)
    len2 = len(arr2)
        # merge
    while index1 < len1  and index2 < len2:
        if arr1[index1] < arr2[index2]:
            ans.append(arr1[index1])
            index1+=1
        else:
            ans.append(arr2[index2])
            index2+=1
    if index1 < len1:
        while index1 < len1:
            ans.append(arr1[index1])
            index1+=1
    else:
        while index2 < len2:
            ans.append(arr2[index2])
            index2 +=1
    return ans

# counter = 0
arr = [3, 2, 1, 5, 3, 0, 9, 4,6,10]
print(mergesort(arr))