# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) : key에 Value를 저장하는 구조
# 파이썬의 dictionary가 해쉬 테이블의 예시
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조

#Dictionary 구조
print(__builtins__.__dict__)

#Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
#print(hash(t2)) #예외발생. 가변형인 리스트가 있기 때문에 언제든지 해쉬값이 바뀔수 있다.

print()
print()

#----------------------------------------------
#Dict Setdefault 예제
source = (('k1','val1'),
          ('k1','val2'),
          ('k2','val3'),
          ('k2','val4'),
          ('k2','val5'))

new_dict1 = {}
new_dict2 = {}

#No use Setdefault

for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)


#use Setdefault

for k,v in source:
    new_dict2.setdefault(k,[]).append(v)

print(new_dict2)

#----------------------------------------------
#주의사항
new_dict3 = {k:v for k,v in source} # 키가 같으면 나중의 값으로 덮어쓰기가 되니까 이건 안됨!
print(new_dict3)