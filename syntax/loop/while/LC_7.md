{% tabs %}
{% tab title='LC_7.md' %}

> Question

* Reverse integer

```txt
Input: 421
Output: 124
```

{% endtab %}
{% tab title='LC_7.cpp' %}

```cpp
class Solution {
public:
  int reverse(int x) {
    long r = 0;
    while (x) r = r * 10 + x % 10, x /= 10;
    return (int(r) == r) * r;
  }
};
```

{% endtab %}
{% endtabs %}
