#시작 09시 10분
#끝 09시 41분
import sys
def main():
    num_of_computers = int(sys.stdin.readline())
    num_of_com_ssang = int(sys.stdin.readline())
    computers = dict()
    answer = set()
    queue = list()
    visited = [False] * (num_of_computers + 1)
    for _ in range(num_of_com_ssang):
        i, j = map(int, sys.stdin.readline().strip().split(" "))
        if computers.get(i) is None:
            computers[i] = list()
            computers[i].append(j)
        else:
            computers[i].append(j)
        if computers.get(j) is None:
            computers[j] = list()
            computers[j].append(i)
        else:
            computers[j].append(i)
            
        if i == 1:
            queue.append(j)
            visited[i] = True
            visited[j] = True
    while len(queue) > 0:
        #print(queue, visited)

        computer = queue.pop(0)
        answer.add(computer)
        if computers.get(computer) is not None:
            for i in computers[computer]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
    print(len(answer))
    #print(answer)
            


if __name__ == "__main__":
    main()