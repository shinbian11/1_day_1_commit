//static : 정적 <-> 동적
// 붕어빵의 틀의 멤버 : 정적 멤버
//붕어빵 틀로 찍어낸 붕어빵들의 멤버 : 동적 멤버


//static선언
//전역으로 쓰고 싶은 함수가 어떤 클래스와 밀접한 관련이 있고, private안에 있는 것들에게 직접접근을 하고 싶을때
//static선언을 하면 된다.

//객체지향언어는 전역변수와 전역함수를 지양(줄여야한다)해야한다.
//전역변수와 전역함수 대신 클래스 안으로 넣어서 static 선언을 하는 쪽으로!

#include <iostream>
using namespace std;


class Color {
public:
	
	Color() :r(0), g(0), b(0), id(idCounter++) {}
	Color(float r, float g, float b) : r(r), g(g), b(b), id(idCounter++) {}

	float GetR() { return r; }
	float GetG() { return g; }
	float GetB() { return b; }

	int GetId() { return id; }

	static Color MixColors(Color a, Color b)//정적 메서드
	{
		//return Color((a.GetR() + b.GetR()) / 2, (a.GetG() + b.GetG()) / 2, (a.GetB() + b.GetB()) / 2);
		return Color((a.r + b.r) / 2, (a.g + b.g) / 2, (a.b + b.b) / 2);
		//getter사용하지 않고 바로 private 멤버변수에 접근 가능!
	}

	static int idCounter;

private:
	float r;
	float g;
	float b;
	
	int id;
};

int Color::idCounter = 1; //static 변수는 밖에서 초기화!

int main()
{
	Color blue(0, 0, 1);
	Color red(1, 0, 0);
	//MixColors는 Color객체 안에 속해있는 메서드이므로 호출할때 그냥 MixColors라고 쓰면 안된다!
	//왜냐하면 어떤 객체의 MixColors인지를 표시해야하므로! 즉 그러므로 이럴떈 MixColors는 static선언을 한 다음에
	//그 정적 선언이 된 함수를 호출할땐 그 함수가 속해있는 Class의 이름을 앞에 써주면 된다!
	Color purple = Color::MixColors(blue, red);


	cout << "r = " << purple.GetR() << " g = " << purple.GetG() << " b = " << purple.GetR() << endl;
	cout << "blue.Getid() = " << blue.GetId() << endl;
	cout << "red.Getid() = " << red.GetId() << endl;
	cout << "purple.Getid() = " << purple.GetId() << endl;
}