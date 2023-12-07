data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
sorted = [0] * len(data)

def merge(left, mid, right):
    i = left
    j = mid+1
    k = left
    
    while i <= mid and j <= right:
        if data[i] <= data[j]:
            sorted[k] = data[i]
            i += 1
            k += 1

        else:
            sorted[k] = data[j]
            j += 1
            k += 1
    
    if i > mid:
        for l in range(j, right+1):
            sorted[k] = data[l]
            k += 1
    else:
        for l in range(i, mid+1):
            sorted[k] = data[l]
            k += 1

    data[left:right+1] = sorted[left:right+1]

def mergeSort(left, right): # divide
    if left < right:
        mid = (left + right) // 2
        mergeSort(left, mid)
        mergeSort(mid+1, right)
        merge(left, mid, right)


if __name__ == '__main__':
    print('Origin: ', data)
    mergeSort(0, len(data) -1)
    print('Sorted: ', data)