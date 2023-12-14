class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

def mergeTree(t1, t2):
    if t1 == None and t2 == None:
        return None
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    t1.val += t2.val
    t1.left = mergeTree(t1.left, t2.left)
    t1.right = mergeTree(t1.right, t2.right)
    return t1
    
def preOrder(root):
    if root == None:
        return
    print("[{}]".format(root.val), end=' ')
    preOrder(root.left)
    preOrder(root.right)

if __name__ == '__main__':
    N4 = TreeNode(5, None, None); N3 = TreeNode(2, None, None)
    N2 = TreeNode(3, N4, None); T1 = TreeNode(1, N2, N3)

    M6 = TreeNode(7, None, None); M5 = TreeNode(4, None, None);
    M3 = TreeNode(3, None, M6); M2 = TreeNode(1, None, M5)
    T2 = TreeNode(2, M2, M3)

    root = mergeTree(T1, T2)
    preOrder(root)