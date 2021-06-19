{% tabs %}
{% tab title='HR_negative-lookbehind.md' %}

> Question

* Write a regex which can match all the occurences of characters which are not immediately preceded by vowels

```txt
Input: abru
Output: Number of matches : 3   # abr
```

{% endtab %}
{% tab title='HR_negative-lookbehind.py' %}

```py
import re

pattern = r"(?<![aeiouAEIOU])."
match = re.findall(pattern, input)

print("Number of matches :", len(match))
```

{% endtab %}
{% endtabs %}
