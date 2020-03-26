# 상품을 주려고 한다. 댓글 작성자 중 추첨 1명은 치킨, 3명은 커피쿠폰
# 추첨 프로그램 작성
# 편의상 댓글은 20명 이 작성, 아이디는 1~20이다.
# 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# random모듈의 shuffle과 sample을 이용

'''
(출력 예제)
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다--
'''
'''
(활용하는 법)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) #lst를 아무렇게나 섞는다.
print(lst)
print(sample(lst,1)) #lst에서 1개를 아무거나 뽑는다
'''
from random import *

user = range(1,21)
users = list(user)
shuffle(users)

winners = sample(users, 4) #4명중 한명만 치킨, 3명은 커피

print('--당첨자 발표--')
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피 당첨자 : {}'.format(winners[1:4]))
print('--축하합니다--')