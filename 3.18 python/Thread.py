#thread : 동시에 여러 프로세서를 돌리는 것(멀티테스킹)

import threading

class Messenger(threading.Thread):
    def run(self):  #임의의 함수가 아니라 run이라는 함수로 해야함!
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messenger(name = "메세지를 보냅니다")
y = Messenger(name = "메세지를 수신합니다")

x.start()  #x.run() 이 아님! thread에서는 start를 사용
y.start()