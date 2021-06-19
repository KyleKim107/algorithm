{% tabs %}
{% tab title='KT_apaxiaaans.md' %}

> Question

* Print consecutive character at most once

```txt
Input: rooobert
Output: robert
```

{% endtab %}
{% tab title='KT_apaxiaaans.py' %}

```py
st = input()
for i, c in enumerate(st):
  if i == 0 or st[i - 1] != c:
    print(c, end='')
```

{% endtab %}
{% endtabs %}
