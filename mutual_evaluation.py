# Mutual evaluation

def solution(scores):
    answer =''
    new_list = [[] for i in range(len(scores))]

    for i in range(len(scores)):
        for j in range(len(scores)):
            new_list[i].append(scores[j][i])
        if new_list[i][i] == max(new_list[i]) and new_list[i].count(new_list[i][i]) == 1:
            new_list[i].remove(new_list[i][i])
        elif new_list[i][i] == min(new_list[i]) and new_list[i].count(new_list[i][i]) == 1:
            new_list[i].remove(new_list[i][i])
        else:
            print(new_list[i][i],'bye')
    answer = ''
    print(new_list)
    for i in new_list:
        temp = sum(i)/len(i)
        if temp >= 90:
            answer += 'A'
        elif temp < 90 and temp >= 80:
            answer += 'B'
        elif temp < 80 and temp >= 70:
            answer += 'C'
        elif temp < 70 and temp >= 50:
            answer += 'D'
        else:
            answer += 'F'
        print(temp,answer)
    return answer

scores = [[70,49,90],[68,50,38],[73,31,100]]
scores1 = [[50,90],[50,87]]
scores2 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores1))

                

