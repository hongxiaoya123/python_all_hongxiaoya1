'''
人类：
    姓名，性别，身高，年龄，体重，体色，地址
地址类:
    国籍，省份，街道，门牌号
'''
class People:
    username = None
    sex =None
    age =None
    height =None
    weight =None
    color = None
    address =None

class Address:
    country =None
    province =None
    street =None
    door =None

adr = Address()
adr.country = "中国"
adr.province = "陕西省"
adr.street = "狄寨街道"
adr.door = "108号"

c = People()
c.username ="憨憨"
c.sex ="男"
c.age =25
c.height =175
c.weight =120
c.color ="白皮肤"
c.address =adr

print("我叫",c.username,"性别",c.sex,"年龄",c.age,"身高",c.height,"体重",c.weight,"肤色是",c.color)
print("我居住在",c.address.country,c.address.province,c.address.street,c.address.door)  # c.address  -->adr









