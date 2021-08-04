from collections import deque

def solution(s):
    x = list(s)
    x = deque(x)
    y = x
    k = 1
    new = []
    length = len(s)
    idx = 0

    while True:
        if len(x) >= k:
            for _ in range(0,k):
                new.append(x.popleft())
        else:
            for _ in range(0,len(x)):
                new.append(x.popleft())
        print(new,k)
        k += 1
        new = []
        x = y
        if k == int(len(x)//2+1): break


s = "aabbaccc"
print(solution(s))