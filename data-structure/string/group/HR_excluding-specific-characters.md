{% tabs %}
{% tab title='HR_excluding-specific-characters.md' %}

> Question

* must be of length 6
* First character should not be a digit
* Second character should not be a lowercase vowel
* Third character should not be b, c, D or F
* Fourth character should not be a whitespace character ( \r, \n, \t, \f or \<space> )
* Fifth character should not be a uppercase vowel
* Sixth character should not be a . or , symbol

```txt
Input: think?
Output: true
```

{% endtab %}
{% tab title='HR_excluding-specific-characters.py' %}

```py
import re

pattern = r'^[^\d][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}
