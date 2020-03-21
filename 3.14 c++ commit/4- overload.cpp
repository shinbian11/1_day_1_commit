#include <iostream>
//함수 overload(오버로드) : 다중 정의
void swap(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}
void swap(double& a, double& b)
{
	double tmp = a;
	a = b;
	b = tmp;
}
void swap(int* (&a), int* (&b))
{
	int* tmp = a;
	a = b;
	b = tmp;
}

int main()
{
	int a = 20, b = 30;
	double da = 2.222, db = 3.333;
	int* pa = &a, * pb = &b;

	//함수의 이름이 같아도 매개변수의 형을 자동으로 찾아준다.
	swap(a, b); 
	swap(da, db);
	swap(pa, pb);


	std::cout << "a : " << a << std:: endl;
	std::cout << "b : " << b << std:: endl;

	std::cout << "da : " << da << std:: endl;
	std::cout << "db : " << db << std:: endl;

	std::cout << "*pa : " << *pa << std:: endl;
	std::cout << "*pb : " << *pb << std:: endl;

}