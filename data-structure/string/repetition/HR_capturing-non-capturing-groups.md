{% tabs %}
{% tab title='HR_capturing-non-capturing-groups.md' %}

> Question

* should have or more consecutive repetitions of ok

```txt
Input: okokok! cya
Output: true
```

{% endtab %}
{% tab title='HR_capturing-non-capturing-groups.py' %}

```py
import re
pattern = r'(ok){3,}'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
