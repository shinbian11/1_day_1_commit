#include <iostream>
using namespace std;
int main()
{
	//���� ����,�ʱ�ȭ,����

	int a(10); // int a = 10; �� ����
	// a(5);  >> ��� �Ұ�! �Լ����� �������� ��
	int b(a + 5);
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	//----------------------------------

	//���� ��� for��(��� for��)

	int arr[10] = { 0,1,2,3,4,5,6,7,8,9 };
	//for (int i = 0; i < 10; i++)
	//{
	//	cout << arr[i] << endl;
	//}
	for (int& n : arr) //���۷��� ���� �����ϸ� arr[i] ���� ����!
	{
		cout << n << ' ';
		n++; //n�� arr[i]�� ����Ű�鼭 1�� �����ϹǷ� ������ ���� ��ȭ�� �Ͼ��.
	}

	cout << endl; //���� ����

	for (int& n : arr) //������ n++�����Ƿ�
	{
		cout << n << ' ';
		n -= 2;
	}

	cout << endl;

	for (int& n : arr) //������ 2�� ���������Ƿ�
	{
		cout << n << ' ';
	}
	cout << endl;
	for (int n : arr) //arr ��ü�� ����ϴ� for���̹Ƿ� �׳� �������� arr�� �״�� ���
	{
		cout << n << ' ';
	}
}