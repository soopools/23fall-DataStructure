class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None  

# 손으로 구조 따라 그려보기
def getHeight(root):
    if root is None:
        return 0
    
    hLeft = getHeight(root.left)
    hRight = getHeight(root.right)

    if hLeft > hRight:
        return hLeft + 1
    
    else: 
        return hRight + 1
    
def getBalance(root):
    if root is None:
        return 0
    
    return getHeight(root.left) - getHeight(root.right)

def rotateRight(p): # 날아온 노드를 parent (p)로 지정
    c = p.left # c는 p의 왼쪽 자식
    p.left = c.right # p의 왼쪽 자식은 c의 오른쪽 자식
    c.right = p # c의 오른쪽 자식은 p
    return c # c를 새로운 parent로 지정

def rotateLeft(p): 
    c = p.right
    p.right = c.left
    c.left = p
    return c

def insertNode(root, key):
    if root == None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insertNode(root.left, key)
    
    elif key > root.key:
        root.right = insertNode(root.right, key)

    balance = getBalance(root)

    # LL (2)
    if balance > 1 and key < root.left.key: # 시계 방향으로 회전
        return rotateRight(root) # rotateLL()
    
    # LR (2)
    if balance > 1 and key > root.left.key: # 반시계 방향으로 회전
        root.left = rotateLeft(root.left)
        return rotateRight(root)

    # RR (-2)
    if balance < -1 and key > root.right.key:
        return rotateLeft(root) # rotateRR()

    # RL (-2)
    if balance < -1 and key < root.right.key:
        root.right = rotateRight(root.right)
        return rotateLeft(root)

    return root

# def inOrder(root):
#     if root:
#         inOrder(root.left)
#         print('[%c] ' % root.data, end='') # 프린트 중간에
#         inOrder(root.right)

def preOrder(root):
    if root:
        print('[%c] ' % root.key, end='')
        preOrder(root.left)
        preOrder(root.right)

def display(root, msg):
    print(msg, end = ' ')
    preOrder(root)
    print()

if __name__ == '__main__':

    root = None # root is the root node of the tree: 루트 노드 지정 ==  빈 트리
    # keys = [7, 8, 9, 2, 1, 5, 3, 6, 4] # keys is the list of keys to be inserted: 삽입할 키 리스트, !! 26 중복 !!
    keys = [5, 3, 1, 8, 10]
    
    for key in keys:
        root = insertNode(root, key) # insert each key to the tree: 키를 트리에 삽입
        display(root, '[Insert %2d]' % key) # display the tree after each insertion: 삽입 후 트리 출력]')
    
    print()