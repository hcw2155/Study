def solution(m, n, board):
    answer = 0
    p = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    new = []
    for i in range(0,m):
        tmp = []
        for j in range(0,n):
            tmp.append(board[i][j])
        new.append(tmp)

    while True:
        check = []
        for i in range(0,m-1):
            for j in range(0,n-1):
                # if new[i][j] in block:
                if new[i][j] != 'X' and new[i][j] == new[i+1][j] == new[i][j+1] == new[i+1][j+1]:
                    check.append((i,j))
                    check.append((i,j+1))
                    check.append((i+1,j))
                    check.append((i+1,j+1))
        if len(check) == 0:
            break
        else:
            answer += len(set(check))
            for c in check:
                new[c[0]][c[1]] = 'X'
            for c in reversed(check): # bottom-up
                check_n = c[0] - 1
                put_n = c[0]
                while check_n >= 0:
                    if new[put_n][c[1]] == 'X' and new[check_n][c[1]] != 'X':
                        new[put_n][c[1]] = new[check_n][c[1]]
                        new[check_n][c[1]] = 'X'
                        put_n -= 1
                    check_n -= 1
    return answer

m,n=4,5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board),'answer')
