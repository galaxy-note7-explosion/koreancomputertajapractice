import random
import time

with open('shorthangul.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
m = random.choice(data)
count = len(m)
print(m)
start = time.time()
m1 = str(input())
end = time.time()
sec = end - start
perfect = 0
for i in range(count-1):
    if m[i] == m1[i]:
        perfect += 1
print("걸린 시간 :", int(sec))
print("타수 :", int(perfect * 60 / sec))
print("정확도 :", int(perfect / count * 100))
