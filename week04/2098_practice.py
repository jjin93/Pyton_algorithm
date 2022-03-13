import sys
input = sys.stdin.readline

def tsp(dists):
    N = len(dists)
    visited_all = (1 << N) -1
    dp = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')
    
    def find_path(last, visited) :
        if visited == visited_all :
            return dists[last][0] or INF
        if dp[last][visited] is not None :
            return dp[last][visited]
        
        tmp = INF
        for city in range(N) :
            if visited & (1 << city) == 0 and dists[last][city] != 0 :
                tmp  = min(tmp,
                           find_path(city, visited | (1 << city)) + dists[last][city])
        dp[last][visited] = tmp
        return tmp
    
    return find_path(0,1 << 0)        
if __name__ == '__main__' :
    city_num = int(input())
    dists = []
    for _ in range(city_num) :
        cost = list(map(int, input().split()))
        dists.append(cost)
        
    print(tsp(dists))    