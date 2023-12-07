data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

def partition(left, right):
    pivot = data[left]
    low = left + 1
    high = right

    while low < high:
        while low <= right and data[low] < pivot:
            low += 1
        while high >= left and data[high] > pivot:
            high -= 1
        
        if low < high:
            data[low], data[high] = data[high], data[low]
    
    data[left], data[high] = data[high], data[left]
    return high

def quickSort(left, right):
    if left < right:
        q = partition(left, right)
        quickSort(left, q-1)
        quickSort(q+1, right)

if __name__ == '__main__':
    print('Origin: ', data)
    quickSort(0, len(data) -1)
    print('Sorted: ', data)