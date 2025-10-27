import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

old = [int(input()) for _ in range(n)]
new = [int(input()) for _ in range(m)]

x, y = 0, 0

# 비용별로 처리 (비용 = (i+1) + (j+1))
for cost in range(2, n + m + 1):
    # cost = i + j + 2, 따라서 i + j = cost - 2
    target_sum = cost - 2
    
    for i in range(n):
        j = target_sum - i
        if 0 <= j < m:
            # i층에서 j층으로 옮기기
            move = min(old[i], new[j])
            if move > 0:
                old[i] -= move
                new[j] -= move
                x += move
                y += cost * move

print(x, y)