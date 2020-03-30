# Chapter03-03
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# <<<Namedtuple 실습>>>
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 1. 일반적인 튜플 사용하여 두 점 사이의 거리 구하기
pt1 = (1.0, 5.0)
pt2=  (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1])** 2) #튜플은 인덱스로 접근!
print(l_leng1) #3.8078865529319543


# 1.보다 좋은 방법 ...  2. 네임드 튜플을 사용하여 두 점 사이의 거리 구해보기
# 네임드 튜플은 딕셔너리의 성질을 가지고 있는 튜플이다.
#즉, 인덱스로도 접근가능하고, 키(key)로도 접근 가능하다.
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point','x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

#유연하게 접근 가능(키로도, 인덱스로도 접근 가능!)
print(pt3) #Point(x=1.0, y=5.0)
print(pt3.x) #1.0
print(pt3[1])  #5.0
print(pt4)  #Point(x=2.5, y=1.5)
print(pt4[0])  #2.5
print(pt4.y)  #1.5

#일반적인 튜플의 방법과 출력 결과가 같지만, 가독성이 매우 높기 때문에 namedtuple은 꼭 알고 있어야 한다.
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y)** 2) #튜플은 인덱스로 접근!

print(l_leng2)  #3.8078865529319543


# 3. 네임드 튜플 선언 방법(4가지 모두 가능.. 매우 유연하다)
Point1 = namedtuple('Point','x y')  #1번. 위에서 했던 방법
Point2 = namedtuple('Point', ['x', 'y']) #2번
Point3 = namedtuple('Point','x, y') #3번
Point4 = namedtuple('Point','x y x class', rename=True) #기본값은 False이다.
# True로 바꾸면 키가 중복되거나 예약어일때도 선언 가능하다.


#출력
print(Point1, Point2, Point3, Point4) #<class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

#Dict to Unpacking
temp_dict = {'x' : 75, 'y': 55} #딕셔너리



#객체 생성(이 방법들은 모두 가능한 방법들..매우 유연하다)
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
#unpacking 할때 : 튜플은 * 한개, 딕셔너리는 ** 두개가 붙는다.
p5 = Point3(**temp_dict)


print()

print(p1)   #Point(x=10, y=35)
print(p2)   #Point(x=20, y=40)
print(p3)   #Point(x=45, y=20)
#rename 테스트
print(p4)   #Point(x=10, y=20, _2=30, _3=40)
#딕셔너리를 언패킹
print(p5)   #Point(x=75, y=55)

#사용
print(p1[0] + p2[1]) #인덱스(index)로 접근   # 50
print(p1.x + p2.y) #키(key)로 접근  # 50

#Unpacking
x,y = p3
print(x, y) #45 20

# ** 네임드 튜플 메서드 **
temp = [52, 38]

#_make() : 리스트를 네임드 튜플로 바꾸어주는 메서드 (값 개수가 같아야 됨)
p4 = Point1._make(temp)
print(p4) #Point(x=52, y=38)


#_fields : 필드 네임을 확인할 수 있는 메서드 (key 값을 조회한다.)
print(p1._fields, p2._fields, p3._fields, p4._fields) #('x', 'y') ('x', 'y') ('x', 'y') ('x', 'y')


#중요! _asdict() : OrderedDict 변환
#네임드 튜플 >> (정렬된)딕셔너리로 반환  (원래 딕셔너리는 정렬 안되어있음)
print(p1._asdict())  #{'x': 10, 'y': 35}

#------------------------------------------------------------------
# 실 사용 실습!!

# 반에는 20명, 4개의 반이 있다 (A,B,C,D반). 학생들의 리스트를 만들기! (A1, A2, A3 .....)
Classes = namedtuple('Classes','rank number')

#1. 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

#2. List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students)) #80명
print(students) #80명의 학생 리스트들 모두 출력

#추천(1. 과 2. 를 합쳐서)
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(len(students2)) #80명
print(students2) #80명의 학생 리스트들 모두 출력


print()

#출력
for s in students2:
    print(s)