from collections import defaultdict

def LRU(key, time, cacheSize, current_cache_size, cache):
    
    if cacheSize == 0:
        return 5
    
    if key in cache:
        cache[key] = time
        return 1
    else:
        if current_cache_size[0] < cacheSize:
            current_cache_size[0] += 1
        else:
            list_cache = list(cache.items())
            list_cache.sort(key=lambda x: (x[1], x[0]))
            cache.pop(list_cache[0][0], None)
        
        cache[key] = time
        return 5

def solution(cacheSize, cities):
    answer = 0
    cache = defaultdict(int)
    current_cache_size = [0]
    
    for time, city in enumerate(cities):
        answer += LRU(city.lower(), time, cacheSize, current_cache_size, cache)
    
    return answer

if __name__ == "__main__":

    cacheSize = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
    print(solution(cacheSize, cities))
    