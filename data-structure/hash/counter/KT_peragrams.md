
{% tabs %}
{% tab title='KT_peragrams.md' %}

> Question

* Peragrams is Palindrome when suffle it's character
* Given string, how many character should I remove to make Peragrams

```txt
Input: abc
Output: 0
```

{% endtab %}
{% tab title='KT_peragrams.py' %}

```py
from collections import Counter
cnt = Counter()
for ch in input():
  cnt[ch] += 1
ret = 0
for count in cnt:
  if cnt[count] % 2 == 1:
    ret += 1
print(max(0, ret - 1))
```

{% endtab %}
{% endtabs %}
