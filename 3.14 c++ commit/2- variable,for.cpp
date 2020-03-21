#include <iostream>
using namespace std;
int main()
{
	//변수 선언,초기화,대입

	int a(10); // int a = 10; 와 같음
	// a(5);  >> 사용 불가! 함수인지 변수인지 모름
	int b(a + 5);
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	//----------------------------------

	//범위 기반 for문(향상 for문)

	int arr[10] = { 0,1,2,3,4,5,6,7,8,9 };
	//for (int i = 0; i < 10; i++)
	//{
	//	cout << arr[i] << endl;
	//}
	for (int& n : arr) //레퍼런수 변수 선언하면 arr[i] 수정 가능!
	{
		cout << n << ' ';
		n++; //n이 arr[i]를 가리키면서 1씩 증가하므로 실제로 값의 변화가 일어난다.
	}

	cout << endl; //개행 문자

	for (int& n : arr) //위에서 n++했으므로
	{
		cout << n << ' ';
		n -= 2;
	}

	cout << endl;

	for (int& n : arr) //위에서 2씩 감소했으므로
	{
		cout << n << ' ';
	}
	cout << endl;
	for (int n : arr) //arr 자체를 출력하는 for문이므로 그냥 위에서의 arr이 그대로 출력
	{
		cout << n << ' ';
	}
}