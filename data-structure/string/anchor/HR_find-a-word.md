{% tabs %}
{% tab title='HR_find-a-word.md' %}

> Question

* For every word, print the number of occurrences of the word in all the N sentences listed

```txt
Input:
1
foo bar (foo) bar foo-bar foo_bar foobar bar-foo bar, foo.
2
foo
foobar

Output:
5  # foobar doesn't count
1
```

{% endtab %}
{% tab title='HR_find-a-word.py' %}

```py
import re

sentence = ' '.join(input() for _ in range(int(input())))
for _ in range(int(input())):
  print(len(re.findall(fr'\b{input()}\b', sentence)))
```

{% endtab %}
{% endtabs %}
