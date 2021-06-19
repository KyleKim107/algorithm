{% tabs %}
{% tab title='KT_pokerhand.md' %}

> Question

* First character is rank
* How many times did msot frequent rank appeared

```txt
Input: AC AD AH AS KD
Output: 4
```

{% endtab %}
{% tab title='KT_pokerhand.py' %}

```py
from collections import Counter
cnter = Counter()
for card in input().split():
  cnter[card[0]]+=1
print(cnter.most_common(1)[0][1])
```

{% endtab %}
{% endtabs %}
