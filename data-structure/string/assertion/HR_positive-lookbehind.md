{% tabs %}
{% tab title='HR_positive-lookbehind.md' %}

> Question

* Write a regex which can match all the occurences of digit which are immediately preceded by odd digit

> Question

```txt
Input: 123Go!
Output: 1
```

{% endtab %}
{% tab title='HR_positive-lookbehind.py' %}

```py
import re
Test_String = input()
pattern = r"(?<=[13579])\d"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```

{% endtab %}
{% endtabs %}
