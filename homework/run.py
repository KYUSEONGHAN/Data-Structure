# 과제를 수행하기 위한 main 함수 정의 파일
from homework.utils import check_bst, bst_fail, bst_true

if __name__ == '__main__':
    if check_bst(bst_true()):
        print('이진탐색트리입니다.')
    else:
        print('이진탐색트리가 아닙니다.')

    if check_bst(bst_fail()):
        print('이진탐색트리입니다.')
    else:
        print('이진탐색트리가 아닙니다.')
