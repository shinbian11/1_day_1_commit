//C++ : 10972번 백준: 다음 순열

#include <bits/stdc++.h>
#define F_I ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

typedef long long ll;
using namespace std;

int main()
{
	F_I;
	int n;
	cin >> n;
	vector<int> v(n);


	for (int i = 0; i < n; i++) //순열 입력 받기
		cin >> v[i];

	//입력받은 순열이 가장 마지막 순열이라면, -1 출력
	//가장 마지막 순열은.. 모든 원소들이 내림차순이다. (맨 앞의 원소가 제일 크고, 점점 작아진다. 예를 들면, 4 3 2 1)
	bool flag = true;

	for (int i = 0; i < n - 1; i++)
	{
		if (v[i] < v[i + 1])
			flag = false;
	}
	if (flag == true) //사전순으로 가장 마지막 순열이라면
	{
		cout << -1 << '\n';
		return 0;
	}

	while (next_permutation(v.begin(), v.end()))
	{
		for (int i = 0; i < n; i++)
			cout << v[i] << ' ';
		cout << '\n';
		return 0; //다음 순열 하나만 출력하고 프로그램 끝내야 하니까, 하나만 출력하고 바로 return 0; 하기!
	}
}