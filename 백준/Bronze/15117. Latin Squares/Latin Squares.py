import sys

input =sys.stdin.readline

N = int(input())

m = [list(input().strip()) for _ in range(N)]

def transform_digit(char):
    if char.isalpha():
        char = ord(char) - ord('A') + 10
    else:
        char = int(char)
    return char


for i in range(N):
    is_latin=True
    check = [False] * N
    for j in range(N):
        target = transform_digit(m[i][j])
        
        if check[target]:
            is_latin = False
            break
        check[target] = True
    if not is_latin:
        print('No')
        exit(0)

for i in range(N):
    is_latin=True
    check = [False] * N
    for j in range(N):
        target = transform_digit(m[j][i])
        
        if check[target]:
            is_latin = False
            break
        check[target] = True
    if not is_latin:
        print('No')
        exit(0)

is_reduced = True
for i in range(N):
    row, col = transform_digit(m[0][i]), transform_digit(m[i][0])
    if i<10:
        if i==row and i==col:
            continue
        else:
            is_reduced = False
    else:
        if i==row and i==col:
            continue
        else:
            is_reduced = False

if is_reduced:
    print('Reduced')
else:
    print('Not Reduced')