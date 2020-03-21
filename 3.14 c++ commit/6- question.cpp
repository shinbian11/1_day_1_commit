/* 예제.

1. 이름과 점수를 입력받고, 다음과 같이 출력되는 프로그램을 작성해 보세요.

이름 입력 : 두들낙서
점수 입력 : 80
두들낙서님의 점수는 80점입니다.

2. 범위 기반 for문을 사용하여 이차원 배열을 출력해보세요.

3. 다음과 같은 함수 정의에서 컴파일 오류가 나는 이유를 찾아보기.
*/


#include <iostream>
using namespace std;
int main()
{

	//1. 
	string name;
	int score;
	cout << "이름을 입력하세요 : ";
	cin >> name;
	cout << "점수를 입력하세요 : ";
	cin >> score;
	cout << name << "님의 점수는 " << score << "점 입니다." << endl;

	//2.
	int arr[2][3] = { {1,2,3},{4,5,6} };
	
	//배열 포인터랑 비슷하게 선언! 배열에 대한 reference이다.
	for (int(&ln)[3] : arr) //int[3]을 가리키는 참조변수 ln
	{
		for (int& col : ln)
		{
			cout << col << ' ';
		}
		cout << endl;
	}


	//위와 같은 의미!
	for (int(*ln)[3] = arr; ln < arr + 2; ln++)
	{
		for (int* c = *ln; c < *ln + 3; c++)
		{
			cout << *c << ' ';
		}
		cout << endl;
	}


	//물론 auto를 사용해도 됨
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
	//3. 컴파일 오류가 난 이유는?
	//default 값 (기본 매개변수)는 오른쪽 부터 줘야 하는데 왼쪽부터 줬으니 틀렸다.

	//3-2. 또 컴파일 오류가 난 이유는?
	//매개변수가 4개인 drawRectangle함수가 두개니까 오버로딩이 불가능! 두 함수가 구분이 되지 않는다.
}