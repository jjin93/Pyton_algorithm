import sys
n = int(sys.stdin.readline())
word = set()

for i in range(n):
    word.add(sys.stdin.readline().strip())
word = list(word)
word.sort() #알파벳 순으로 정렬
word.sort(key = len) #정렬 된 거에 단어 길이별로 정렬
# sort함수 안에서 어떻게 정렬되는지 공부

print("\n".join(word))


