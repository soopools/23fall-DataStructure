class TreeNode:
    def __init__(self, data, left, right): # Constructor, 서브 트리 지정
        self.data = data
        self.left = left
        self.right = right

def preOrder(root): # 루트가 날아온다 >> 트리가 날아온다 OOOOOO 노드가 날아온다는 단순한 의미 아님 xxxxxx
    if root: # root가 None이 아니면 # if root != None:, if root is not None:
        # root가 none이 아닐 때만 실행
        print('[%c] ' % root.data, end='') # 루트 노드 방문
        preOrder(root.left) # 왼쪽 서브트리로 가기 (현재 루트 노드의 왼쪽 자식)
        preOrder(root.right)

# 중위 순회 > 숙젱 ~
def inOrder(root):
    if root:
        inOrder(root.left)
        print('[%c] ' % root.data, end='') # 프린트 중간에
        inOrder(root.right)

# 후위 순회 > 숙젱 ~
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print('[%c] ' % root.data, end='') # 프린트 마지막에

if __name__ == '__main__':
    N4 = TreeNode('D', None, None) # Leaf Node: 단말
    N5 = TreeNode('E', None, None)
    N6 = TreeNode('F', None, None)
    N2 = TreeNode('B', N4, N5)
    N3 = TreeNode('C', N6, None)
    N1 = TreeNode('A', N2, N3)

    print('Preorder: ', end=''); preOrder(N1); print()
    print('Inorder: ', end=''); inOrder(N1); print()
    print('Postorder: ', end=''); postOrder(N1); print()


'''
Result: A B D E C F

'''

