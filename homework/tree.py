# 트리 선언하는 부분을 따로 선언한 파일
class Tree:  # tree 생성, 선언부
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None