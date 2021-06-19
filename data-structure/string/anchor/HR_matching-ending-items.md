{% tabs %}
{% tab title='HR_matching-ending-items.md' %}

> Question

* should consist of only lowercase and uppercase letters (no numbers or symbols)
* should end in s

```txt
Input: Kites
Output: true
```

{% endtab %}
{% tab title='HR_matching-ending-items.py' %}

```py
import re
pattern = r'^[a-zA-Z]*s$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
