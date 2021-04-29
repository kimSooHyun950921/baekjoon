import sys
input = sys.stdin.readline


def print_map(maps):
    for i in range(len(maps)):
        print(*maps[i])


def find_moved_regions(maps):
    pass


def count_move_people(maps, L, R):
    opened_regions = dict()
    count = 0
    while True:
        # 국경선 탐색
        queue = []
        is_flag = False
        for i in range(len(maps)):
            for j in range(0, len(maps)-1):
                regions_diff = abs(maps[i][j] - maps[i][j+1])
                if regions_diff >= L and regions_diff <= R:
                    opened_regions[(i, j)] = (i, j)
                    opened_regions[(i, j+1)] = (i, j+1)
                    queue.append((i, j))
                    is_flag = True
                    break
            for j in range(0, len(maps)-1):
                if is_flag:
                    break
                regions_diff = abs(maps[j][i] - maps[j+1][i])
                if regions_diff >= L and regions_diff <= R:
                    opened_regions[(j, i)] = (j, i)
                    opened_regions[(j+1, i)] = (j, i)
                    queue.append((i, j))
                    is_flag = True
                    break
            if is_flag:
                break
        
        #bfs
        while len(queue) > 0:
            i, j = queue.pop(0)
            for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                ni = i + dr
                nj = j + dc
                if 0 <= ni < len(maps) and 0 <= nj < len(maps):
                    if opened_regions.get((ni, nj), None):
                        continue
                    regions_diff = abs(maps[ni][nj] - maps[i][j])
                    if regions_diff >= L and regions_diff <= R:
                        queue.append((ni, nj))
                        opened_regions[(ni, nj)] = (ni, nj)  

        print(opened_regions)
        print_map(maps)
        if len(opened_regions) == 0:
            break
        # 값 모두 합하기
        value = 0
        for region in list(opened_regions.keys()):
            i, j = opened_regions[region]
            value += maps[i][j]
        # 값 변환
        avg = int(value / len(opened_regions.keys()))
        for region in list(opened_regions.keys()):
            i, j = opened_regions[region]
            maps[i][j] = avg
        count += 1
        print("avg", avg)
        del opened_regions
        opened_regions = dict()
    return count


def main():
    maps = list()
    N, L, R = map(int, input().rstrip().split(" "))
    for _ in range(N):
        maps.append(list(map(int, input().rstrip().split(" "))))  
    answer = count_move_people(maps, L, R)
    print(answer)

if __name__ == "__main__":
    main()

