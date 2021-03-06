def solution(board, moves):
    stack = []
    cnt = 0
    
    for i in moves:
        for j in range(0,len(board)):
            if board[j][i-1] != 0:
                       stack.append(board[j][i-1])
                       board[j][i-1] = 0
                       break
        while True:
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2
                else:
                       break
            else:
                break
    return cnt
            
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))