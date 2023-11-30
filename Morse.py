table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

def encode(ch):
        idx = ord(ch) - ord('A')
        return table[idx][1]

def decodedFromTable(code):
        for e in table:
                if code == e[1]:
                        return e[0]
        return None

class TreeNode:
        def __init__(self, data, left, right):
                self.data = data
                self.left = left
                self.right = right
        
def makeMorseTree():

        root = TreeNode(None, None, None)

        for e in table:
                code = e[1]
                node = root

                for c in code:
                        if c == '.': # C가 .이면 왼쪽으로 이동
                                if node.left == None: # 왼쪽 자식이 없으면
                                        node.left = TreeNode(None, None, None) # 왼쪽 자식 노드 생성
                                node = node.left
                        elif c == '-': # C가 -이면 오른쪽으로 이동
                                if node.right == None:
                                        node.right = TreeNode(None, None, None)
                                node = node.right
                node.data = e[0]
        return root

def decodedFromTree(root, code):
        node = root

        for c in code:
                if c == '.':
                        node = node.left
                elif c == '-':
                        node = node.right
        return node.data

if __name__ == '__main__':
        str = input("Input a String: ")
        encoded = []
        
        for ch in str:
                code = encode(ch)
                encoded.append(code)
        
        print('Morse Code: ', encoded)
        print('Decoding : ', end = ' ')

        for code in encoded:
                print(decodedFromTable(code), end = ' ')
        print()
        
        root = makeMorseTree()
        print('Decoding From Tree: ', end = ' ')

        for code in encoded:
                print(decodedFromTable(root, code), end = ' ')
        print()

# 테이블로 만들었을 경우 O(n)의 시간 복잡도,
# 그런데 위 코드처럼 하면 이진탐색트리 구조 활용 가능
# 트리의 높이에 비례하여 연산 수행 가능