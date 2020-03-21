# Chapter02-02
# 클래스 변수, 인스턴스 변수

class Car(): #모든 클래스는 object 클래스를 상속받는다.
    '''
    Car class
    Author: Kim
    Date:2020.3.20
    __doc__로 확인 가능!
    '''

    #클래스 변수(모든 인스턴스가 공유한다!!!!)
    car_count = 0



    # self 붙어있는 건 인스턴스 관련된것
    def __init__(self,company,details):  #인스턴스 메서드(self, 나의 것)
        self._company = company   #인스턴스 변수(self, 나의 것)
        #self.car_count = 10
        self._details = details
        Car.car_count += 1  #인스턴스가 한개씩 찍혀서 init함수 호출할때마다 1씩 증가

    def __str__(self):  # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self): # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1
        print('delete!!')

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

#self : 인스턴스에 각각 부여되는 고유의 id값을 받기 위한 예약된 지시어.
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Sliver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)  #false
print(car1 is car2)  #is : id값을 기준으로 인스턴스가 같은지?   false

# dir & __dict__
print(dir(car1)) #dir : 상위로부터 상속받는 것들을 보여줌
print(dir(car2))

print()
print()

print(car1.__dict__) #__dict__ : 상속받는 것의 값을 자세하게 딕셔너리 형태로 보여줌
print(car2.__dict__) #안에 있는 것들을 까보고 싶을때 사용

#Doctring
print(Car.__doc__)  #위에 적어놓은 주석(큰따옴표)을 볼수 있다

print()
print()

car1.detail_info()  #Car.detail_info(car1)
car2.detail_info()  #Car.detail_info(car2)
car3.detail_info()  #Car.detail_info(car3)

#비교
print(car1.__class__,car2.__class__)
print(id(car1.__class__),id(car2.__class__),id(car3.__class__)) # 같은 클래스(부모)에서 나온 인스턴스들이므로, 클래스의 id값은 같다.
print(id(car1.__class__)== id(car2.__class__) == id(car3.__class__)) #같다. True

#에러
#Car.detail_info()  > 에러 (인자를 넘겨야됨)
Car.detail_info(car2)  #car2.detail_info()와 같다. 접근 방법만 다를뿐!

#공유확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 근
# > 인스턴스 네임스페이스에 없으면 상위에서 검색
# > 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 없으면 상위(클래스, 부모 클래스)에서 찾는다)
print(car1.car_count)
#> 만약 car1이라는 인스턴스 내에 car_count라는 변수가 있다면 그것을 사용하지만,
#> 없다면 상위 클래스로 올라가서 찾는다. 상위 클래스에 car_count라는 변수가 있다면 그것을 사용한다.
#> 만약 상위 클래스에도 car_count변수가 없다면 그땐 오류가 발생한다.

print(Car.car_count)  #클래스 이름으로 접근해도 가능! 모두가 공유하는 변수니까!

#---------------------------------------------

del car2  #bmw 삭제

#삭제 확인
print(car1.car_count)
print(Car.car_count)