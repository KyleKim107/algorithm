{% tabs %}
{% tab title='KT_pet.md' %}

> Question

* When each participant is given an evaluation score, find the winner and his score

```txt
Input:
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5

Output: 4 19
```

{% endtab %}
{% tab title='KT_pet.py' %}

```py
num = mx = 0
for i in range(5):
  temp = sum(map(int, input().split()))
  if mx < temp:
    mx = temp
    num = i + 1

print(num, mx)
```

{% endtab %}
{% endtabs %}
