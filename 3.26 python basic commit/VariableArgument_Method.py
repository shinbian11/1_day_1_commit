#가변인자!(Variable Argument)
#함수 호출을 여러번 할때 매개변수의 개수가 모두 일정하지가 않을때 사용!

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print('이름 : {0}\t나이: {1}\t'.format(name,age), end = ' ')
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):
    print('이름 : {0}\t나이: {1}\t'.format(name,age), end = ' ')
    for lang in language:
        print(lang,end=' ')
    print()

profile("유재석",20,"python",'java','c','c++','c#','javaScript')
profile("김태호",25, "kotlin",'swift')