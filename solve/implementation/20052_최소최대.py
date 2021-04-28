
# 후기: 인간적으로 이건 너무 쉬움ㅠㅠ
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    for _ in range(N):
        _  = int(input())
        num_list = list(map(int, input().rstrip().split(" ")))
        print(min(num_list), max(num_list))


if __name__ == "__main__":
    main()
