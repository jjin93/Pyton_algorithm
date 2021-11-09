##n개의 정수를 배열하는 방법
import sys,itertools
N = int(sys.stdin.readline())
arr = []*N
arr = list(map(int,sys.stdin.readline().split()[:N]))
arr.sort()

arr2 =list(itertools.permutations(arr,N))

res = 0

for i in range(len(arr2)):
    cur = 0
    for j in range(0, N-1): 
        cur += abs(arr2[i][j]- arr2[i][j+1])

        if cur > res:
            res = cur
print(res)   


        