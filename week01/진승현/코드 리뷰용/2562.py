# 첫째줄 부터 9번째 줄까지 입력
# 그 중에서 최댓값 구하고 몇번째 입력되었던 수 인지 찾아라
import sys
number = []
for i in range(0,9):
    X = int(sys.stdin.readline())
    number.append(X)

print(max(number))
print(number.index(max(number))+1)    