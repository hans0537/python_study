T = int(input())

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:      # 단어를 넣을 수 있는 공백
                cnt += 1
            else:           # 칸 없음!
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N + 1)]

    # arr 와 arr_t로 각각 개수를 계산
    arr_t = list(map(list,zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{tc} {ans}')