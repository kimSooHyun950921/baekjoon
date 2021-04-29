# 시작시간 3시 22분
# 끝시간 
class Person:
    def __init__(self, money):
        self.num_stock = 0
        self.money = money
   
    def buy_stock(self, stock):
        if self.money > 0 and self.money >= stock:
            self.num_stock += self.money // stock
            self.money = self.money % stock


    def sell_stock(self, stock):
        if self.num_stock > 0:
            self.money += stock * self.num_stock
            self.num_stock = 0

    def calc_asset(self, stock):
        return self.money + stock * self.num_stock


def main():
    N = int(input())
    stocks = list(map(int, input().rstrip().split(" ")))
    smin = Person(N)
    jhyun = Person(N)

    continuous_check = [0, 0]
    previous_stock = stocks[0]
    for stock in stocks:
        jhyun.buy_stock(stock)
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
        previous_stock = stock

    jhyun_asset = jhyun.calc_asset(previous_stock)
    smin_asset = smin.calc_asset(previous_stock)
    if jhyun_asset > smin_asset:
        print("BNP")
    elif jhyun_asset < smin_asset:
        print("TIMING")
    else:
        print("SAMESAME")


if __name__ == "__main__":
    main()