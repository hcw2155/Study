def solution(s):
    a = []
    natural_number = ['0','1','2','3','4','5','6','7','8','9']
    temp = ''
    d = [0] * 100001

    for i in s[1:-1]:
        if i in natural_number:
            temp += i
            d[int(temp)] += 1
        else:
            if temp != '' and int(temp) not in a:
                a.append(int(temp))
            temp = ''
    result = []
    for i in a:
       result.append((i,d[i]))
    result = sorted(result, key=lambda result: result[1], reverse=True)
    real_answer = []
    for i in result:
        real_answer.append(i[0])
    return real_answer

    
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
