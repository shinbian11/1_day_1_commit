#include <iostream>
using namespace std;
//함수 오버로딩 예제

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
//cnt,sc에 기본값(default)값을 주면, cnt와 sc에 대한 매개변수가 전달되지 않았을땐 기본값 만큼을 적용한다.
{
	inventory[itemId] += cnt;
	score += sc;
}
int main()
{
	getItem(6, 5); //sc는 0
	getItem(3, 2); //sc는 0
	getItem(3);  //cnt는 1, sc는 0
	getItem(11, 34, 7000); 

	cout << score << endl;
	for (int i = 0; i < 64; i++)
	{
		cout << inventory[i] << ' ';
	}
	cout << endl;

	
}