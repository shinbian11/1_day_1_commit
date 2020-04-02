# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급


#Tuple Advanced
#Unpacking
#b, a = a, b

print(divmod(100, 9)) #몫과 나머지를 반환 # (11, 1)
print(divmod(*(100, 9))) # (11, 1)
print(*(divmod(100, 9)))#결과값을 unpacking # 11 1

print()

x, y, *rest = range(10) #x,y를 각각 하나씩 Unpacking 하고, 나머지는 모두 rest에!
print(x,y,rest)

x,y,*rest = range(2)
print(x,y,rest)

x,y,*rest = 1,2,3,4,5 #튜플
print(x,y,rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l,id(l))
print(m,id(m))

l = l*2
m = m*2

print(l,id(l)) #12649592
print(m,id(m)) #50053608

l *= 2
m *= 2

print(l,id(l)) #12761456  (불변형이므로 id값 재할당)
print(m,id(m)) #50053608  (가변형이므로 id값 동일)

#즉, 변동이 심한 값들은 리스트에 담아 놓는게 좀 더 메모리적으로 낫다!
#왜? 변동이 심한 값들은 값을 만약 튜플에 담아 놓는다면, 변동이 생길때마다 새로운 주소값으로 재할당을 하게 되므로
#메모리 소모가 심할수있다. 즉 리스트에 담아 놓으면 변동이 있더라도 같은 id값 내에서 처리가 가능하다!

#--------------------------------------------

#sort vs sorted
#reverse, key=len,key=str.lower,key=func...

#1. sorted: 정렬 후 새로운 객체로 반환 (원본이 수정되지 않는다.)
f_list = ['orange','apple','mango','papaya','lemon','strawberry','coconut'] #원본

print('sorted - ', sorted(f_list))#정렬됨
print('sorted - ',sorted(f_list, reverse=True)) #반대로 정렬
print('sorted - ',sorted(f_list, key=len)) #글자 길이 순서대로 정렬
print('sorted - ',sorted(f_list, key=lambda x: x[-1])) #맨 끝 글자를 기준으로 정렬
print('sorted - ',sorted(f_list, key=lambda x: x[-1], reverse = True)) #맨 끝 글자를 기준으로 정렬, 반대로 정렬
print('sorted(원본) : ',f_list) #['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut'] > 원본은 그대로!

#----------------------------------------------------------------------
#2. sort: 정럴후 객체 직접 변경 (원본이 직접 수정된다.)
#반환 값 확인(None)
print('sort - ', f_list.sort()) #직접 호출 (직접 변경할거니까 직접 호출)
print('sort(원본) -  ',f_list) #원본이 변경됨!

print('sort - ',f_list.sort(reverse=True), f_list) #반대로 정렬
print('sort - ',f_list.sort(key=len), f_list) #글자 길이 순서대로 정렬
print('sort - ',f_list.sort(key=lambda x : x[-1]), f_list) #맨 끝 글자를 기준으로 정렬
print('sort - ',f_list.sort(key=lambda x : x[-1], reverse=True), f_list) #맨 끝 글자를 기준으로 정렬, 반대로 정렬
print('sort(원본) -  ',f_list) #원본이 변경됨!

#----------------------------------------------------------------------

# List vs Array 적합한 사용법 설명 (중요!)
# 리스트 기반 : 융통성, '다양한' 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)  (import Array)




