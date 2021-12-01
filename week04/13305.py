import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    N = int(input())
    roads = list(map(int,input().split()))
    gas_station = list(map(int,input().split()))
    
    gas_value = 10**9 + 1
    gas_road = 0
    result = 0
    for i in range(N-1) :
        if gas_station[i] < gas_value :
            result += gas_value * gas_road
            gas_road = 0
            gas_value = gas_station[i]
            gas_road += roads[i]
        
        else :
            gas_road  += roads[i]        
    
    result += gas_road * gas_value
    print(result)                        