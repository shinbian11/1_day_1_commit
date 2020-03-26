#표준 출력
print('python','java','c++','javaScript',sep = ' vs ')
#sep > 각 콤마 사이에 들어갈 것을 정의

print()

print('python', 'java', sep=', ', end="?")
print('무엇이 더 재밌을까요? ')
#end > 문장의 끝 부분을 어떤걸로 바꿀지를 정의

print()

import sys
print('python','java', file=sys.stdout) #표준출력
#print('python','java', file=sys.stderr) #표준에러

print()

#시험 성적
scores = {'수학' : 0, '영어' : 50, '코딩' :100}
#딕셔너리에서 items를 사용하면 키와 값이 쌍으로 튜플형식으로 나온다.
for subject, score in scores.items():
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=':')
#ljust(8) : 8칸을 확보하고 왼쪽 정렬
#rjust(4) : 8칸을 확보하고 오른쪽 정렬

print()

#은행 대기순번표
#001, 002, 003 ...
for num in range(1,21):
    #print('대기번호 : '+ str(num))  #num은 int 형이니까 문자열로 변환해야 문자열끼리 더하기가 가능!
    print('대기번호 : '+ str(num).zfill(3)) #3칸을 확보하고 값이 없는 빈 공간은 0으로 채운다.



print()

#-----------------------------------------------------
#표준 입력

#input을 통해 입력을 받으면 항상 str(문자열)형태로 나오게 된다!
answer = input('아무 값이나 입력하세요 : ')
print(type(answer))  #str형
print('입력하신 값은 ' + answer + '입니다.')