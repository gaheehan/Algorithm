def solution(sides):
    sides.sort()
    a = sides[2]
    b = sides[:2]    
    if a == sum(b):
        answer = 2
    elif a > sum(b):
        answer = 2
    else:
        answer = 1
    return answer