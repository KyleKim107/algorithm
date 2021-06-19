{% tabs %}
{% tab title='KT_differentdistances.md' %}

> Question

* x1, x2, y1, y2이 주어진다
* 이때 를 출력하라
* 마지막 줄에 0이 나온다

```txt
Input:
1.0 1.0 2.0 2.0 2.0
1.0 1.0 2.0 2.0 1.0
1.0 1.0 20.0 20.0 10.0
0

Output:
1.4142135624
2.0000000000
20.3636957882
```

{% endtab %}
{% tab title='KT_differentdistances.py' %}

```py
while True:
  raw = input()
  if raw == '0':
    break
  a, b, c, d, e = map(float, raw.split())
  print((abs(a - c) ** e + abs(b - d) ** e) ** (1/e))
```

{% endtab %}
{% endtabs %}
