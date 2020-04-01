# Chapter04-01
# 파이썬 심화
# 시퀀스형
#-----------------------------------------------
# 파이썬의 데이터 타입 구분!!

# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])

# 가변(수정 가능)(list, bytearray, array.array, memoryview, deque)
# 불변(수정 불가)(tuple, str, bytes)
#-----------------------------------------------

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!'
code_list1 = []

for s in chars:
    #유니코드 리스트
    #ord함수는 유니코드로 바꾸어주는 함수
    code_list1.append(ord(s))

print(code_list1)

#Comprehension Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

#Comprehending lists + map, filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

#문자 -> 유니코드 : ord()
#유니코드 -> 문자 : chr()
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

#--------------------------------------------------------
#Generator 생성

import array

#Generator : 한 번에 한 개의 항목을 생성(메모리 유지 x)
tuple_g = (ord(s) for s in chars)  #[]가 아닌 ()로 감싸면 generator가 만들어짐
array_g = array.array('I',(ord(s) for s in chars))

print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

print()
print()

#제네레이터 예제
print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1, 21)):
    print(s)

print()
print()

#(중요!) 리스트 주의 (깊은 복사와 얕은 복사의 차이점..)

marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

#수정 (수정을 하면 결과값이 서로 달라진다!)
marks1[0][1] = 'X'
marks2[0][1] = 'X'

#각각 다른 id값이 부여된 것이기 때문에 리스트들끼리 서로 구분이 된다
print(marks1) #[['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
#같은 주소값을 가진 리스트가 4번 복사된 것이므로, 리스트들이 서로 구분이 안된다.
print(marks2) #[['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]

#증명
print([id(i) for i in marks1]) # [54249192, 54248584, 54249128, 54249064]
print([id(i) for i in marks2]) # [54249032, 54249032, 54249032, 54249032]
