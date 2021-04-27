import sys
input = sys.stdin.readline
# 시작 10시 47분
# 문제해석시간 10시 48분
# 코드생각시간 10시 57분
# 코드만드는시간 11시 12분
# 디버깅시간 12시 13분
# 딴짓을 너무 많이 함 잡생각이 많았음

NUMBER = 0
COMBIN = 0


def combination(start, seq, count):
    global NUMBER
    global COMBIN
    if count == COMBIN:
        print(*seq)
        return
    for i in range(start, NUMBER+1):
        seq[count] = i
        combination(i+1, seq, count+1)


def main():
    global NUMBER
    global COMBIN
    NUMBER, COMBIN = map(int, input().strip().split())
    combination(1, [0]*COMBIN, 0)


if __name__ == "__main__":
    main()