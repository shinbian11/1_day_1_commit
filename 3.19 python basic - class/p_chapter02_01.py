# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 ,유지보수,대형프로젝트 용이
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대해짐-> 복잡해짐
# 클래스 중심-> 데이터 중심-> 객체로 관리

#1. 일반적인 (절차적인) 코딩

#차량 1
car_company = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower' : 400},
    {'price': 8000}
]

#차량 2
car_company = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower' : 270},
    {'price': 5000}
]

#차량 3
car_company = 'Audi'
car_detail_3 = [
    {'color': 'Sliver'},
    {'horsepower' : 300},
    {'price': 6000}
]

#=> 자동차가 추가될 수록 코드가 방대하게 증가하며, 수정사항이 있으면 일일히 다 변경해야한다는 단점!

#----------------------------------------------------------

#리스트 구조
car_company_list= ['Ferrari','Bmw','Audi']
car_detail_list = [
    {'color': 'White', 'horsepower' : 400,'price': 8000},
    {'color': 'Black', 'horsepower': 270,'price': 5000},
    {'color': 'Sliver', 'horsepower': 300,'price': 6000}
]
# 인덱스로 접근하기도 불편하고, 수정사항이 있으면 일일히 다 변경하기가 불편하다는 단점!
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제도 불편

print(car_company_list)
print(car_detail_list)

#----------------------------------------------------------
print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키 => 중복을 허용하지 않는다), 키 조회 예외 처리 등
# 이것도 불편한 점이 많다.

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail':  {'color': 'White', 'horsepower' : 400,'price': 8000}},
    {'car_company': 'Bmw', 'car_detail':  {'color': 'Black', 'horsepower': 270,'price': 5000}},
    {'car_company': 'Audi', 'car_detail':  {'color': 'Sliver', 'horsepower': 300,'price': 6000}}
]

del car_dicts[1]
print(car_dicts)
#----------------------------------------------------------
# 클래스 구조
# 구조 설계후 재사용성 증가, 코드 반복 최소화 , 메서드를 활용


# 2. 객체적인 코딩

class Car():
    def __init__(self,company,details):
        self.company = company
        self.details = details


# 스페셜(매직) 메서드
    def __str__(self):  # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'str : {} - {}'.format(self.company,self.details)

    def __repr__(self): # Car안의 속 알맹이를 출력할수 있는 메서드
        return 'repr : {} - {}'.format(self.company, self.details)

car1 = Car('Ferrari',{'color': 'White', 'horsepower' : 400,'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270,'price': 5000})
car3 = Car('Audi',{'color': 'Sliver', 'horsepower': 300,'price': 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__) #클래스 안의 속성 정보를 볼수있다!
print(car2.__dict__)
print(car3.__dict__)

#print(dir(car1))


print()
print()
#-------------------------------------------
#리스트 선언

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
print(car_list)

print()
print()
#-------------------------------------------
#반복문에서는 기본적으로 __str__로 출력
for x in car_list:
    print(x)
    print(repr(x))  #이렇게 명시하면 __repr__로도 출력 가능
