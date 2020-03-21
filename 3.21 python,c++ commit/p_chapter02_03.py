# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드

class Car(): #모든 클래스는 object 클래스를 상속받는다.
    '''
    Car class
    Author: Kim
    Date:2020.3.21
    __doc__로 확인 가능!
    Description : Class, Static, Instance Method
    '''

    #클래스 변수(모든 인스턴스가 공유한다!!!!)
    price_per_raise = 1.0


    # self 붙어있는 건 인스턴스 관련된것
    def __init__(self,company,details):  #인스턴스 메서드(self, 나의 것)
        self._company = company   #인스턴스 변수(self, 나의 것)
        #self.car_count = 10
        self._details = details

    def __str__(self):  # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self): # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'repr : {} - {}'.format(self._company, self._details)

    #Instance Method

    # self : 인스턴스에 각각 부여되는 고유의 id값을 받기 위한 예약된 지시어, 객체의 고유한 속성값을 사용,
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    #인스턴스 메서드
    def get_price(self):  #getter 함수
        return 'Before Car Price -> company : {}, price : {}'.format(self._company,self._details.get('price'))

    #인스턴스 메서드
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    #class method(클래스 메서드)
    @classmethod
    def raise_price(cls, per):  #클래스 메서드는 cls를 받음
        if per <= 1:  #가격이 내려가는건 의미 없다고 가정
            print('please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! Price increased!')

    #static method(스태틱 메서드) : 기본적으로 아무것도 전달받지 않음
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return 'Ok! this car is {}'.format(inst._company)
        return 'sorry! this car is not Bmw..'


#인스턴스 메서드는 self를 받고, 클래스 메서드는 cls를 받고, 스태틱 메서드는 아무것도 받지 않는다.

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

#전체정보
car1.detail_info()
car2.detail_info()

#-----------------------------------------------------
#가격정보(직접 접근 ->권장하지 않음)
print(car1._details.get('price')) #좋지 못한 방법. 외부에서 접근 못하게 private으로 선언하면 못 쓴다.
print(car2._details['price'])

#가격정보 (인상전)
print(car1.get_price())
print(car2.get_price())
#-----------------------------------------------------
#가격 인상 (클래스 메서드 미사용)
Car.price_per_raise = 1.4 #(직접 접근하는건 좋지 못한 방법 ㅠ)

#가격정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

#-----------------------------------------------------

#가격 인상 (클래스 메서드 사용)
Car.raise_price(1.8)

#가격정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

#-----------------------------------------------------

# static 메서드 사용하여 bmw가 맞는지 확인!

#인스턴스로 호출(스테틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 이렇게 클래스로도 호출 가능!
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))