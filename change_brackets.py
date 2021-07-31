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
    u = ''
    v = ''
    for i in range(0,len(s)):
        if s[i] == '(':
            cnt[0] += 1
        elif s[i] == ')':
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            u = s[:i+1]
            v = s[i+1:]
            break
    return [u,v]

def do2(p):
    answer = ''
    result =  separation(p)
    u = result[0]
    v = result[1]
    while True:
        if correct(u) == True:
            answer += u
            if v == '':
                return [answer,u,v] 
            result = separation(v)
            u = result[0]
            v = result[1]
        elif correct(u) == False:
            break
    print('answer:',answer,'u:',u,'v:',v,'here')
    return [answer,u,v]

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
    # do_2 -> [answer,u,v]
    # 빈 문자열 처리
    if correct(p): # 올바르면 반환
        return p
    else: # 올바르지 않으면 2단계 수행
        result = do2(p)
        print(result,'************')
        answer = result[0] + '(' + (do2(result[2])[1]) + ')'
        answer += last(result[1])
    print('answer:',answer)

p = "()"
solution(p)
