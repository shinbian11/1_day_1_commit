#include <iostream>
using namespace std;
int main()
{
	int* arr;
	int len;

	cout << " ���� �Է� : > ";
	cin >> len;

	arr = new int[len];

	for (int i = 0; i < len; i++)
	{
		arr[i] = len - i;
	}
	for (int i = 0; i < len; i++)
	{
		cout << arr[i] << endl;
	}

	//delete arr;  //>> arr[0]�� delete��
	delete[] arr;  //�迭 ��ü ����
}