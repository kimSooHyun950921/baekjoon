
## 출처: 백준 아이디 sky9739
def TIMING(number):
  sum = 0
  for i in range(len(price)):
    
    if i >= 3 :
      if price[i] > price[i-1] and price[i-1] > price[i-2] and price[i-2] > price[i-3]:
        if sum != 0:        
          number = sum * price[i]
          sum = 0

      elif price[i] < price[i-1] and price[i-1] < price[i-2] and price[i-2] < price[i-3]:
        sum += number // price[i]
        number = number - price[i] * (number // price[i])
    
  return number + (sum * price[13])      

def BNP(number):
  sum = 0
  for i in price:
    sum += number // i
    number = number - i * (number // i)
    
  return number + (sum * price[13])

n = int(input())


price = list(map(int, input().split()))

if BNP(n) > TIMING(n):
  print('BNP')
elif BNP(n) < TIMING(n):
  print('TIMING')
else:
  print('SAMESAME')