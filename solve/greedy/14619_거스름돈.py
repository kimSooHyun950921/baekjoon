#시작 09시 41분
#끝 10시 50분
#핵심: 5원으로 가장 최선의 방법구하기 (total_change - (5 * num_5won))
#      5원으로 줄 수 있는 가장 큰 값에서 하나씩 빼기
import sys


def main():
    total_change = int(sys.stdin.readline())
    num_5won = total_change // 5
    while num_5won > 0 and (total_change - (5 * num_5won)) % 2 != 0:
        num_5won -= 1
    num_2won = (total_change - (5 * num_5won)) / 2
    if (total_change - (5 * num_5won)) % 2 == 0:
        return num_5won + int(num_2won)
    else:
        return -1


if __name__ == "__main__":
    print(main())