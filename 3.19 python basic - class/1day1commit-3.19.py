#3.19 1 day 1 commit
# 이 파일은 https://shinbian11.tistory.com/38 에서도 볼수 있습니다.
'''
[클래스]

> 함수나 변수들을 모아 놓은 집합체

[인스턴스]

> 클래스에 의해 생성된 객체
> 인스턴스 각자 자신의 값을 가지고 있다. => 클래스가 붕어빵 틀이면, 인스턴스(객체)는 그 틀로 찍어내는 붕어빵 틀이다.
'''

'''
[is 연산]
> 인스턴스들이 같은 인스턴스인지를 알아 볼 수 있는 명령어이다.
-> 사용법 : if(list1 is list2) : list1 과 list2가 같은 인스턴스인지? 라고 묻는 문장
'''

#is 연산 예시
list1 = [1,2,3]
list2 = [1,2,3]

if list1 is list2:
    print('list1과 list2는 같은 인스턴스이다!')
else:
    print('같은 인스턴스가 아니다!')

#list1과 list2의 값은 같지만(list1 == list2)
#list1과 list2는 같은 인스턴스는 아닙니다.(if list1 is list2  => false)
'''
클래스 만드는 법

구조:

class 클래스명():

> 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장이 가능하다!
> 함수나 변수들을 클래스에 넣어서 묶을수있음.

'''
#클래스 만들기 예시

class Human():
    '''사람'''


person1 = Human()  # Human의 인스턴스가 person1에 저장됨
person2 = Human()  # Human의 인스턴스가 person2에 저장됨

person1.language = '한국어'
person2.language = 'English'

person1.name = '서울시민'
person2.name = '인도인'


def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))


Human.speak = speak  # Human 클래스에 speak함수를 넣었으므로,
# Human의 인스턴스인 person1,person2에서도 speak함수의 능력을 가지게된다! 즉.. 아래처럼 가능!

person1.speak()  # 서울시민이 한국어로 말을 합니다.
person2.speak()  # 인도인이 English로 말을 합니다.