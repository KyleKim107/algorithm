{% tabs %}
{% tab title='HR_uk-and-us.md' %}

> Question

* For some spelling, US uses -se, while UK uses -ze
* Given text, find the number of occurence from sentence either of them

```txt
Input:
2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize

Output: 2
```

{% endtab %}
{% tab title='HR_uk-and-us.py' %}

```py
import re

text = '\n'.join(input() for _ in range(int(input())))
for n in range(int(input())):
  e = input()
  print(len(re.findall(f"{e[:len(e)-2]}[sz]e", text)))
```

{% endtab %}
{% endtabs %}
