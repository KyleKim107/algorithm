{% tabs %}
{% tab title='HR_matching-x-y-repetitions.md' %}

> Question

* should begin with 3, 4 or 5 digits
* After that, should have 3 or more letters (both lowercase and uppercase)
* Then should end with up to 3 symbol(s). You can end with 0 to 3. symbol(s), inclusively

{% endtab %}
{% tab title='HR_matching-x-y-repetitions.py' %}

```py
import re
pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
