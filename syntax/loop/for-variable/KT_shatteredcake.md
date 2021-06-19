{% tabs %}
{% tab title='KT_shatteredcake.md' %}

> Question

* 첫 줄에는 원 케익의 가로 길이가 주어진다
* 케익이 정확히 N등분 되어 N개의 줄에 각 조각의 가로 세로 길이가 주어지는데 이 때 원 케익의 세로 길이를 출력

```txt
Input:
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
Output: 6
```

{% endtab %}
{% tab title='KT_shatteredcake.py' %}

```py
w = int(input())
total = 0
for _ in range(int(input())):
  a, b = map(int, input().split())
  total += a * b
print(total // w)
```

{% endtab %}
{% endtabs %}
