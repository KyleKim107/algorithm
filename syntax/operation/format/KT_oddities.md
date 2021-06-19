{% tabs %}
{% tab title='KT_oddities.md' %}

> Question

* n 이 짝수이면 n is even 홀수이면 n is odd 라고 출력하라

```txt
Input:
2
1
2

Output:
1 is even
2 is odd
```

{% endtab %}
{% tab title='KT_oddities.py' %}

```py
for _ in range(int(input())):
  n = int(input())
  if n % 2 == 0:
    print(f"{n} is even")
  else:
    print(f"{n} is odd")
```

{% endtab %}
{% endtabs %}
