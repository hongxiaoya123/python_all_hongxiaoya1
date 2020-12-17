from day13.AgeException import AgeException
from day13.person import person

p = person()
p.setAge(2)
try:
    p.age()
except AgeException as e:
    print(e)



