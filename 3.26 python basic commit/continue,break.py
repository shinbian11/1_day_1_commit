#continue,break

absent = [2, 5] #결석
no_book = [7] #책 안가져온 학생

for student in range(1,11):
    if student in absent:
        continue #continue는 밑 문장을 실행하지 않고 다시 위로 올라가는 명령!
    elif student in no_book:
        print('오늘 수업 여기까지. 책이 없는 {0}은 교무실로 따라와!'.format(student))
        break  #break는 반복문(for이나 while문)을 종료하고 탈출한다.
    print('{0}번아, 책 읽어야지!'.format(student))

