# 문제의 핵심
- 구현
- 인덱싱, 규칙처리
# 알고리즘 
- 중앙부터 2, 2, 3, 3... 개씩 넓혀나간다.
- 방향은 매방향 전환
- 0번은 반복되므로 무시
- 마지막은 3번 반복
# code Snippet
```python
for i in range(2, N+1):  # 회전전 숫자쓰는 횟수 2, 2, 3, 3, 4, 4, 5, 5
        loop = 2 if i < N else 3  # 같은 숫자 횟수는 2번씩 마지막은 3번 반복
        for l in range(loop):   
            for j in range(i):  # 회전전 숫자 연속으로 쓰는횟수 
                if j == 0: # 처음은 마지막과 겹치므로 넘어감
                    continue
                srow += direction[dcount % 4][0]  #매방향 전환
                scol += direction[dcount % 4][1]
                snail[count] = (srow, scol)  
                count += 1
            dcount += 1
```
# 복기
- 그래도, 어제보다 시간이 덜걸리지 않았을까, 
- 적어도 10분 안에 풀수있도록 반복연습해야한다.
- dict에 넣었는데, dict에 넣지 않고 바로 배열에 넣을 수 있을듯하다.