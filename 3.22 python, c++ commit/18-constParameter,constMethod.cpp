//����� �Ű������� ����� �޼���

//1. �Ű������� ���ȭ (��� �Լ��� ����)
//2. �޼����� ���ȭ (��� �޼��忡���� ����)

#include <iostream>

using namespace std;

class Account
{
public:
	//������ �����ε�
	Account() : money(0) {}
	Account(int money) : money(money) {}

	//�Լ�
	void Deposit(const int d){ //�Ű������� ���ȭ(d�� ���� ���ϰ�!)
		money += d;
		cout << d << "���� �����ߴ�!" << endl;
	}
	void Draw(const int d) { //�Ű������� ���ȭ(d�� ���� ���ϰ�!)
		if (money >= d) {
			money -= d;
			cout << d << "���� �����ߴ�!" << endl;
		}
	}
	int ViewMoney() const //��� �޼����� ���ȭ(money�� ���� ���ϰ�!)
	{
		return money;
	}

private:
	int money; //�ܾ�
};

int main()
{
	Account doodle(200);
	doodle.Deposit(100);
	doodle.Draw(20);
	cout << doodle.ViewMoney() << endl;
}
