{% tabs %}
{% tab title='KT_mixedfractions.md' %}

> Question

* 각 줄에 a, b 가 주어진다
* 이 때 a / b 인 분수를 대분수로 형식으로 출력하라. a, b가 둘다 0 일 경우 종료한다

```txt
Input:
27 12
2460000 98400
3 4000
0 0

Output:
2 3 / 12
25 0 / 98400
0 3 / 4000
```

{% endtab %}
{% tab title='KT_mixedfractions.py' %}

```py
while True:
  dem, num = map(int, input().split())
  if dem == num == 0:
    break
  print(dem // num, dem % num, '/', num)
```

{% endtab %}
{% endtabs %}
