# 1. 문제 요약
- case 1: 매수할 수 있으면 전체 매수
- case 2:
    - 3일 연속 올라가면 전량 매도
    - 3일 연속 내려가면 전량 매수
- 주가와 돈이 주어졌을때 얼마 N일일때는 얼마나 남는지 코드 만들기
# 2. 알고리즘
- 단순 구현
# 3. 동작순서
- case 1인 경우는 그냥 매수할 수 있으면 무조건 매수
- cas2 2인 경우는 3일씩 확인하면서 매수/매도 확인
# 4. 걸린시간
- 1시간 20분
## 4.1 왜 늦게 걸렸는지?
- 실수
    - 현재 가진돈 + 다음에 가진돈을 했어야했는데 못함
    - money와 stock 순서바꿈 (집중력문제)
- 문제의 잘못이해
    - 3일째되는 날이니까 전일대비 올라가거나 내려가는 '당일' 도 1일째에 포함한
        - ex)
           ```
           주식: 23 12 4 0 2 1 2
           오답: 1  2  3 4
           정답: 0  1  2 3
           ```
- *3일째를 어떻게 계산하는지 확인하는데 시간이 오래걸림*
## 5. 다른 사람 코드 snippet
### 5.0 내거
```python
        if previous_stock < stock:  # 계속 상승할경우
            continuous_check[0] += 1
        else:
            continuous_check[0] = 0
        
        if previous_stock > stock:  # 계속 하강하는경우
            continuous_check[1] += 1
        else:
            continuous_check[1] = 0
        if continuous_check[1] >= 3:  # 전량 매수
            smin.buy_stock(stock)
        if continuous_check[0] >= 3:  # 전량 매도
            smin.sell_stock(stock)
```
- 확실히 너무 어렵게 푼 티가난다..
### 5.1 첫번째
```c++
    for (int i = 3; i < 14; i++) {
		if (a[i - 3] < a[i - 2] && a[i - 2] < a[i - 1] && a[i - 1] < a[i]) {
			M += b * a[i];
			b = 0;
		}
		else if (a[i - 3] > a[i - 2] && a[i - 2] > a[i - 1] && a[i - 1] > a[i]) {
			int _add = M / a[i];
			b += _add;
			M -= (_add * a[i]);
		}
	}
    }
```
- 대부분이 3번째부터 연속으로 계산하였다. 확실이 이렇게하는게 직관적으로 보인다.
```java
			if(i > 0 && price[i] > price[i-1]) {
				down = 0;
				up++;
				if(up >= 3) {
					up = 0;
					s.sell(price[i]);
				}
			}
			else if(i > 0 && price[i] < price[i-1]) {
				up = 0;
				down++;	
				if(down >= 3) {
					down = 0;
					s.buy(s.seed/price[i], price[i]);
				}
			}
			else {
				up = 0; down = 0;
			}
```
- 나랑 비슷하게 푼사람. 이코드가 좀더 와닿는다.
### 5.2 두번째
