{% tabs %}
{% tab title='KT_railroad2.md' %}

> Question

* a와 b가 주어진다
* b가 짝수이면 possible 홀수이면 impossible을 출력한다

```txt
Input: 0 2
Output: possible
```

{% endtab %}
{% tab title='KT_railroad2.py' %}

```py
a, b = map(int, input().split())
print("possible" if b % 2 == 0 else "impossible")
```

{% endtab %}
{% endtabs %}
