{% tabs %}
{% tab title='KT_dicegame.md' %}

> Question

* 두줄에 거쳐 총 8개의 수가 주어진다
* 이 때 위 줄의 합이 크면 Emma 아랫줄의 합이 크면 Gunnar, 같을 시에는 Tie를 출력하라

```txt
Input:
1 2 3 4
1 2 3 5

Output: Gunnar
```

{% endtab %}
{% tab title='KT_dicegame.py' %}

```py
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
if a < b:
  print('Emma')
elif b < a:
  print('Gunnar')
else:
  print('Tie')
```

{% endtab %}
{% endtabs %}
