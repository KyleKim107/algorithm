{% tabs %}
{% tab title='HR_negative-lookahead.md' %}

> Question

* Write a regex which can match all characters which are not immediately followed by that same character

```txt
Input: gooooo
Output: 2
```

{% endtab %}
{% tab title='HR_negative-lookahead.py' %}

```py
import re

Test_String = input()
pattern = r"(.)(?!\1)"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```

{% endtab %}
{% endtabs %}
