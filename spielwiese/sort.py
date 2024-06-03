

def pivot(pivot,arr):
    p = 0
    q = len(arr)-1
    arr[0], arr[pivot] = arr[pivot], arr[0]
    for i in range(1, q+1):
        if arr[i] <= arr[0]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    arr[0], arr[p-1] = arr[p-1], arr[0]
    return arr[:p], arr[p:]
