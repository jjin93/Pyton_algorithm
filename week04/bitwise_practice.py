from random import randint

def nth_bit_on(n):
    return(1 << n)
#파이썬의 bin 함수는 인자가 하나일 때는 주어진 정수를 2진수 형태의 문자열로 반환한다. 앞에 붙은 ‘0b’는 식별자라고 생각하면 된다.
print(bin(nth_bit_on(0)))
print(bin(nth_bit_on(1)))
print(bin(nth_bit_on(2)))
print(bin(nth_bit_on(3)))
print(bin(nth_bit_on(4)))
print(bin(nth_bit_on(5)))

#혹시나 착각하지 말자. 비트를 셀 때 0번째를 포함해야 한다.
print()

#어떤 정수의 nth번째 비트가 켜져 있는지, 꺼져 있는지 확인하는 함수.
def get_nth_bit(n, nth) :
    #이 식의 핵심은 n & (1 << nth)이다.
    return 1 if n & (1 <<nth) else 0
    # 확인할 n과, nth번째 비트를 켠 수를 & 연산하면 답이 0일 시에는 0, 아닐 시에는 다른 값이 나올 것이다.
print('10진수 100을 2진수로 변환한 값 :', bin(100))
print(get_nth_bit(100,2))
print(get_nth_bit(100,3))

print()
# 그냥 n을 반환하지 않고 삼항 연산자를 쓴 이유
def get_nth_bit_error(n, nth):
    return n & (1 << nth)
# 만약 비트가 꺼져 있다면 0이 반환된다. 근데 0이 아니라면, 다시 말해 해당 nth 번째 비트가 켜져 있다면 반환되는 값은 0이 아니라 nth번째 비트가 켜진 정수다.
# 이 값은 nth이 2, 3, 4임에 따라 4, 8, 16 등의 값이 된다. 그래서 0 아니면 반드시 1을 반환하도록 삼항연산자를 쓸 수 밖에 없다. 다른 비트 연산에서도 조심!
print('10진수 100을 2진수로 변환한 값 :', bin(100))
print(get_nth_bit_error(100,2))
print(get_nth_bit_error(100,3))

print()

# (1 << n) - 1: n개의 비트 모두 켜기
# . 앞선 절에서는 n번째 비트를 켜는데 그때는 0번째를 고려해야 해서 헷갈릴 수도 있지만 2장의 내용은 단순히 ‘주어진 개수만큼 비트를 켠다’기 때문에 더 직관적으로 와닿는다.

print(bin((1 << 1) - 1))
print(bin((1 << 2) - 1))
print(bin((1 << 3) - 1))
print(bin((1 << 4) - 1))
print(bin((1 << 8) - 1))
# 우리 모두, '10000 - 1 = 9999'라는 것을 안다. 근데 이 식은 이번 절의 식과 매우 비슷하다는 것을 느낄 수 있다. 
# 10진수 식에서 10000에서 1을 빼면 오른쪽부터 시작해서 0인 부분은 9(10-1)로 치환되고 0이 아닌 부분까지 진행하며 최종적으로 0이 아닌 처음 자리값을 1 낮춘다. 

# 간단한 비트 마스킹
# 비트 마스크란 어떤 숫자에 마스크라고 불리는 비트값을 비트 연산해서 숫자의 특정 비트 구간값을 변경시키거나, 그 값을 추출하는 등의 행위를 말한다.

# 주어진 수의 오른쪽 끝에서 n개의 비트값을 추출하는 기능을 만들자.

def get_trailing_bits(n, count):
    return n & ((1 << count) - 1)

N = randint(1, 2 ** 32)
last_4_bits = get_trailing_bits(N, 4)

print('N은', N, ', 2진수로는', bin(N), '입니다.')
print('이때 N의 마지막 4개의 비트는', '{:04b}'.format(last_4_bits), '입니다.')

print()
# 유용한 몇가지 비트 연산 트릭, 알고리즘 문제에서 쓸모 있거나, 실제 프로그램 개발에서 써먹을 수 있는 것을 의미한다.
# 정수의 2의 지수승 여부 확인하기

def is_exp_binary(n):
    return n & (n - 1) == 0

print(1, is_exp_binary(2 ** 0))
print(2, is_exp_binary(2 ** 1))
print(4, is_exp_binary(2 ** 2))
print(1024, is_exp_binary(2 ** 10))

print(3, is_exp_binary(3))
print(15, is_exp_binary(15))
print(101, is_exp_binary(101))
print(1000, is_exp_binary(1000))
print()
# 2진수에서 1비트의 개수 구하기 - 어떤 0이상의 n을 2진수화했을 때, 켜진(값이 1인) 비트의 개수는 몇개 일까?

def count_bit(n):
    return n % 2 + count_bit(n // 2) if n >= 2 else n
print('1000은 2진수로', bin(1000), '이고, 1의 개수는', count_bit(1000), '개입니다.')
print()

# 꽤나 괜찮은 방법이지만, 굳이 지적하자면 단점이 몇가지 있다.
# 1. 직관적이지 않다. ( 이 함수는 비트연산자가 쓰지 않기 때문에 '각 비트자릿수의 0/1여부를 확인한다.' 는 개념이 직관적이지 않다.)
# 2. 상대적으로 느리다.(사칙연산에서 더하기,빼기, 곱하기에 비해 나누기,나머지 연산은 상대적으로 느리다.)

def bit_count(n):
    k = 0
    count = 0

    while n >= (1 << k):
        if n & (1 << k) != 0:
            count += 1
        k += 1

    return count

print('1000은 2진수로', bin(1000), '이고, 1의 개수는', bit_count(1000), '개입니다.')
print()

# Boolean 값 Toggle 하기( 비트가 on상태면 off로 꺼버리고, off상태면 on상태로 바꾸는 작업)
onoff = True
onoff ^= True
print(onoff)

onoff = False
onoff ^= True
print(onoff)
print()

# 집합론과 비트의 만남 - 비트 연산이 집합론과 접점을 가지고 있음을 깨닫고 통찰한 적 있다.먼저 어떤 2진수를 집합으로 표현해보고, 그 표현을 바탕으로 비트 집합의 차집합 예제를 통해 둘의 접점을 확인하자.
# 2진수의 집합 표현 : 핵심은 특정 비트값 1 또는 0에 집중하는 것이 아니라 2진수 n에서 1로 켜져 있는 k번째 자릿값을 집합의 원소로 하는 것이다. 

def diff(n, d):
    return n & ~(1 << d)
# &는 비트 AND 연산자으로 교집합을 의미하는  집합 연산자와 대응된다.
# (1 << d)는 앞서 살펴봤듯 d 번째 비트를 켠다를 의미한다.
# (1 << d)는 비트 여집합 연산자로 C9 여집합 연산자와 대응된다.

print(15, '는 ', bin(15), '이고 여기서 ', 2, '번째 비트 집합을 빼면 ', bin(diff(15, 2)), '이 됩니다.', sep='')
print(32, '는 ', bin(32), '이고 여기서 ', 5, '번째 비트 집합을 빼면 ', bin(diff(32, 5)), '이 됩니다.', sep='')
print(100, '는 ', bin(100), '이고 여기서 ', 5, '번째 비트 집합을 빼면 ', bin(diff(100, 5)), '이 됩니다.', sep='')
print(210, '는 ', bin(210), '이고 여기서 ', 4, '번째 비트 집합을 빼면 ', bin(diff(210, 4)), '이 됩니다.', sep='')
