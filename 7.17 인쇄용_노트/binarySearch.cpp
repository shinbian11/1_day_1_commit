#include<bits/stdc++.h>
//이분 탐색
using namespace std;
typedef long long ll;
ll a[1000005]; //나무의 높이
ll n, m;
ll pos(ll x) {
	ll sum = 0;
	for (int i = 0; i < n; i++) {
		if (a[i] >= x) {
			sum += a[i] - x;
		}
	}
	return (sum >= m);
}
int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	ll s=0, e=1e18, ans=0;
	while (s <= e) {
		ll mid = (s + e) / 2;
		if (pos(mid)) {
			ans = max({ ans, mid });
			s = mid + 1;
		}
		else {
			e = mid - 1;
		}
	}
	cout << ans;
}