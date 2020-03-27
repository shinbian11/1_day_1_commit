import pickle
# profile_file = open("profile.pickle","wb")  #pickle binary의 b를 꼭 써야한다.
# #wb에서 b는 binary , encoding은 필요없음
# profile = {'이름':'박명수','나이':30,'취미':['축구','골프','코딩']}
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

#profile.pickle에서 가져오기
profile_file = open("profile.pickle","rb")
try:
    profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러옴
    print(profile)
    profile_file.close()
except EOFError:
    print('EOFError')