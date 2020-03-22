//상수형 매개변수와 상수형 메서드

//1. 매개변수의 상수화 (모든 함수에 가능)
//2. 메서드의 상수화 (멤버 메서드에서만 가능)

#include <iostream>

using namespace std;

class Account
{
public:
	//생성자 오버로딩
	Account() : money(0) {}
	Account(int money) : money(money) {}

	//함수
	void Deposit(const int d){ //매개변수의 상수화(d를 변경 못하게!)
		money += d;
		cout << d << "원을 예금했다!" << endl;
	}
	void Draw(const int d) { //매개변수의 상수화(d를 변경 못하게!)
		if (money >= d) {
			money -= d;
			cout << d << "원을 인출했다!" << endl;
		}
	}
	int ViewMoney() const //멤버 메서드의 상수화(money를 변경 못하게!)
	{
		return money;
	}

private:
	int money; //잔액
};

int main()
{
	Account doodle(200);
	doodle.Deposit(100);
	doodle.Draw(20);
	cout << doodle.ViewMoney() << endl;
}
