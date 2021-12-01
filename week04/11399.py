import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    N = int(input())
    time_list = list(map(int,input().split()))
    
    time_list.sort()
    result = 0
    
    for i in range(len(time_list) + 1) :
        
        result += sum(time_list[0:i])
        
    print(result)    
        