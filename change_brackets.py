def correct(s):
    cnt = [0,0]
    for i in s:
        if i == '(':
            cnt[0] += 1
        elif i == ')':
            cnt[1] += 1
        if cnt[0] < cnt[1]:
            return False
    return True

def separation(s): # 분리 과정
    cnt = [0,0]
    result=[]
    for i in range(0,len(s)):
        if s[i] == '(':
            cnt[0] += 1
        elif s[i] == ')':
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            result.append(s[:i+1])
            result.append(s[i+1:])
            break
    return result

def do2(p):
    answer = ''
    result =  separation(p)
    while True:
        if correct(result[0]):
            answer += result[0]
            if len(result[1]) != 0:
                result = separation(result[1])
            else:
                break
        else:
            break
    return [answer,result[0],result[1]]

def last(s):
    result = ''
    if len(s) == 2:
        return result
    else:
        s = s[1:len(s)-1]
        for i in range(0,len(s)):
            if s[i] =='(':
                result += ')'
            elif s[i] ==')':
                result += '('
    return result

def solution(p):
    answer = ''
    # 빈 문자열 처리
    if correct(p): # 올바르면 반환
        return p
    else: # 올바르지 않으면 2단계 수행
        result = do2(p)
        print(result,'this is result, 2 phase')
        answer = result[0] + '(' + do2(result[2])[1] + ')'
        print(answer,'this is answer1')
        answer += last(result[1])
        print('***',result[1],last(result[1]))
        print(answer,'this is answer2')
    print(answer)

p = "()))((()"
solution(p)
