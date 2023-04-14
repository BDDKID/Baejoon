# 2진수와 10진수로 표현 아하 그렇구나
# or연산으로 이진수를 계산해보자!
def solution(n, arr1, arr2):
    result = []
    for i, j in zip(arr1, arr2):
        result.append(bin(i | j)[2:].zfill(n).replace('0', ' ').replace('1', '#'))
    return result