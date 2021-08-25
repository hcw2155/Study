def dist(tuple1,tuple2):
    distance = 0
    distance = abs(tuple1[0]-tuple2[0])+abs(tuple1[1]-tuple2[1])
    return distance
    
def solution(numbers, hand):
    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    dict = {}
    for i in range(0,len(keypad)):
        for j in range(0,len(keypad[0])):
            dict[keypad[i][j]] = (i,j)
    left = '*'
    right = '#'
    answer = ''
    for number in numbers:
        if str(number) in ['1','4','7']:
            answer += 'L'
            left = str(number)
        elif str(number) in ['3','6','9']:
            answer += 'R'
            right = str(number)
        else:
            left_len = dist(dict[str(number)],dict[left])
            right_len = dist(dict[str(number)],dict[right])
            if left_len > right_len:
                answer += 'R'
                right = str(number)
            elif left_len < right_len:
                answer += 'L'
                left = str(number)
            else:
                if hand == 'left':
                    answer += 'L'
                    left = str(number)
                else:
                    answer += 'R'
                    rigt = str(number)
    print(dict)
    return answer                
            
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers2,hand))                               
    
