{% tabs %}
{% tab title='HR_uk-and-us-2.md' %}

> Question

* For some spelling, US uses or, while UK uses our
* Given UK spelling, find the number of occurence from sentence either of them

```txt
Input:
2
the odour coming out of the leftover food was intolerable
ammonia has a very pungent odor
1
odour

Output: 2
```

{% endtab %}
{% tab title='HR_uk-and-us-2.py' %}

```py
import re
text = '\n'.join(input() for _ in range(int(input())))
for i in range(int(input())):
  s1 = input()
  s2 = s1.replace('our','or')
  print(len(re.findall(rf"\b({s1}|{s2})\b", text)))
```

{% endtab %}
{% endtabs %}
