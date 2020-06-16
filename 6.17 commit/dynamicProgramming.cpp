#include <iostream>
//���� ���α׷��� dp (������ �߿�. ������ ������ ����)
using namespace std;
long long cnt;
long long dp[14]; //dp �迭�� ���ǰ� �߿�
/*
int f(int n) { //brute-force(����õ)
	cnt++;
	if (n == 0) return 1;
	int ans = 0;
	for (int i = 1; i <= 3; i++) {
		if(n-i>=0)
		ans += f(n - i);
	}
	return ans;
}*/

int f(int n) { //top-down
	cnt++;
	if (n == 0) return 1;
	if (dp[n] != 0)return dp[n];
	int ans = 0;
	for (int i = 1; i <= 3; i++) {
		if(n-i>=0)
		ans += f(n - i);
	}
	return dp[n]=ans;
}
int main()
{
	/* bottom-up
	dp[0] = 1;
	for (int i = 1; i <= 10; i++) {
		for (int j = 1; j <= 3; j++) {
			if (i - j >= 0) {
				dp[i] += dp[i - j];
			}
		}
	}*/
	int tc;
	cin >> tc;
	while (tc--) {
		int n;
		cin >> n;
		cout << f(n) << '\n';
	}
}