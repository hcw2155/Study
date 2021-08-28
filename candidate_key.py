from itertools import combinations
def solution(relation):
    answer = 0
    k = len(relation)
    x = list(zip(*relation))
    print(x)
    cnt = 0
    while True:
        cnt += 1
        if len(x) >= cnt:
            temp = x[:]
            temp = list(combinations(temp,cnt))

            temp_remove = []
            for i in temp:
                check = list(zip(*i))
                print(check,cnt,answer)
                print(set(check))
                for j in i:
                    temp_remove.append(j)
                if len(set(check)) == k:
                    answer += 1
                    for i in temp_remove:
                        x.remove(i)
                else: print('no')
        else: break
            # temp_remove = []
            # #print(temp,cnt)
            # for i in temp:
            #     for j in i:
            #         temp_remove.append(j)
            # print(cnt,temp_remove)
            # temp_zip = list(zip(*temp))
            # if len(temp_zip) == k:
            #     answer += 1
            #     for i in temp_remove:
            #         x.remove(i)
    print(x)
    return answer

relation2 = [["100","ryan"]]
relation = [[100],[200],[300],[400],[500],[500]]
print(solution(relation))