//멤버 메서드의 선언, 정의 분리하기
#include <iostream>
using namespace std;

class Vector2
{
public:
	//생성자의 선언,정의 분리하기
	Vector2(); 
	Vector2(float x, float y);

	float GetX() const;
	float GetY() const;
	//벡터의 연산방법1 : 정적 방법
	static Vector2 Sum(Vector2 a, Vector2 b)
	{
		return Vector2(a.x + b.x, a.y + b.y);
	}

	//벡터의 연산방법2 : 동적 방법
	Vector2 Add(Vector2 rhs)
	{
		return Vector2(x + rhs.x, y + rhs.y);
	}

private:
	float x;
	float y;
};


int main()
{
	Vector2 a(2, 3);
	Vector2 b(-1, 4);
	Vector2 c1 = Vector2::Sum(a , b);
	Vector2 c2 = a.Add(b);

	cout << a.GetX() << ", " << a.GetY() << endl;
	cout << b.GetX() << ", " << b.GetY() << endl;
	cout << c1.GetX() << ", " << c1.GetY() << endl;
	cout << c2.GetX() << ", " << c2.GetY() << endl;
}

//class이름을 namespace공간처럼 생각하여 ::로 이어준다.
Vector2::Vector2() : x(0), y(0) {} 
Vector2::Vector2(float x,float y) : x(x), y(y) {}

float Vector2::GetX() const { return x; }
float Vector2::GetY() const { return y; }