from collections import deque
def solution(s):

    dir = ['()','[]','{}']
    answer = 0
    
    for i in range(0,len(s)):
        temp = s[i:] + s[0:i]
        temp = deque(temp)
        stack = []
        stack = deque(stack)
        while len(temp) != 0:
            stack.append(temp.popleft())
            if len(stack) >= 2:
                if stack[-2] + stack[-1] in dir:
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            answer +=1
            
    return answer
