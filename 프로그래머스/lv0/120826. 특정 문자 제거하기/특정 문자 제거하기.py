import re
def solution(my_string, letter):
    return re.sub(rf'[{letter}]','',my_string)