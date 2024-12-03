#include <bits/stdc++.h>
#define f first
#define s second
#define pb push_back
#define pii pair<int, int>
#define endl '\n'
#define vi vector<int>
#define vvi vector<vi>
#define vvvi vector<vvi>
#define vvvvi vector<vvvi>
#define vl vector<ll>
#define vvl vector<vl>
#define vld vector<ld>
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vpii vector<pii>
#define vvpii vector<vpii>
#define vpll vector<pll>
#define rep(s, l, r) for (int s = l; s < r; s++)
#define per(s, r, l) for (int s = r - 1; s >= l; s--)
#define all(x) x.begin(), x.end()
typedef long long ll;
typedef long double ld;
using namespace std;
template<class T> using minheap = priority_queue<T, vector<T>, greater<T>>;
template<typename T> void setmax(T& a, T b) { a = max(a, b); };
template<typename T> void setmin(T& a, T b) { a = min(a, b); };
template<typename T> bool in(T lo, T v, T hi) { return lo <= v && v <= hi; };

struct node {
  node *ne;
  int value;
};

node* do_step(map<int, node*> &getNode, node* cur) {
  set<int> rem;
  node *ptr = cur;
  node *tb = ptr->ne, *te;
  for (int i = 0; i < 3; i++) {
    ptr = ptr->ne;
    rem.insert(ptr->value);
  }
  te = ptr;
  ptr = ptr->ne;
  cur->ne = ptr; // remove

  // get next label
  int curLabel = cur->value;
  curLabel -= 1;
  while (true) {
    if (rem.count(curLabel)) {
      curLabel -= 1;
    } else if (getNode.count(curLabel)) {
      break;
    } else {
      curLabel = getNode.rbegin()->first;
    }
  }
  ptr = getNode[curLabel];
  node* ptr2 = ptr->ne;
  ptr->ne = tb;
  te->ne = ptr2;

  return cur->ne;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  string s;
  cin >> s;
  vi cyc;
  for (char ch : s) {
    cyc.pb(int(ch - '0'));
  }
  for (int i = 1 + *max_element(all(cyc)); i <= 1e6; i++) {
    cyc.pb(i);
  }

  int n = cyc.size();

  map<int, node*> getNode;
  vector<node> nodes(cyc.size());

  for (int i = 0; i < n; i++) {
    nodes[i] = {NULL, cyc[i]};
  }
  for (int i = 0; i < n; i++) {
    nodes[i].ne = &nodes[(i + 1) % n];
  }
  for (int i = 0; i < n; i++) {
    getNode[nodes[i].value] = &nodes[i];
  }

  node* cur = &nodes[0];
  for (int i = 0; i < 10000000; i++) {
    cur = do_step(getNode, cur);
  }

  node* ptr = getNode.rbegin()->second;

  while (ptr->value != 1)  {
    ptr = ptr->ne;
  }

  ll result = 1;

  ptr = ptr->ne;
  result *= ptr->value;

  ptr = ptr->ne;
  result *= ptr->value;
  cout << result << endl;

  return 0;
}
