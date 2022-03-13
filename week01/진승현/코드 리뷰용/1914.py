import sys
def hanoi(n,from_post, goal_post, help_post):
    if n ==1: #원반 1개를 옮기는 문제면 그냥 옮기면 됨, 어디든 갈수 있다.
        print(from_post, goal_post)
        return #여기가 재귀함수 탈출 조건

    #원반 n-1개를 help_post로 이동(goal_post를 보조 기둥으로)
    #왜? 2가 목표로 가기 위해선 1이 help_post로 가야한다
    # 그다음 2가 goal_post로 간다.
    hanoi(n-1,from_post, help_post, goal_post)
    #가장 큰 원반을 goal_post로 이동
    print(from_post, goal_post)
    #help_post에 있는 원반 n-1개를 goal_post로 이동(from_post를 보조 기둥으로)
    hanoi(n-1,help_post,goal_post,from_post)

N = int(sys.stdin.readline())
print(2**N-1)
if(N < 20):
    hanoi(N,1,3,2)
        



    
    
         