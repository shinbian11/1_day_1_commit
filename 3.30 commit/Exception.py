try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력 > ")))
    nums.append(int(input("두 번째 숫자를 입력 > ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("ERROR가 발생했습니다.")
except ZeroDivisionError as err:
    print(err, ", 0으로 나눌순 없습니다.")
except Exception as err:
    print("알 수 없는 에러 발생! > ")
    print(err)