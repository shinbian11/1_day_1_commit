#include <iostream>


int n;
void set()
{
	n = 10;
}

namespace doodle {
	int n;
	void set()
	{
		n = 20;
	}

	namespace google {
		int n;
		void set()
		{
			n = 30;
		}
	}
}

int main()
{
	using namespace std;
	using namespace doodle;

	::set();
	doodle::set();

	//google 스페이스가 한개만 있으니까 doodle 생략 가능
	google::set(); //doodle::google::set();

	cout << ::n << endl;
	cout << doodle::n << endl;
	cout << doodle::google::n << endl;
}

