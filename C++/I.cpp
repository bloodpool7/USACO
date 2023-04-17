#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int n, m;
    cin >> n;
    cin >> m;
    int nums[n];
    vector< tuple<int, int> > todo;
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    for (int i = 0; i < m; i++){
        int x, y;
        cin >> x;
        cin >> y;
        todo.push_back(tuple<int, int>(x, y))
    }
}