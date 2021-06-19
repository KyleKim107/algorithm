{% tabs %}
{% tab title='KT_helpaphd.md' %}

> Question

* n개 줄의 a + b가 주어진다. 이 때 결과 값을 출력하라. 단 P=NP 가 주어질 때는 skipped를 출력하라

```txt
Input:
4
2+2
1+2
P=NP
0+0

Output:
4
3
skipped
0
```

{% endtab %}
{% tab title='KT_helpaphd.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  line = input()
  if line == 'P=NP':
    print('skipped')
  else:
    print(eval(line))
```

{% endtab %}
{% endtabs %}
