import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y) :
    
    if x ==(row-1) and y == (col- 1) :
        # 목적지에 도착하고 1을 반환, 이 값은 check리스트에 들어간다.
        return 1
    # check가 0 이면 목적지까지 갈수 없는 경로이므로 바로 리턴!!
    if check[x][y] != -1 :
        return check[x][y]
    # 이동할 때 마다 0으로 설정
    check[x][y] = 0
            
    for i in range(4) :
        
        new_x , new_y = x + dx[i] , y + dy[i]
        if 0 <= new_x < row and 0 <= new_y < col:
            if maps[new_x][new_y] < maps[x][y]:
                
                check[x][y] += dfs(new_x,new_y)
    return check[x][y]    

if __name__ == '__main__' :
    row, col = map(int,input().split())
    maps = []
    for i in range(row) :
        maps.append(list(map(int,input().split())))
    # 방문 체크할 리스트 -1로 초기화
    check =[[-1]*col for _ in range(row)]
    print(dfs(0, 0))
    