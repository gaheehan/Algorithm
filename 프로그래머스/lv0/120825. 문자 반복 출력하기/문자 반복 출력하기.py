def solution(my_string, n):
    answer = ''
    for i in str(my_string):
        answer += i*n
    return answer