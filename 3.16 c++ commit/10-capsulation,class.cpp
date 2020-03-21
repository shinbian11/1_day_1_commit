//클래스 = 자료 저장(변수) + 자료 처리(함수)
//클래스(타입) : 특정한 용도를 수행하기 위한 변수와 함수를 모아 둔 틀(자료형)
//객체(오브젝트) : 그 틀을 이용하여 찍어낸 객체 (변수, 메모리 상의 공간)

#include <iostream>

using namespace std;

//접근 제어 지시자 : private,protected,public

//<< struct와 class 의 차이점! >>

//-> struct내에서는 접근 제어 지시자를 사용하지 않으면 기본값이 public이다.
//-> class내에서는 접근 제어 지시자를 사용하지 않으면 기본값이 private이다.

struct TV {
	//내부 변수들을 보호하며 외부 사용자들에게 보여주는 인터페이스를 구현하는 것을 캡슐화라고 함.

private: //변수들을 다른곳에서 막 바꾸지 못하도록 보호
	bool powerOn;
	int channel;
	int volume;

public: //public 선언한 함수 안에 if문 넣어서 올바른 입력만 될수 있도록 필터링 작업을 거침!
	void on()
	{
		powerOn = true;
		cout << "TV를 켰습니다." << endl;
	}
	void off()
	{
		powerOn = false;
		cout << "TV를 껐습니다." << endl;
	}
	void setChannel(int cnl)
	{
		if (cnl >= 1 && cnl <= 999)
		{
			channel = cnl;
			cout << "채널을 " << cnl << "(으)로 바꿨습니다." << endl;
		}
	}
	void setVolume(int vol)
	{
		if (vol >= 0 && vol <= 100)
		{
			volume = vol;
			cout << "볼륨을 " << vol << "(으)로 바꿨습니다." << endl;
		}
	}
};
int main()
{
	TV lg;
	lg.on();
	lg.setChannel(10);
	lg.setVolume(50);
	//lg.setChannel(-73);
}