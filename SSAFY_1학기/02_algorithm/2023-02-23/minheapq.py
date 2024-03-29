# 최소힙
import heapq

hq = []

# 기본
for i in range(10):
    heapq.heappush(hq, i)

for i in range(10):
    print(heapq.heappop(hq), end=' ')
print()

# 응용
heapq.heappush(hq, (4, "4등"))
heapq.heappush(hq, (2, "2등"))
heapq.heappush(hq, (1, "1등"))
heapq.heappush(hq, (3, "3등"))

for i in range(4):
    print(heapq.heappop(hq), end=' ')
print()

# 최대 힙
for i in range(10):
    heapq.heappush(hq, (-i, i))

for i in range(10):
    print(heapq.heappop(hq), end=' ')
print()
