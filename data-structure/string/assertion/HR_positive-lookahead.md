{% tabs %}
{% tab title='HR_positive-lookahead.md' %}

> Question

* Write a regex that can match all occurrences of o followed immediately by oo in S

```txt
Input: gooooo!
Output: Number of matches : 3
```

{% endtab %}
{% tab title='HR_positive-lookahead.py' %}

```py
import re

Test_String = input()

pattern = r"o(?=oo)"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```

{% endtab %}
{% endtabs %}
