#include <iostream>
using namespace std;
//�Լ� �����ε� ����

int inventory[64] = { 0 };
int score = 0;

//void getItem(int itemId)
//{
//	inventory[itemId]++;
//}
//void getItem(int itemId, int cnt)
//{
//	inventory[itemId] += cnt;
//}
void getItem(int itemId, int cnt = 1, int sc = 0) 
//cnt,sc�� �⺻��(default)���� �ָ�, cnt�� sc�� ���� �Ű������� ���޵��� �ʾ����� �⺻�� ��ŭ�� �����Ѵ�.
{
	inventory[itemId] += cnt;
	score += sc;
}
int main()
{
	getItem(6, 5); //sc�� 0
	getItem(3, 2); //sc�� 0
	getItem(3);  //cnt�� 1, sc�� 0
	getItem(11, 34, 7000); 

	cout << score << endl;
	for (int i = 0; i < 64; i++)
	{
		cout << inventory[i] << ' ';
	}
	cout << endl;

	
}