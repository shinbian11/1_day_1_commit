#include<bits/stdc++.h>
//dfs,bfs
using namespace std;
vector<int> v[1004]; //2차원 배열같은 느낌

int visit[1004], ch[1004]; //전역변수는 다 0으로 기본 초기화!
void dfs(int x) { //재귀함수를 이용하면 스택을 만들 필요가 없다.
	visit[x] = 1;
	cout << x << ' ';
	for (auto t : v[x]) { //x 와 인접한 정점들 중 방문하지 않은 정점들은 모두 dfs한다.
		if (visit[t] == 0) {
			dfs(t);
		}
	}
}
int main() {
	int n, m, k;
	cin >> n >> m >> k;
	for (int i = 0; i < m; i++) {
		int s, e;
		cin >> s >> e;
		v[s].push_back(e);
		v[e].push_back(s);
	}
	for (int i = 1; i <= n; i++) {
		sort(v[i].begin(), v[i].end());
	}
	dfs(k); //dfs 끝
	cout << '\n';

	//bfs 시작
	queue<int> q; //bfs는 큐를 만들어야 한다.
	q.push(k);
	ch[k] = 1;
	while (!q.empty()) {
		int x = q.front(); //front는 날리는게 아니고 맨 앞의 정점을 참조만 하는것!
		cout << x << ' ';
		q.pop();
		for (int i = 0; i < v[x].size(); i++)
		{
			//if (ch[v[x][i]] == 0)  //인접한 정점들 중 방문 안한 정점들이 있다면
			//{
			//	ch[v[x][i]] = 1; //방문했다는 체크를 하고
			//	q.push(v[x][i]); //큐에 push하기
			//}
			for (auto t : v[x])
			{
				if (ch[t] == 0)
				{
					ch[t] = 1;
					q.push(t);
				}
			}
		}
	}
	return 0;
}