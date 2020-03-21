import chien   #chien.py 를 import 한다.
import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1,1000)
    full_file_name = str(name) + '.jpg'  #name이 숫자가 오더라도 string 형으로 바꿔준다.
    urllib.request.urlretrieve(url,full_file_name)

download_web_image("http://post.phinf.naver.net/20160816_66/1471358257192YTaTP_PNG/ItAkQVzT1V86PKlwxc8W1-W_wwrk.jpg")  #사진이 저장된다!

chien.chien()  #Je suis un chien 출력

x = random.randrange(1,1000) #1~1000사이의 랜덤 숫자
print(x)