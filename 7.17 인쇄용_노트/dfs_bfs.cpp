#include<bits/stdc++.h>
//dfs,bfs
using namespace std;
vector<int> v[1004]; //2���� �迭���� ����

int visit[1004], ch[1004]; //���������� �� 0���� �⺻ �ʱ�ȭ!
void dfs(int x) { //����Լ��� �̿��ϸ� ������ ���� �ʿ䰡 ����.
	visit[x] = 1;
	cout << x << ' ';
	for (auto t : v[x]) { //x �� ������ ������ �� �湮���� ���� �������� ��� dfs�Ѵ�.
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
	dfs(k); //dfs ��
	cout << '\n';

	//bfs ����
	queue<int> q; //bfs�� ť�� ������ �Ѵ�.
	q.push(k);
	ch[k] = 1;
	while (!q.empty()) {
		int x = q.front(); //front�� �����°� �ƴϰ� �� ���� ������ ������ �ϴ°�!
		cout << x << ' ';
		q.pop();
		for (int i = 0; i < v[x].size(); i++)
		{
			//if (ch[v[x][i]] == 0)  //������ ������ �� �湮 ���� �������� �ִٸ�
			//{
			//	ch[v[x][i]] = 1; //�湮�ߴٴ� üũ�� �ϰ�
			//	q.push(v[x][i]); //ť�� push�ϱ�
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