{% tabs %}
{% tab title='KT_runlengthencodingrun.md' %}

> Question

* Convert using two rules

```txt
Input: E HHHeellloWooorrrrlld!!
Output: H3e2l3o1W1o3r4l2d1!2
```

{% endtab %}
{% tab title='KT_runlengthencodingrun.py' %}

```py
t, s = input().split()
if t == 'E':
  row = 1
  for i, ch in enumerate(s):
    if i == len(s) - 1 or s[i + 1] != s[i]:
      print(ch + str(row), end='')
      row = 1
    else:
      row+=1
else:
  for i in range(1, len(s), 2):
    print(s[i - 1] * int(s[i]), end='')
```

{% endtab %}
{% endtabs %}
