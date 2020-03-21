//static : ���� <-> ����
// �ؾ�� Ʋ�� ��� : ���� ���
//�ؾ Ʋ�� �� �ؾ���� ��� : ���� ���


//static����
//�������� ���� ���� �Լ��� � Ŭ������ ������ ������ �ְ�, private�ȿ� �ִ� �͵鿡�� ���������� �ϰ� ������
//static������ �ϸ� �ȴ�.

//��ü������� ���������� �����Լ��� ����(�ٿ����Ѵ�)�ؾ��Ѵ�.
//���������� �����Լ� ��� Ŭ���� ������ �־ static ������ �ϴ� ������!

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

	static Color MixColors(Color a, Color b)//���� �޼���
	{
		//return Color((a.GetR() + b.GetR()) / 2, (a.GetG() + b.GetG()) / 2, (a.GetB() + b.GetB()) / 2);
		return Color((a.r + b.r) / 2, (a.g + b.g) / 2, (a.b + b.b) / 2);
		//getter������� �ʰ� �ٷ� private ��������� ���� ����!
	}

	static int idCounter;

private:
	float r;
	float g;
	float b;
	
	int id;
};

int Color::idCounter = 1; //static ������ �ۿ��� �ʱ�ȭ!

int main()
{
	Color blue(0, 0, 1);
	Color red(1, 0, 0);
	//MixColors�� Color��ü �ȿ� �����ִ� �޼����̹Ƿ� ȣ���Ҷ� �׳� MixColors��� ���� �ȵȴ�!
	//�ֳ��ϸ� � ��ü�� MixColors������ ǥ���ؾ��ϹǷ�! �� �׷��Ƿ� �̷��� MixColors�� static������ �� ������
	//�� ���� ������ �� �Լ��� ȣ���Ҷ� �� �Լ��� �����ִ� Class�� �̸��� �տ� ���ָ� �ȴ�!
	Color purple = Color::MixColors(blue, red);


	cout << "r = " << purple.GetR() << " g = " << purple.GetG() << " b = " << purple.GetR() << endl;
	cout << "blue.Getid() = " << blue.GetId() << endl;
	cout << "red.Getid() = " << red.GetId() << endl;
	cout << "purple.Getid() = " << purple.GetId() << endl;
}