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
	//���۷��� ����(���� ����)
	int a(5);
	int& p = a;
	p = 10;

	cout << p << endl;  //10
	cout << a << endl;  //10

	//--------------------------

	//swap �Լ�
	int x(10);
	int y(50);
	swap(x, y);
	cout << x << endl;   //50
	cout << y << endl;   //10

	//------------------------

	int a(5);
	int& r1 = a;

	//3�̳� a*a��� ���� �޸� ������ ����ִ� ���� �ƴϱ� ������ ����ų�� ����.
	//int& r2 = 3;  (x)
	//int& r3 = a * a;  (x)

	//------------------------

	//r-value : ������ �� ���� ��
	//l-value : ������ �� �ִ� ��

	//int&& r1 = a; //a�� l-value�ε� &&�� r-value�� ��Ÿ���� ���̹Ƿ� �ȵȴ�.
	int&& r2 = 3;
	int&& r3 = a * a;
	//����, �Լ����� �����Ҽ� ���� ���̹Ƿ� r-value�� ���� ����!


}