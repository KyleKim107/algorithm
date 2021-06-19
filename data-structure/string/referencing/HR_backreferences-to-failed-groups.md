{% tabs %}
{% tab title='HR_backreferences-to-failed-groups.md' %}

> Question

* consists of 8 digits
* may have "-" separator such that string gets divided in 4 parts, with each part having exactly two digits

```txt
Input: 12-45-7810
Output: false
```

{% endtab %}
{% tab title='HR_backreferences-to-failed-groups.py' %}

```py
import re
pattern = r'^\d\d(-?)\d\d\1\d\d\1\d\d$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
