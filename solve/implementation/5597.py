def main():
    submitted = [False] * 30
    for i in range(28):
        N = int(input())
        submitted[N-1] = True
    for i in range(30):
        if not submitted[i]:
            print(i+1)
    print(submitted)

if __name__ == "__main__":
    main()