#include <bits/stdc++.h>
using namespace std;
int dp[1004];
int solve(int n)
{
	if (n == 0) return 1;
	if (n == 1) return 1;
	if (n == 2) return 2;

	if (dp[n] != 0) return dp[n];
	else
		dp[n] = solve(n - 1) + solve(n - 2) + solve(n - 3);

	return dp[n];
}
int main()
{
	int n, tc;
	cin >> tc;
	for (int i = 0; i < tc; i++)
	{
		cin >> n;
		cout << solve(n) << endl;
	}
}