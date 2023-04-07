def solution(array, height):
    ls = []
    for i in array:
        if i > height:
            ls.append(i)
    return len(ls)