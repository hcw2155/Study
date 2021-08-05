def solution(s):
    
    left = ['(','{','[']
    right = [')','}',']']
    answer = 0
    
    for i in range(0,len(s)):
        temp = s[i:] + s[0:i]
        cnt = [0,0,0]
        flag = 0
        for j in temp:
            if j in left:
                if j == '(':
                    cnt[0] += 1
                elif j == '{':
                    cnt[1] += 1
                elif j == '[':
                    cnt[2] += 1
            else:
                if j == ')':
                    cnt[0] -= 1
                elif j == '}':
                    cnt[1] -= 1
                elif j == ']':
                    cnt[2] -= 1
            for i in cnt:
                if i < 0 :
                    flag = 1
        if flag == 0 and cnt.count(0) == 3:
            answer += 1
                
    return answer