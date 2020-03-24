# Chapter03-02
# 파이썬 심화
# 스페셜 메서드(심화 메서드)
# 클래스 안에 정의할수 있는 특별한(built-in)메서드

#클래스 예제2
class Vector(object):

    def __init__(self, *args):
        '''
        Create a vector , example : v = Vector(5,10)
        '''
        if len(args) == 0: #예외처리
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector addition of self and other.'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        if self._x == 0 and self._y ==0:
            print('Warning! 0,0 입니다!')
        return bool(max(self._x, self._y))


#Vector instance 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

#매직 메서드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1,v2,v3)

print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))

if not bool(v3):
    print('ok')

if bool(v1):
    print('ok')