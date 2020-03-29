class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값 입력! 한 자리 수만 입력하세요!")
except BigNumberError as err:
    print("에러 발생! 한 자리 수만 입력하세요!")
    print(err) #전달한 메세지가 출력됨