{% tabs %}
{% tab title='KT_3dprinter.md' %}

> Question

* You can make 3d printer or prodcut using 3d printer
* What is the minimum possible number of days needed to print at least 𝑛 statues?

```txt
Input: 5
Output: 4
```

{% endtab %}
{% tab title='KT_3dprinter.py' %}

```py
from math import ceil, log
line = int(input())
print(int(ceil(log(line, 2) + 1)))
```

{% endtab %}
{% endtabs %}
