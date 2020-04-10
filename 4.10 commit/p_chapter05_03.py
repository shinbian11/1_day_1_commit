# Chapter05-03
# 파이썬 심화
# 클로저 심화
# 외부에서 호출된 함수의 변수값, 상태(래퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능


# - 클로저 사용 예제
# - 잘못된 클로저 사용
# - 클로저 정리

#---------------------------------------------------

# - 클로저 사용 예제

# - averager 내부 함수에서 외부의 series 자유변수를 참조한다. 그런데 averager 함수 호출이
# 끝났음에도 불구하고 series에 들어있는 값을 계속 기억하고 있다.

def closure_ex1():
    # Free variable(자유 변수)
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()
#------------------------------------
# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) #자유 변수 출력  #('series',)
print(avg_closure1.__closure__[0].cell_contents) #자유 변수의 값 출력
#------------------------------------
print()
print()

# - 잘못된 클로저 사용

def closure_ex2():
    #자유 변수
    cnt = 0  #len 같은 느낌
    total = 0  #sum 같은 느낌

    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외 발생

#--------------------------------------
def closure_ex3():
    #자유 변수
    cnt = 0  #len 같은 느낌
    total = 0  #sum 같은 느낌

    def averager(v):
        nonlocal cnt,total # 위에서 이 문장만 추가하면 예외 발생 안하고 실행 가능!
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))