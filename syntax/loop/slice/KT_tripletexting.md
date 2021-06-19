{% tabs %}
{% tab title='KT_tripletexting.md' %}

> Question

* Same string are repeated three times and but one of them are wrong
* Print right string

```txt
Input: hellohrllohello
Output: hello
```

{% endtab %}
{% tab title='KT_tripletexting.py' %}

```py
s = input()
chunk = len(s) // 3
a = s[:chunk]
b = s[chunk:chunk * 2]
c = s[chunk * 2:]
if b == c:
  print(b)
else:
  print(a)
```

{% endtab %}
{% endtabs %}
