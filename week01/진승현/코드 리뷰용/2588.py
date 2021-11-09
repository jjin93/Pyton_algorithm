import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(a*int((b/10**0)%10))
print(a*int((b/10**1)%10))
print(a*int((b/10**2)%10))
print(a*b)

# 공부해볼만한것
# 0,1,2 자릿수가 자동으로 들어가게 하기
# 마지막 a*b할때 자릿수 곱하기가 자동으로 들어가서 계산되게 해볼것

