//생성자 : 객체가 생성될때 자동으로 호출되는 함수
//소멸자 : 객체가 소멸될때 자동으로 호출되는 함수

//전역 객체의 생성자는 main함수 실행 전에 생성되고,
//전역 객체의 소멸자는 main함수가 끝난 이후에 생성된다.

//지역 객체의 생성자는 지역변수를 만나는 순간 생성된다.
//지역 객체의 소멸자는 지역변수가 속한 지역이 끝나는 순간 생성된다.

#include <iostream>
using namespace std;
class MyClass
{
public:
	MyClass() //생성자 : 반환형의 자료형을 쓰지 않음
	{
		cout << "생성자가 호출되었다." << endl;
	}

	~MyClass() //소멸자: ~ 표시를 적어줌
	{
		cout << "소멸자가 호출되었다." << endl;
	}
};

//MyClass globalObj;  //전역 변수

void testLocalObj()
{
	cout << "testLocalObj함수 시작!!" << endl;
	MyClass localObj; //지역 변수
	cout << "testLocalObj함수 끝!!" << endl;
}
int main()
{
	cout << "main함수 시작!" << endl;
	testLocalObj();
	cout << "main함수 끝!" << endl;
}