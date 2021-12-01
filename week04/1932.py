import sys
input = sys.stdin.readline


if __name__ == '__main__' :
    
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int,input().split())))
        
    for i in range(1, n):
        for j in range(i + 1) :
            if j == 0 :
                triangle[i][j]  = triangle[i][j] + triangle[i-1][j]
            elif i == j :
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i-1][j],
                                     triangle[i][j]+triangle[i-1][j-1])
                
    print(max(triangle[n-1]))            