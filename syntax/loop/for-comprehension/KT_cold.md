{% tabs %}
{% tab title='KT_cold.md' %}

> Question

* print number of negative numbers

```txt
Input:
3
5 -10 15

Output:
1
```

{% endtab %}
{% tab title='KT_cold.py' %}

```py
input()
print(len(n for n in map(int, input().split()) if n < 0))
```

{% endtab %}
{% endtabs %}
