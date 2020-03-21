//C:\Users\shinb\Downloads\인프런 강의\c++   에 담기!
//C:\Users\shinb\OneDrive\문서\GitHub\MyProject\C-Project\repository   에 담기!
#include <iostream> //<stdio.h> 아니다!
#include <string> //<string.h> 아니다!
using namespace std; // std::cout => cout,   std::endl => endl

int main()
{
	//출력
	cout << "Hello World!" << endl;


	//입력
	int a, b;
	cin >> a >> b; //서식문자(%d,%c 등등) 필요 없음! 입력받는 변수들의 자료형을 알아서 처리해줌!
	cout << a << " + " << b << " = " << a + b << endl;

	//문자열
	string str; //문자열 자료형이 string 이다. 
	str = "Hello World"; //배열이 아니므로 길이를 줄 필요가 없다.
	cout << str << endl;

	string name;
	cout << "이름 입력 : ";
	cin >> name;
	string message = "안녕하세요, " + name + " 님!"; //문자열을 c언어보다 훨씬 유연하게 사용가능하다. (strcpy 같은 함수 사용하지 않고도 + 기호로 문자열끼리 덧붙일수 있는 것처럼!)
	cout << message << endl;
}