#입력 먼저
from collections import deque
import sys

def bfs(x, y, safe_area):
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1  # 시작 좌표 방문 마크
    
    
    while len(queue) :
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <N and 0 <= ny < N :
                if graph[nx][ny] > safe_area and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] =1
                    
                    
        # q.deque를 가져와서 x,y에 넣고 그다음 상하좌우 확인하고 계속 진행하면 되는데


input = sys.stdin.readline


N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
# graph_min = min(map(min, graph)) # 지역 최저 높이
graph_max = max(map(max, graph)) # 지역 최고 높이

dx = [0,0,-1,1] # 상하좌우 순 변량 체크
dy = [1,-1,0,0]

max_safe_area = 0  # 안전 영역 0일 수도 있다

for safe_area in range(0, graph_max): #강수량 높이 조건
    visited = [[0]*N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            # 필터링 : 이 if가 돈다는 것은 지형 높이가 강수량 높이보다 높거나 방문한 적이 없을때 
            if graph[i][j] > safe_area and visited[i][j] ==0:
                 
                bfs(i,j,safe_area)
                temp += 1 #bfs가 한번 끝날때마다 안전영역 체크 +1
    
    if temp > max_safe_area:
        max_safe_area = temp
        

print(max_safe_area)