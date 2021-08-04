# expected match table

def solution(n,a,b):
    x = [0] * n
    x[a-1], x[b-1] = 1, 1
    cnt = 1
    temp = []

    while True:
        n = n//2
        for i in range(0,n):
            if x[i*2] == 0 and x[i*2+1] == 0:
                temp.append(0)
            elif  x[i*2] == 1 and x[i*2+1] == 1:
                return cnt
            else:

                temp.append(1)
        x = temp
        temp = []
        cnt += 1

n = 8
a = 4
b = 7
print(solution(n,a,b))