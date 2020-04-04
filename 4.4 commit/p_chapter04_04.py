# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict(딕셔너리) -> Key 중복 허용 X
# Set(집합) -> 중복 허용 X

# Dict 및 Set 심화 (읽기 전용으로 딕셔너리와 집합을 생성 가능하다)

#---------------------------------------------------------------------------

# immutable Dict (읽기 전용의 딕셔너리) (수정 불가)
from types import MappingProxyType

d={'key1':'value1'}

#Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 1.수정 불가
#d_frozen['key2'] = 'value2' # > TypeError: 'mappingproxy' object does not support item assignment

# 2.수정 가능
d['key2'] = 'value2'
print(d)


print()
print()
#---------------------------------------------------------------------------

#set(집합) 만드는 법! 5가지!

s1 = {'Apple','Orange','Apple','Orange','Kiwi'} #중복 불가
s2 = set(['Apple','Orange','Apple','Orange','Kiwi']) #set([리스트 형태])
s3 = {3}
s4 = set() # 원소가 하나도 없을땐 {} 이라고 선언하면 dict이 되므로 안된다! set()으로 해야됨!
s5 = frozenset({'Apple','Orange','Apple','Orange','Kiwi'}) #읽기 전용의 set

# 1.추가 가능
s1.add('Melon')
print(s1)

# 2.추가 불가
# s5.add('Melon') # > AttributeError: 'frozenset' object has no attribute 'add'
# 읽기 전용 이므로 새로운 값을 추가하거나 수정은 불가능하다.
# 매우 중요한 자료들은 이렇게 frozenset을 통하여 보관할 수 있다!!

print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))

#---------------------------------------------------------------------------

# set 선언 최적화
# 바이트 코드 실행 -> 파이썬 인터프리터 실행

from dis import dis
print('---------')
print(dis('{10}')) #3단계가 존재

print('---------')
print(dis('set([10])')) #5단계가 존재

# set을 만들 때 알고 있으면 좋은 점!
# 시간적인 차이에서 set() 함수를 이용하는것보다, {10}처럼 직접 집합을 만드는 것이
# 더 시간을 아낄 수 있다. 즉 '직접 집합을 만드는 것'을 '추천'함!

#---------------------------------------------------------------------------

# 지능형 집합 만드는 법 (Comprehending Set)
# 참고 : 지능형은 리스트, 튜플, 딕셔너리, 집합 모두 가능하다!
print()

print('지능형 set')
from unicodedata import name

#chr() 함수는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
#name 함수를 가져와서 해당하는 값이 없다면 ''(공백)으로 출력하게끔 변환하였다.
print({name(chr(i),'') for i in range(0,256)})
