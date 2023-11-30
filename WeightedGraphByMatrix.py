
Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Weight = [
    [None, 29, None, None, None, 10, None],
    [29, None, 16, None, None, None, 15],
    [None, 16, None, 12, None, None, None],
    [None, None, 12, None, 22, None, 18],
    [None, None, None, 22, None, 27, 25],
    [10, None, None, None, 27, None, None],
    [None, 15, None, 18, 25, None, None]]

def display():
    for i in range(len(Vertex)):
        for j in range(i+1, len(Vertex)):
            if Weight[i][j] != None:
                print('[%c%c%d]' %(Vertex[i], Vertex[j], Weight[i][j]), end=' ')
        print()

if __name__ == '__main__':
    display()
