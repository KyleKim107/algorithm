{% tabs %}
{% tab title='KT_mirror.md' %}

> Question

* Print mirrored string

```txt
Input:
2
2 2
.*
..
4 4
***.
**..
....
....

Output:
Test 1
..
*.
Test 2
....
....
..**
.***
```

{% endtab %}
{% tab title='KT_mirror.py' %}

```py
n_test = int(input())
for test in range(1, n_test + 1):
  R, C = map(int, input().split())
  G = [input() for _ in range(R)]
  print(f"Test {test}")
  for st in reversed(G):
    print("".join(reversed(st)))
```

{% endtab %}
{% endtabs %}
