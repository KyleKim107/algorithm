{% tabs %}
{% tab title='HR_matching-start-end.md' %}

> Question

* must start with a digit and end with . symbol
* should be characters long only

```txt
Input: 0qwer.
Output: true
```

{% endtab %}
{% tab title='HR_matching-start-end.py' %}

```py
import re

pattern = r'^\d\w\w\w\w\.$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
