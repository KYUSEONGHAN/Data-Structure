# 과제를 수행하기 위한 함수들을 따로 모아놓은 파일
from homework.tree import Tree

# tree가 bst (binary search tree인지 확인하는 함수)
# 반환형은 true, false로 bst인지 아닌지를 반환
def check_bst(root, left=None, right=None) -> bool:
    if not root:
        return True

    # node 값이 왼쪽이 정의된 상태에서 node값이 왼쪽 자식 노드보다 같거나 더 크면 bst에 성립 x
    if left != None and root.data <= left.data:
        return False

    # node 값이 오른쪽이 정의된 상태에서 node값이 오른쪽 자식 노드보다 같거나 더 크면 bst에 성립 x
    if right != None and root.data >= right.data:
        return False

    # 재귀 호출로 모든 노드를 탐색
    return check_bst(root.left, left, root) and check_bst(root.right, root, right)


# 이진탐색트리인 경우 입력값 대입 함수
def bst_true():
    root = Tree(5)
    root.left = Tree(2)
    root.right = Tree(10)
    root.left.left = Tree(1)
    root.left.right = Tree(4)
    root.right.left = Tree(8)
    root.right.right = Tree(13)

    return root

# 이진탐색트리가 아닌 경우 입력값 대입 함수
def bst_fail():
    root = Tree(5)
    root.left = Tree(2)
    root.right = Tree(10)
    root.right.left = Tree(11)
    root.right.right = Tree(9)

    return root