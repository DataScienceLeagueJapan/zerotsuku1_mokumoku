#1.3.1　算術計算
print(1+2)
print(1-2)
print(4*5)
print(7/5)
print(3**2)

#1.3.2　データ型
print(type(10))
print(2.718)
print("hello")

#1.3.3　変数
x = 10
print(x)
x = 100
print(x)
y = 3.14
print(x*y)
print(type(x*y))

#1.3.4　リスト型
a = [1,2,3,4,5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a)
print(a)
print(a[0:2])
print(a[1:])
print(a[:3])
print(a[:-1])
print(a[:-2])

#1.3.5ディクショナリ
me = {'height':100}
print(me['height'])
me['weight'] = 70
print(me)

#1.3.6 ブーリアン
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)

#1.3.7 if文
hungry = True
if hungry:
    print("Im hungry")
else:
    print("Im not hungry")
    print("Im sleepy")
    
#1.3.8 for文
for i in [1,2,3]:
    print(i)
    
#1.3.9 関数
def hello():
    print("Hello World!")
hello()

def hello(object):
    print("Hello "+object+"!")
hello("cat")

#1.4.1は省略

#1.4.2 クラス
class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized!!")
    def hello(self):
        print("Hello "+self.name+"!")
    def good_bye(self):
        print("Good-bye "+self.name+"!")
m = Man("David")
m.hello()
m.good_bye()

#以上が基礎事項
        
        
    
    