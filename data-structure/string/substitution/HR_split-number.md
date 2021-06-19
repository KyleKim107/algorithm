{% tabs %}
{% tab title='HR_split-number.md' %}

> Question

* There might either be a hyphen, or a space between the segments
* The country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each

```txt
Input:
2
1 877 2638277
91-011-23413627

Output:
CountryCode=1,LocalAreaCode=877,Number=2638277
CountryCode=91,LocalAreaCode=011,Number=23413627
```

{% endtab %}
{% tab title='HR_split-number.py' %}

```py
import re
for i in range(int(input())):
  a, b, c = (re.sub(r"[ -]", " ", input())).split()
  print(f"CountryCode={a},LocalAreaCode={b},Number={c}")
```

{% endtab %}
{% endtabs %}
