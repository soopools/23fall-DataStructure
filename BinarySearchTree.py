class TreeNode:
    def __init__(self, key):
        self.key = key # key is the value of the node: 노드의 키 지정
        self.left = None # left is the left child of the node: 단말 노드라 노드 왼쪽/오른쪽 자식 없음
        self.right = None
    
def insertNode(root, key):
    if root == None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insertNode(root.left, key)
    
    elif key > root.key:
        root.right = insertNode(root.right, key)

    return root

def in_Order(root):
    if root != None:
        in_Order(root.left)
        print('%2d ' %root.key, end = ' ')
        in_Order(root.right)

def min_key_node(root):
    while root is not None and root.left is not None:
        root = root.left

    return root

def deleteNode(root, key):
    if root == None:
        return None

    if key < root.key:
        root.left = deleteNode(root.left, key)
    
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    
    else:
        succ = min_key_node(root.right) # successor 찾기
        root.key = succ.key # successor의 키를 root로 복사
        root.right = deleteNode(root.right, succ.key) # successor 삭제
        
    return root

def display(root, msg):
    print(msg, end = ' ')
    in_Order(root)
    print()

if __name__ == '__main__':

    root = None # root is the root node of the tree: 루트 노드 지정 ==  빈 트리
    keys = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99] # keys is the list of keys to be inserted: 삽입할 키 리스트, !! 26 중복 !!

    for key in keys:
        root = insertNode(root, key) # insert each key to the tree: 키를 트리에 삽입
        display(root, '[Insert %2d]' % key) # display the tree after each insertion: 삽입 후 트리 출력]')
    
    print()
'''
case 2: 삭제할 노드가 자식 노드 하나만 가지고 있을 경우
    root = deleteNode(root, 30)
    display(root, '[Delete 30]')
    root = deleteNode(root, 26)
    display(root, '[Delete 26]')
'''
    root = deleteNode(root, 18)
    display(root, '[Delete 18]: ')
