/* ����.

1. �̸��� ������ �Է¹ް�, ������ ���� ��µǴ� ���α׷��� �ۼ��� ������.

�̸� �Է� : �ε鳫��
���� �Է� : 80
�ε鳫������ ������ 80���Դϴ�.

2. ���� ��� for���� ����Ͽ� ������ �迭�� ����غ�����.

3. ������ ���� �Լ� ���ǿ��� ������ ������ ���� ������ ã�ƺ���.
*/


#include <iostream>
using namespace std;
int main()
{

	//1. 
	string name;
	int score;
	cout << "�̸��� �Է��ϼ��� : ";
	cin >> name;
	cout << "������ �Է��ϼ��� : ";
	cin >> score;
	cout << name << "���� ������ " << score << "�� �Դϴ�." << endl;

	//2.
	int arr[2][3] = { {1,2,3},{4,5,6} };
	
	//�迭 �����Ͷ� ����ϰ� ����! �迭�� ���� reference�̴�.
	for (int(&ln)[3] : arr) //int[3]�� ����Ű�� �������� ln
	{
		for (int& col : ln)
		{
			cout << col << ' ';
		}
		cout << endl;
	}


	//���� ���� �ǹ�!
	for (int(*ln)[3] = arr; ln < arr + 2; ln++)
	{
		for (int* c = *ln; c < *ln + 3; c++)
		{
			cout << *c << ' ';
		}
		cout << endl;
	}


	//���� auto�� ����ص� ��
	for (auto& ln : arr)
	{
		for (auto& col : ln)
		{
			cout << col << ' ';
		}
		cout << endl;
	}
}


//3.

void drawRectangle(int l, int r, int t, int b)
{

}
//3.void drawRectangle(int x = 0, int y = 0, int w, int h)
//3-2.void drawRectangle(int x, int y, int w = 0, int h = 0)
{
	//3. ������ ������ �� ������?
	//default �� (�⺻ �Ű�����)�� ������ ���� ��� �ϴµ� ���ʺ��� ������ Ʋ�ȴ�.

	//3-2. �� ������ ������ �� ������?
	//�Ű������� 4���� drawRectangle�Լ��� �ΰ��ϱ� �����ε��� �Ұ���! �� �Լ��� ������ ���� �ʴ´�.
}