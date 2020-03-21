#include <iostream>

using namespace std;

class Complex
{
public:

	//Complex()
	//{
	//	real = 0;
	//	imag = 0;
	//}
	//Complex(double real_, double imag_)
	//{
	//	real = real_;
	//	imag = imag_;
	//}

	//위의 생성자를 밑처럼 표현할수도 있다! 생성자 초기화 목록!

	Complex() : real(0), imag(0) { }
	Complex(double real, double imag) : real(real), imag(imag) {}
	//Complex(double real_, double imag_) : real(real_), imag(imag_) {}
	

	double GetReal() //getter
	{
		return real;
	}
	void SetReal(double real_)//setter
	{
		real = real_;
	}
	double GetImag()//getter
	{
		return imag;
	}
	void SetImag(double imag_)//setter
	{
		imag = imag_;
	}
private:
	double real;
	double imag;
};
int main()
{

	Complex c1; //생성자 1번 호출
	Complex c2 = Complex(2, 3); //생성자 2번 호출
	Complex c3(2,3); //생성자 2번 호출


	cout << "c1 = " << c1.GetReal() << ", " << c1.GetImag() << endl;
	cout << "c2 = " << c2.GetReal() << ", " << c2.GetImag() << endl;
	cout << "c3 = " << c3.GetReal() << ", " << c3.GetImag() << endl;

}