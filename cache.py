from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = []
    cache = deque(cache)

    if cacheSize == 0:
        answer = 5*len(cities)
        return answer

    for i in range(0,len(cities)):
        cities[i] = cities[i].upper()
    
    for city in cities:
        # cache miss
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
        # cache hit
        else:
            answer += 1
            if cache.index(city) == len(cache)-1:
                pass
            else:
                #idx = cache.index(city)
                #cache = cache[:idx] + cache[idx+1:] + cache[idx:idx+1]
                cache.remove(city)
                cache.append(city)
    return answer

cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cacheSize = 3
print(solution(cacheSize,cities))