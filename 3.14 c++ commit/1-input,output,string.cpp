//C:\Users\shinb\Downloads\������ ����\c++   �� ���!
//C:\Users\shinb\OneDrive\����\GitHub\MyProject\C-Project\repository   �� ���!
#include <iostream> //<stdio.h> �ƴϴ�!
#include <string> //<string.h> �ƴϴ�!
using namespace std; // std::cout => cout,   std::endl => endl

int main()
{
	//���
	cout << "Hello World!" << endl;


	//�Է�
	int a, b;
	cin >> a >> b; //���Ĺ���(%d,%c ���) �ʿ� ����! �Է¹޴� �������� �ڷ����� �˾Ƽ� ó������!
	cout << a << " + " << b << " = " << a + b << endl;

	//���ڿ�
	string str; //���ڿ� �ڷ����� string �̴�. 
	str = "Hello World"; //�迭�� �ƴϹǷ� ���̸� �� �ʿ䰡 ����.
	cout << str << endl;

	string name;
	cout << "�̸� �Է� : ";
	cin >> name;
	string message = "�ȳ��ϼ���, " + name + " ��!"; //���ڿ��� c���� �ξ� �����ϰ� ��밡���ϴ�. (strcpy ���� �Լ� ������� �ʰ� + ��ȣ�� ���ڿ����� �����ϼ� �ִ� ��ó��!)
	cout << message << endl;
}