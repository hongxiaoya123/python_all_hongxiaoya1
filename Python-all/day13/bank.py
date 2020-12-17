from day13.BalanceException import BalanceException
class Takemoney:
    __money = None

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def money(self):
        if self.__money <= 3000:
            print(self.__money)
        else:
            raise BalanceException("余额不足!")
