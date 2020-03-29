#include <iostream>
using namespace std;
int main()
{
	int* arr;
	int len;

	cout << " 길이 입력 : > ";
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

	//delete arr;  //>> arr[0]만 delete됨
	delete[] arr;  //배열 전체 해제
}