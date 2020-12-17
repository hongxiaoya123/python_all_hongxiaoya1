from day13.BalanceException import BalanceException
from day13.bank import Takemoney

b = Takemoney()
b.setMoney(3000)

try:
    b.money()
except BalanceException as e:
    print(e)


