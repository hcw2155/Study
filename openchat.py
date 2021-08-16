def solution(record):
    answer = []
    result = []
    id = []

    for i in record:
        i = i.split(" ")
        if i[1] not in id:
            id.append(i[1])
        result.append(i)
    temp_name = ''
    final_name = []
    
    for i in id:  
        for j in result:
            if len(j) > 2 and i == j[1]: 
                temp_name = j[2]
        final_name.append([i,temp_name])
        temp_name = ''
        
    for i in result:
        for j in final_name:
            if i[0] == 'Enter' and j[0] == i[1]:
                answer.append('%s님이 들어왔습니다.'%(j[1]))
            elif i[0] == 'Leave' and j[0] == i[1]:
                answer.append('%s님이 나갔습니다.'%(j[1]))

    return answer