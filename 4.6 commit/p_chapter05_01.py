# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수의 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능

#---------------------------------------------------------------------

#함수 객체(ex. 팩토리얼)
def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: #n < 2
        return 1
    return n*factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__) #__doc__ : 주석 확인
print(type(factorial),type(A))
print(set(sorted(dir(factorial)))-set(sorted(dir(A)))) #함수만 가지고 있는 성질
print(factorial.__name__) #함수의 이름
print(factorial.__code__) #파일의 세부정보

print()
print()

#---------------------------------------------------------------------

# 2.변수 할당 가능
var_func = factorial
print(var_func)
print(var_func(10)) #3628800
print(list(map(var_func,range(1,11)))) #[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

#---------------------------------------------------------------------

# 3,4. 함수 인수 전달 및 함수로 결과 반환 가능-> 고위 함수(Higher-order Function)
# (중요!) map, filter, reduce

print(list(map(var_func, filter(lambda x:x % 2, range(1,6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

#---------------------------------------------------------------------

#reduce
from functools import reduce #reduce 가져오기
from operator import add #더해주는 함수
from operator import sub #빼주는 함수


print(reduce(add, range(1,11))) #1부터 11까지 누적해서 add해준다. #55
print(sum(range(1,11))) #55

print(reduce(sub, range(1,11))) #1부터 11까지 누적해서 sub해준다. #-53

#---------------------------------------------------------------------

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 익명함수 보다는 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x+t,range(1,11))) #55

print()
print()

#---------------------------------------------------------------------

# Callable : 호출 연산자 -> 메서드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str)) # str() 함수는 호출 가능! True
print(callable(A)) # 위에서 만들어놓은 클래스 A도 호출 가능! True
print(callable(list),callable(var_func), callable(factorial)) # True True True
print(callable(3.14)) # 상수는 함수 형태로 호출 불가능! False


print()
print()

#---------------------------------------------------------------------

# partial 사용법 (매우 중요!!) : 인수를 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5) # 5 * ? 인 상태 (5가 고정된 상태)

print(five(10)) # 5 * 10 = 50
print(five(100)) # 5 * 100 = 500

#고정 추가
six = partial(five, 6) #5가 고정되어 있는 상태에서 나머지 1개도 6으로 고정!

print(five(10)) # 5*10 = 50
print(six()) # 5*6 = 30

print([five(i) for i in range(1,11)]) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five,range(1,11)))) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
