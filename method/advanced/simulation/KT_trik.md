{% tabs %}
{% tab title='KT_trik.md' %}

> Question

* Print location of cup at the end of simulation

```txt
Input: CBABCACCC
Output: 1
```

{% endtab %}
{% tab title='KT_trik.py' %}

```py
moves = input()
cur = 1
for move in moves:
  if move == 'A':
    if cur == 1:
      cur = 2
    elif cur == 2:
      cur = 1
  elif move == 'B':
    if cur == 2:
      cur = 3
    elif cur == 3:
      cur = 2
  else:
    if cur == 1:
      cur = 3
    elif cur == 3:
      cur = 1
print(cur)
```

{% endtab %}
{% endtabs %}
