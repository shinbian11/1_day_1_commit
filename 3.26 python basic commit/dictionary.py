#사전
cabinet = {3:"유재석",100:"김태호"}

#value값을 가져오는 방법 1
print(cabinet[3])  #키 값을 []안에 넣어서 검색 가능
print(cabinet[100])

#value값을 가져오는 방법 2
print(cabinet.get(3))
print(cabinet.get(100))

#1번과 2번의 차이점
# []안에 키 값을 넣어서 사용했을때, 키 값이 없다면 오류가 발생한 뒤 프로그램 강제 종료됨!
# get()을 사용했을때, 키 값이 없다면 None을 출력하고 프로그램 계속 실행!

#print(cabinet[5])
#print('프로그램 강제 종료 안되었다면 이 문장이 실행됨!')

print(cabinet.get(5))
print('프로그램 강제 종료 안되었다면 이 문장이 실행됨!')


#--------------------------------

cabinet = {'a-100' : '유재석', 'b-100': '김태호'}
print(cabinet)

# 새 손님, 업데이트
cabinet['a-100'] = "박명수" #유재석을 박명수로 업데이트
cabinet['c-100'] = '조세호' #조세호를 추가
print(cabinet)  #{'a-100': '박명수', 'b-100': '김태호', 'c-100': '조세호'}

#간 손님
del cabinet['a-100']
print(cabinet)

#--------------------------------

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key와 value를 쌍으로 출력
print(cabinet.items())

#--------------------------------

#목욕탕 폐점
cabinet.clear()
print(cabinet)