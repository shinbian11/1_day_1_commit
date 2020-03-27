#파일 쓰기
# score_file = open("score.txt","w", encoding="utf8")
# print('수학 : 0',file = score_file)
# print('영어 : 50',file = score_file)
# score_file.close()  #> 항상 파일 닫기 해주기!

#파일 추가하기
# score_file = open("score.txt","a",encoding="utf8") #append
# score_file.write("과학 : 80") #줄바꿈 해줘야됨
# score_file.write("\n코딩 : 100")
# score_file.close()    #> 항상 파일 닫기 해주기!

#파일 읽기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read()) #모든 내용 읽어오기
# score_file.close()    #> 항상 파일 닫기 해주기!

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(), end='')  #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end='')
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()    #> 항상 파일 닫기 해주기!

#파일이 몇줄인지 모를때 반복문을 통해 다 읽기
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='')
# score_file.close()  #> 항상 파일 닫기 해주기!


#리스트에 넣어서 처리하기
# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines() #list형태로 저장
# #print(lines)
# for line in lines:
#     print(line, end='')
#
# score_file.close()




