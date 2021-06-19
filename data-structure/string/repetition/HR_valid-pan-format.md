{% tabs %}
{% tab title='HR_valid-pan-format.md' %}

> Question

* \<char>\<char>\<char>\<char>\<char>\<digit>\<digit>\<digit>\<digit>\<char>

```txt
Input:
3
ABCDS1234Y
ABAB12345Y
avCDS1234Y

Output:
YES
NO
NO
```

{% endtab %}
{% tab title='HR_valid-pan-format.py' %}

```py
import re
for i in range(int(input())):
  print("YES" if re.match(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', input()) else "NO")
```

{% endtab %}
{% endtabs %}
