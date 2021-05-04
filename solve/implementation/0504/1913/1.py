# 시작 10시 22분
# 끝 11시 43분
# 1시간 21분
import sys
input = sys.stdin.readline


def solution(N):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    srow, scol = N//2, N//2
    snail = {1:(srow, scol)}
    count, dcount = 2, 0
    for i in range(2, N+1):
        loop = 2 if i < N else 3
        for l in range(loop):
            for j in range(i):
                if j == 0:#
                    continue
                srow += direction[dcount % 4][0]
                scol += direction[dcount % 4][1]
                snail[count] = (srow, scol)
                count += 1
            dcount += 1
    return snail


def print_grid(snail, N):
    grid = [[0]*N for i in range(N)]
    for key, value in snail.items():
        grid[value[0]][value[1]] = key
    
    for i in range(N):
        print(*grid[i])


def get_axis(snail, nth):
    return snail[nth][0], snail[nth][1]


def main():
    N = int(input())
    nth = int(input())
    snail = solution(N)

    print_grid(snail, N)
    axis = get_axis(snail, nth)
    print(axis[0]+1, axis[1]+1)


if __name__ == "__main__":
    main()
