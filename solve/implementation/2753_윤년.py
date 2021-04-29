
# 후기: 인간적으로 이건 너무 쉬움
import sys
input = sys.stdin.readline


def main():
    year = int(input())
    if ((year % 4) == 0 and (year % 100 != 0)) or ((year % 4) == 0 and (year % 400 == 0)) :
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
