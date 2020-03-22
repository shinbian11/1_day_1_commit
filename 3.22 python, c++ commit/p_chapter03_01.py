# Chapter 03-01
# 매직 메서드 (스페셜 메서드)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심! -> 1. 시퀀스(Sequence), 2. 반복(Iterator), 3. 함수(Functions), 4. 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

#기본형
print(int)
print(float)

#모든 속성 및 메서드 출력
print(dir(int))
print(dir(float))

n = 10
print(n+100)
print(n.__add__(100)) #내부적으로 __add__가 호출됨

#print(n.__doc__)
print(n.__bool__(), bool(n)) #0이 아니니까 true

print(n * 100)
print(n.__mul__(100)) #내부적으로 __mul__이 호출됨

print()
print()

#클래스 예제1
class Fruit:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    def __str__(self):
        print('Called >> __str__')
        return 'Fruit class Info: {} , {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):   #대소비교
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False

s1 = Fruit('Orange',7500)
s2 = Fruit('Banana',3000)

#일반적인 계산
#print(s1._price + s2._price)
print(s1 + s2) #__add__함수가 호출됨

#매직메서드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2) #sub함수 호출됨. self 에는 s1이, x에는 s2가 들어간다.
print(s2 - s1)
print(s1)
print(s2)