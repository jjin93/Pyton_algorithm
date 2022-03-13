# 반복문을 가지고 1억번 계산해서 구할수도 있지만 비 효율적이다. 이항정리를 이용하면 엄청 빠른시간에 값을 구할 수 있다.
import sys

# def snail(A,B,V):
#     y =0
#     for x in range(1,V):
#         if( V != y):
#             y += A
#         else :
#             return x    
#         if( V != y):
#             y -= B
#         else :
#             return x    

        

A,B,V = map(int,sys.stdin.readline().split())
# d =0
# h =0
d = (V-B)/(A-B)
print(int(d) if d == int(d) else int(d)+1)
# while 1:
#     d+1
#     # 이항정리
#     if A*d-B*(d-1)>=V:
#         break
    
# print(A,B,V)
# print((snail(A,B,V)))    