import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    
    N = map(int,input().strip())
    N = list(N)
    
    if 0 not in N or sum(N) % 3 != 0:
        print(-1)
        exit(0)
    else :
                
        N = sorted(N, reverse= True)
        print(*N,sep='')
        
        
    
    
    
    