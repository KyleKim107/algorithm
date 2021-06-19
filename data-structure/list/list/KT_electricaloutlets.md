{% tabs %}
{% tab title='KT_electricaloutlets.md' %}

> Question

* Find maximum number of plugs with n plugs with port

```txt
Input:
3
3 2 3 4
10 4 4 4 4 4 4 4 4 4 4
4 10 10 10 10

Output:
7
31
37
```

{% endtab %}
{% tab title='KT_electricaloutlets.py' %}

```py
for _ in range(int(input())):
  li = list(map(int, input().split()))
  count = sum(li) - 2 * li[0] + 1
  print(count)
```

{% endtab %}
{% endtabs %}
