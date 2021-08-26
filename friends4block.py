def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))
    m,n = n,m
    while True:
        p = [i[:] for i in board]
        temp = answer
        for i in range(0,m-1):
            for j in range(0,n-1):
                print(i,j)
                if board[i][j] != 'X' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    p[i][j] = 1
                    p[i][j+1] = 1
                    p[i+1][j] = 1
                    p[i+1][j+1] = 1
        print(p,board)
        for idx, k in enumerate(p):
            cnt1 = k.count(1)
            answer += cnt1
            board[idx] = ['X'] * cnt1 + [i for i in k if i != 1]
        if temp == answer: break
    return answer

m,n=4,5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board),'answer')
