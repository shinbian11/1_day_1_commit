//this
#include <iostream>
using namespace std;

class MyClass {
public:
	void PrintThis()
	{
		cout << "나의 주소는 " << this << endl;
		//this가 소속되어있는 객체의 주소값을 출력한다.
	}
};

int main()
{
	MyClass a, b;

	cout << "a의 주소는 " << &a << endl;
	cout << "b의 주소는 " << &b << endl;
	
	a.PrintThis(); 
	b.PrintThis();
}