//C++

//น้มุ 14501น๘ : ล๐ป็
#include <bits/stdc++.h>
#define F_I ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
using namespace std;
typedef long long ll;
int n;
int t[16];
int p[16];
int ans = 0;
void go(int day, int sum)
{
	
	if (day == n)
	{
		if (ans < sum)
			ans = sum;
		return;	
	}
	if (day > n)
		return;

	go(day + t[day], sum + p[day]);
	go(day + 1, sum);
}
int main() {
	
	cin >> n;
	
	for (int i = 0; i < n; i++)
		cin >> t[i] >> p[i];
	go(0,0);
	cout << ans << '\n';
}