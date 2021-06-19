{% tabs %}
{% tab title='KT_missingnumbers.md' %}

> Question

* print all missing number

```txt
Input:
9
2
4
5
7
8
9
10
11
13

Output:
1
3
6
12
```

{% endtab %}
{% tab title='KT_missingnumbers.py' %}

```py
n = int(input())
gap = False
prev = 0
for i in range(n):
  a = int(input())
  for j in range(prev + 1, a):
    print(j)
    gap = True
  prev = a
if not gap:
  print('good job')
```

{% endtab %}
{% endtabs %}
