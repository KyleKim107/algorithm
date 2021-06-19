{% tabs %}
{% tab title='CC_ARRAYOPS.md' %}

> Question

* Given a1...an, all equal to 1, use following operation to reach the array b
  * Take index i and multiply by 2
  * Take two indexes i and j and aj from ai

```txt
Input:
3
1 2 3

Output:
4
1 3
1 3
2 3 1
1 2
```

> Solution

* reverse the problem into
  * Take the index i (> 1, < n), and divide it by 2, if bi is divisible by 2
  * a[it2.second] = it2.first + it1.first;
* Suppose all the numbers are odd, else we would keep on dividing them by 2 until they become odd
* Now instead of finding a subset whose gcd equals 1, each time we take the maximum and minimum elements of the array
* Let mx and mi be the maximum and minimum elements of the array respectively
* As soon as we get any element of the array B equal to 1
* Use this element to reduce all elements of array B to 1 as gcd of this element with any other element will be 1
* This will take at most 2*N*log(C) operations

{% endtab %}
{% tab title='CC_ARRAYOPS.py' %}

```cpp
// Time : 2*N*log(C)
#include <bits/stdc++.h>
using namespace std;
int a[(int)1e4 + 12];

inline void normalize(vector<array<int, 3>>& oper, int i){
  while(a[i] % 2 == 0) oper.push_back({1, i, -1}), a[i] /= 2;
}

int main () {
  int t = 1;
  while (t--){
    int n, g = 0;
    vector<array<int, 3>> oper;
    set<pair<int, int>> vals;
    cin >> n;
    for (int i = 0; i < n; i++){
      cin >> a[i];
      normalize(oper, i);
      g = __gcd(g, a[i]);
      vals.insert({a[i], i});
    }

    if (g > 1){
      cout << -1 << endl;
      continue;
    }
    while(1) {
      auto it1 = *vals.begin(), it2 = *vals.rbegin();
      if (it1.first == it2.first && it1.first == 1) break;

      while (it2.first != it1.first) {
        if (it2.first < it1.first) swap(it1, it2);
        vals.erase(it2);
        a[it2.second] = it2.first + it1.first;

        oper.push_back({2, it2.second, it1.second});
        normalize(oper, it2.second);
        it2.first = a[it2.second];
        vals.insert({a[it2.second], it2.second});
      }
    }
    cout << oper.size() << "\n";
    reverse(oper.begin(), oper.end());
    for (auto x : oper) {
      cout << x[0] << " " << x[1] + 1;
      if(x[2] != -1) cout << " " << x[2] + 1;
      cout << "\n";
    }
  }
}
```

{% endtab %}
{% endtabs %}
