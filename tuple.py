def solution(s):
    new = []
    inside = []
    temp = ''
    cnt=0
    for i in s[1:-1]:
        if i == '{':
            cnt = 1
        elif i == '}':
            inside.append(int(temp))
            new.append(inside)
            temp = ''
            inside = []
            cnt = 0
        elif i == ',':
            if cnt == 1:
                inside.append(int(temp))
            temp =''
        else:
            temp += i
    new = sorted(new, key=len)
    print(new)
    answer = []
    for i in new:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

