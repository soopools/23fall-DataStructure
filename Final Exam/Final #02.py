colors = ['B', 'R', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R', 'G']

def sepColor(left, right):
    q = partition(left, right, 'R')
    partition(q, right, 'G')

def partition(left, right, pivot):
    i = left
    for j in range(left, right+1):
        if colors[j] == pivot:
            colors[i], colors[j] = colors[j], colors[i]
            i += 1
    return i

if __name__ == '__main__':

    print("Origin :", colors)
    sepColor(0, len(colors)-1)
    print("Sorted :", colors) 