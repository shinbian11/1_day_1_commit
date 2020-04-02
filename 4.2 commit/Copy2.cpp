#include <iostream>
using namespace std;

class String {
public:
	String()
	{
		cout << "String() ������ ȣ��" << endl;
		strData = NULL;
		len = 0;
	}
	String(const char* str)
	{
		cout << "String(const char*) ������ ȣ��" << endl;
		len = strlen(str);
		strData = new char[len + 1];
		cout << "strData �Ҵ� : " << (void*)strData << endl;
		strcpy(strData, str); //���� ����
	}
	String(const String& rhs) //���� ������
	{
		cout << "String(String& rhs) ������ ȣ��" << endl;
		strData = new char[rhs.len + 1];
		cout << "strData �Ҵ� : " << (void*)strData << endl;
		strcpy(strData, rhs.strData); //���� ����
		len = rhs.len; //���� ����
	}
	~String()
	{
		cout << "~String() �Ҹ��� ȣ��" << endl;
		delete[] strData;
		cout << "strData ������ : " << (void*)strData << endl;
		strData = NULL;
	}

	String& operator=(const String& rhs)//������ �����ε�
	{
		if (this != &rhs)//rhs�� �ּҰ� != this �϶���! ���� ����Ű�°� �ٸ�����!
		{
			delete[] strData;//���� �Ҵ��ϰ� �ִ� �޸𸮸� ����
			strData = new char[rhs.len + 1];
			cout << "strData �Ҵ� : " << (void*)strData << endl;
			strcpy(strData, rhs.strData); //���� ����
			len = rhs.len; //���� ����
		}
		

		return *this; //�� �Լ��� �����ִ� ��ü�� �ּҰ��� ����Ű��, �� �� ��ü ��ü�� ��ȯ
	}

	char* GetStrData() const
	{
		return strData;
	}
	int GetLen() const
	{
		return len;
	}
private:
	char* strData;
	int len; 
};
int main()
{
	String s1("�ȳ�");
	String s2(s1); //���� ������
	String s3("Hello");
	s3.operator=(s3); //s3 = s3;


	cout << s1.GetStrData() << endl;
	cout << s2.GetStrData() << endl;
	cout << s3.GetStrData() << endl;

}