{% tabs %}
{% tab title='CC_TDISTS.md' %}

> Question

* Find tree with following property
* The number of pairs of vertices with an even distance between them is x
* The number of pairs of vertices with an odd distance between them is y

```txt
Input:
4
2 2
29 20
3 12
6 3
Output:
YES
2
1 2
YES
7
1 2
1 3
2 4
2 5
3 6
3 7
NO
NO
```

{% endtab %}
{% tab title='CC_TDISTS.py' %}

```py
for _ in range(int(input())):
  x, y = map(int, input().split())
  root = int((x + y) ** 0.5)
  if y % 2 == 1 or x + y != root ** 2:
    print('NO')
    continue
  for i in range(1, int(y ** 0.5) + 1):
    n, m = i, root-i
    if n ** 2 + m ** 2 == x and 2 * n * m == y:
      print('YES')
      print(root)
      for i in range(n):
        print(1, 2 + i)
      for i in range(m-1):
        print(2, 2 + n + i)
      break
  else:
    print('NO')
```

{% endtab %}
{% endtabs %}
