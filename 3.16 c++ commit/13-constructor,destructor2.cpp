#include <iostream>

using namespace std;

//생성자 : 멤버 변수를 초기화 할 때 주로 사용됨
//소멸자 : 메모리 해제 할 때 주로 사용됨

//복소수(Complex number): (real 실수부, imag 허수부)

class Complex
{
public:
	Complex() //생성자 1번
	{
		real = 0;
		imag = 0;
	}
	Complex(double real_, double imag_) //생성자 2번 (오버로딩)
	{
		real = real_;
		imag = imag_;
	}

	double GetReal() //getter
	{
		return real;
	}
	void SetReal(double real_)//setter
	{
		if (real_ > 0)
		{
			real = real_;
		}
		else
		{
			cout << "실수부는 0보다 큰 수를 입력해주세요!" << endl;
		} 

	}
	double GetImag()//getter
	{
		return imag;
	}
	void SetImag(double imag_)//setter
	{
		if (imag_ > 0)
		{
			imag = imag_;
		}
		else
		{
			cout << "허수부는 0보다 큰 수를 입력해주세요!" << endl;
		}
	}
private:
	double real;
	double imag;

};
int main()
{
	Complex c1; //생성자 1번 호출
	Complex c2 = Complex(2, 3); //생성자 2번 호출
	Complex c3(3, 4); //생성자 2번 호출
	Complex c4 = { 5,6 }; //생성자 2번 호출
	Complex c5 = Complex{ 7,8 }; //생성자 2번 호출
	Complex c6{ 9,1 }; //생성자 2번 호출

	cout << "c1 = " << c1.GetReal() << ", " << c1.GetImag() << endl;
	cout << "c2 = " << c2.GetReal() << ", " << c2.GetImag() << endl;
	cout << "c3 = " << c3.GetReal() << ", " << c3.GetImag() << endl;
	cout << "c4 = " << c4.GetReal() << ", " << c4.GetImag() << endl;
	cout << "c5 = " << c5.GetReal() << ", " << c5.GetImag() << endl;
	cout << "c6 = " << c6.GetReal() << ", " << c6.GetImag() << endl;
	
	//< getter setter 사용법 >
	//정보 은닉과 객체의 무결성을 위해 변수 real과 imag 를 private하여 직접접근은 불가능하게 만들어놓고,
	//대신 getter함수와 setter함수를 통해서 이 변수에 간접접근할수 있도록 함!
	//밑처럼 setter함수를 호출하여 값을 넘겨주고, getter함수를 호출하여 값을 다시 돌려받는다.
	//밑의 z2,z3처럼 setter함수에 if 조건문을 걸어 일정 조건에 합당하지 않는 비유효한 값을 필터링 하는 경우도 많다.

	Complex z1;
	z1.SetReal(80);
	z1.SetImag(5);
	cout << z1.GetReal() << '.' << z1.GetImag() << endl;

	Complex z2;
	z2.SetReal(-5);
	z2.SetImag(10);
	cout << z2.GetReal() << '.' << z2.GetImag() << endl;

	Complex z3;
	z3.SetReal(3);
	z3.SetImag(-4);
	cout << z3.GetReal() << '.' << z3.GetImag() << endl;
}
