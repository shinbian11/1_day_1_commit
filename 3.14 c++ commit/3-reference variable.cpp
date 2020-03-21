#include <iostream>
using namespace std;

void swap(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}

int main()
{
	//레퍼런스 변수(참조 변수)
	int a(5);
	int& p = a;
	p = 10;

	cout << p << endl;  //10
	cout << a << endl;  //10

	//--------------------------

	//swap 함수
	int x(10);
	int y(50);
	swap(x, y);
	cout << x << endl;   //50
	cout << y << endl;   //10

	//------------------------

	int a(5);
	int& r1 = a;

	//3이나 a*a라는 것은 메모리 공간에 들어있는 것이 아니기 때문에 가리킬수 없다.
	//int& r2 = 3;  (x)
	//int& r3 = a * a;  (x)

	//------------------------

	//r-value : 수정할 수 없는 값
	//l-value : 수정할 수 있는 값

	//int&& r1 = a; //a는 l-value인데 &&은 r-value를 나타내는 것이므로 안된다.
	int&& r2 = 3;
	int&& r3 = a * a;
	//또한, 함숫값도 수정할수 없는 값이므로 r-value로 참조 가능!


}