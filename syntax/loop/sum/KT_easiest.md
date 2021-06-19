{% tabs %}
{% tab title='KT_easiest.md' %}

> Question

* single integer number p which is the minimal number st N * p has the same sum of digits as N and p is bigger than 10

```txt
Input:
3029
4
5
42
0

Output:
37
28
28
25
```

{% endtab %}
{% tab title='KT_easiest.py' %}

```py
def SOD(st):
  return sum(map(int, st))
while True:
  n = input()
  if n == '0':
    break
  for i in range(11, 100000):
    if SOD(n) == SOD(str(int(n) * i)):
      print(i)
      break
```

{% endtab %}
{% endtabs %}
