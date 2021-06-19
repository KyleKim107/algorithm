{% tabs %}
{% tab title='KT_jobexpenses.md' %}

> Question

* 첫줄에 N이 주어진다
* 다음 줄에 N개의 숫자가 주어지는데, 이 때 0보다 작은 수의 절대값의 합을 구하여라

```txt
Input:
3
1 -2 3

Output: 2
```

{% endtab %}
{% tab titlepyT_jobexpenses.md'' %}

```py
print(sum(n for n in map(int, input().split()) if n < 0))
```

{% endtab %}
{% endtabs %}
