#lambda : 함수 이름도 필요 없는 간단하게 사용하는 함수
#간단하게 한번 정도만 실행하고 싶을때 많이 사용! (일회성)

#lambda 변수 : 표현식

'''
일반식

def mul(x,y=7)
    return x*y
print(mul(5))

'''

#윗 일반식을 람다식으로 표현하면?
mul = lambda x : x*7
print(mul(5))
