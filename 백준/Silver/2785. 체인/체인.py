import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

need = N - 1  # 아무것도 분해 안 하면 필요한 열린 고리 개수
ans = need  # 초기 후보답
sumplus = 0  # Σ (s_i + 1)
cost = 0  # Σ s_i

for s in arr:
    sumplus += s + 1
    cost += s
    rem = max(0, need - sumplus)
    ans = min(ans, cost + rem)
    if sumplus >= need:  # 이후는 비용만 더 커지므로 조기 종료 가능
        break

print(ans)
