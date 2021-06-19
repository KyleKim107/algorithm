{% tabs %}
{% tab title='KT_alphabetspam.md' %}

> Question

* 첫줄에 문장이 주어진다
* 이 때 문장에서 _의 비율, 소문자의 비율, 대문자의 비율, 나머지 부호의 비율을 각각 출력하라

```txt
Input: Welcome_NWERC_participants!

Output:
0.0740740740740741
0.666666666666667
0.222222222222222
0.0370370370370370
```

{% endtab %}
{% tab titlepyT_alphabetspam.md'' %}

```py
st = input()
white = 0
lower = 0
upper = 0
symbol = 0
for ch in st:
  if ch == '_':
    white += 1
  elif ch.islower():
    lower += 1
  elif ch.isupper():
    upper += 1
  else:
    symbol += 1

total = white + lower + upper + symbol
print(white / total)
print(lower / total)
print(upper / total)
print(symbol / total)
```

{% endtab %}
{% endtabs %}
