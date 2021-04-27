# 시작 15시 55분
# 문제해석시간 15시 55분
# 코드생각시간 04시 04분
# 코드만드는시간 04시 08분
# 디버깅시간 04시 30분
# 디버깅 오래걸림 & 8진수 2진수 바꾸는 법 찾아봄

def make_octal_bin(partial_bin):
    while len(partial_bin) < 3:
        partial_bin = '0' + partial_bin
    return partial_bin


def main():
    octal = input()
    binary = ''
    for num in octal:
        num = int(num)
        partial_bin = ''
        while num > 0:
            masking = num & 1
            num = num >> 1
            partial_bin = str(masking) + partial_bin
        binary += make_octal_bin(partial_bin)
    while len(binary) > 1 and binary[0] == '0':
        binary = binary[1:]
    return binary


if __name__ == "__main__":
    print(main())
