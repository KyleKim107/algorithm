{% tabs %}
{% tab title='HR_saying-hi.md' %}

> Question

* The first character must be the letter H or h
* The second character must be the letter I or i
* The third character must be a single space
* The fourth character must not be the letter D or d

```txt
Input:
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

Output: Hi Alex how are you doing
```

{% endtab %}
{% tab title='HR_saying-hi.py' %}

```py
import re, sys
for s in filter(re.match(r"(?i:hi\s[^d])", sys.stdin)):
  print(s.strip())
```

{% endtab %}
{% endtabs %}
