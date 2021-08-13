from itertools import permutations

def cal(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def change(s):
    s += '.'
    cal = ['+','-','*']
    result = []
    temp = ''
    for i in s:
        if i in cal:
            result.append(temp)
            result.append(i)
            temp = ''
        elif i == '.':
            result.append(temp)
            break
        else:
            temp += i
    return result

def solution(expression):
    answer = 0
    temp = ''
    op = list(permutations(['+','-','*']))
    new = change(expression)
    print(new)
    for i in operation:
        pass
  
    return answer


expression = "100-200*300-500+20"
solution(expression)