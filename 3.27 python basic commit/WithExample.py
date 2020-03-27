#with >> with는 close 할 필요가 없다. 자동적으로 됨

#import pickle
# with open("profile.pickle",'rb') as profile_file:
#     print(pickle.load(profile_file))

#------------------------------
#pickle 쓰지 않고 일반 파일을 읽고 쓰기
with open("study.txt",'w',encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하는 중입니다!!')

with open('study.txt','r',encoding='utf8') as study_file:
    print(study_file.read())