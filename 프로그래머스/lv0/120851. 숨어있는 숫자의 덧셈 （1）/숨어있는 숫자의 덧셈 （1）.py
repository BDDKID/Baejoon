import re

def solution(my_string):
    new_string = re.sub(r'[a-zA-Z]','',my_string)
    number = int(new_string)
    answer = 0
    while number > 0:
        digit = number % 10
        answer += digit
        number //= 10
                  
    return answer