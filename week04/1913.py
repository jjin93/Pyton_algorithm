import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    N = int(input())
    conference_time = []    
    for _ in range(N) :
        start, end = map(int, input().split())
        conference_time.append((start, end))
        
    conference_time = sorted(conference_time, key = lambda x: x[0])
    conference_time = sorted(conference_time, key = lambda x: x[1])    
    count = 0
    end = 0
    for start_time, end_time in conference_time :
        if start_time >= end:
            count += 1
            end = end_time
    
    print(count)        