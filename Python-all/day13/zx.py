from day13.User import User
from day13.UserException import UserException

u = User()
u.setAge(34)
u.setUsername("旺财")

u1 = User()
u1.setAge(34)
u1.setUsername("大橘")
try:
    u.compare(u1)
except UserException as e:
    print(e)
