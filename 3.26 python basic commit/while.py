#while
customer = "토르"
index = 5

while index >= 1:
    print("{0} 손님, 커피가 준비되었습니다. {1}번 남았어요 ".format(customer,index))
    index -= 1
    if index == 0:
        print('커피가 폐기처분되었습니다.')

#무한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0} 손님, 커피가 준비되었습니다. {1}번째 호출입니다. ".format(customer, index))
#     index += 1



#이름이 토르인 사람을 찾아서 커피를 준다.
customer = '토르'
person = 'unknown'

while person != customer:
    print('{0}님, 커피가 준비되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요? > ')

print('안녕하세요 {0}님, 커피 가져가시면 됩니다.'.format(customer))