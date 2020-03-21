#include <iostream>
using namespace std;

int n;
void set(); //함수 선언

namespace doodle {
	int n;
	void set();

}
namespace google {
	int n;
	void set();

}
int main()
{
	::set(); 
	doodle::set();
	google::set();

	cout << ::n << endl; 
	cout << doodle::n << endl; 
	cout << google::n << endl; 
}
//void set()
//{
//	n = 10; //전역변수라는 걸 명시함!
//}
void ::set()
{
	n = 10;
}
//namespace doodle {
//	void set()
//	{
//		n = 20;
//	}
//}
void doodle::set()
{
	n = 20;
}
//namespace google {
//	void set()
//	{
//		n = 30;
//	}
//}

//함수 선언만 위에서 하고 밑에서 함수의 정의를 할땐 이렇게 작성해도 된다!
void google::set() 
{
	n = 30; 
}