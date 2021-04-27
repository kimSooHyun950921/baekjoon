import sys
input = sys.stdin.readline
# 시작 1시 17분
# 코드생각시간 1시 27분
# 코드만드는시간 1시 ??분
# 디버깅시간 1시 49분 
# 한번더 풀때는 visited로 사용해볼것! 어떨진 모르겠음..
NUMBER = 0
COMBIN = 0


def permutation(numbers, seq, count):
    global NUMBER
    global COMBIN
    if len(seq) == COMBIN:
        print(*seq)
        return
    for _ in range(1, len(numbers)+1):
        num = numbers.pop(0)
        seq.append(num)
        sorted_numbers = sorted(numbers)
        permutation(sorted_numbers, seq, count)
        numbers.append(num)
        seq.pop()


def main():
    global NUMBER
    global COMBIN
    NUMBER, COMBIN = map(int, input().strip().split())
    permutation(list(range(NUMBER+1))[1:], [], 0)


if __name__ == "__main__":
    main()