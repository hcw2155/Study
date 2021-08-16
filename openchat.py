def solution(record):
    answer = []
    result = []
    id = {}
    # Enter uid1234 Muzi / Etner Leave Change
    for i in record:
        i = i.split(" ")
        if len(i) > 2:
            id[i[1]] = i[2]
        result.append([i[0],i[1]])
    print(id, result)

    for i in result:
        if i[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.'%id.get(i[1]))
        elif i[0] == 'Leave':
            answer.append('%s님이 나갔습니다.'%id.get(i[1]))


    # for i in record:
    #     i = i.split(" ")
    #     if i[1] not in id:
    #         id.append(i[1])
    #     result.append(i)
    # temp_name = ''
    # final_name = []
    
    # for i in id:  
    #     for j in result:
    #         if len(j) > 2 and i == j[1]: 
    #             temp_name = j[2]
    #     final_name.append([i,temp_name])
    #     temp_name = ''
        
    # for i in result:
    #     for j in final_name:
    #         if i[0] == 'Enter' and j[0] == i[1]:
    #             answer.append('%s님이 들어왔습니다.'%(j[1]))
    #         elif i[0] == 'Leave' and j[0] == i[1]:
    #             answer.append('%s님이 나갔습니다.'%(j[1]))

    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
