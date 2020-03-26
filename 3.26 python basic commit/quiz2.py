#50명의 승객과 매칭 기회가 있는 택시 기사님. 총 탑승 승객수 를 구하는 프로그램 작성
'''
조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해짐
조건2: 당신은 소요시간 5~15분 사이의 승객만 매칭할수있습니다.
'''
'''
(출력문 예제)
[O] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
[O] 3번째 손님 (소요시간: 5분)
...
[ ] 50번째 손님 (소요시간: 25분)

총 탑승 승객: 2명
'''
from random import *
i = 1
cnt = 0
while i <= 50:
    #minute = int(random()*46 + 5)
    minute = randrange(5, 51)
    #if minute >= 5 and minute <= 15:
    if 5 <= minute <= 15:
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i, minute))
        cnt += 1
    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, minute))
    i += 1
print()

print('총 탑승 승객 : {}명'.format(cnt))