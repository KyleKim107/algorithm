{% tabs %}
{% tab title='HR_matching-one-or-more-repititions.md' %}

> Question

* begin with  or more digits
* After that, should have 1 or more uppercase letters
* should end with 1 or more lowercase letters

```txt
Input: 1Qa
Output: true
```

{% endtab %}
{% tab title='HR_matching-one-or-more-repititions.py' %}

```py
import re
pattern = r'^\d+[A-Z]+[a-z]+$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
