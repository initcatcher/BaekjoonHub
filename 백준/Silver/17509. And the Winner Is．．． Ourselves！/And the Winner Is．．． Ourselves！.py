import sys

input = sys.stdin.readline
total = 0

arr = []
p = []
for _ in range(11):
    t, v = map(int, input().split())
    arr.append(t)
    p.append(v)
arr.sort()
time_sum = sum((11 - i) * d for i, d in enumerate(arr))

penelty = 20 * sum(p)

print(time_sum + penelty)
