def correct(s):
    cnt = [0,0]
    for i in s:
        if i == '(':
            cnt[0] += 1
        elif i == ')':
            cnt[1] += 1
        if cnt[0] < cnt[1]:
            return False
    return Ture
        
def solution(p):
    answer = ''
    return answer
p = "()))((()"
solution(p)