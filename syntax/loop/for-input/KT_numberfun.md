{% tabs %}
{% tab title='KT_numberfun.md' %}

> Question

* a, b, c가 주어 질 때, a, b와 +, -, *, / 로 c를 만들 수 있으면 Possible 불가능 하면 Impossible을 출력하라

```txt
Input:
6
1 2 3
2 24 12
5 3 1
9 16 7
7 2 14
12 4 2

Output:
Possible
Possible
Impossible
Possible
Possible
Impossible
```

{% endtab %}
{% tab title='KT_numberfun.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  a, b, c = map(int, input().split())
  if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
    print("Possible")
  else:
    print("Impossible")
```

{% endtab %}
{% endtabs %}
