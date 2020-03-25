#quiz ) 사이트별로 비번을 만들어 주는 프로그램을 작성
'''
예) http://naver.com
규칙1: http:// 부분은 제외
2 : 처음 만나는 점 이후 부분은 제외
3: 남은 글자 중 처음 세자리 + 글자 갯수+ 'e'개수 + '!'로구성
=> nav51!
'''

url = "http://daum.net"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3]+str(len(my_str))+str(my_str.count('e'))+'!'
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
