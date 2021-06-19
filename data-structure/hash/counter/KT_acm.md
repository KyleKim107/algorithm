{% tabs %}
{% tab title='KT_acm.md' %}

> Question

* 문제를 풀 때 정답이면 정답인 시간을 더하고,
* 오답이면 그 문제에 대한 penalty가 20분 씩 쌓여 그 문제를 맞았을 때 기존에 쌓인 페널티를 합쳐서 시간을 계산한다
* 시간, 문제, 결과가 입력 될 때 총 시간을 구하라
* -1 이 입력될 까지 계속 된다

```txt
Input:
3 E right
10 A wrong
30 C wrong
50 B wrong
100 A wrong
200 A right
250 C wrong
300 D right
-1

Output: 3 543
```

{% endtab %}
{% tab title='KT_acm.py' %}

```py
from collections import Counter
total_score = total_time = 0
penalty = Counter()
while True:
  st = input()
  if st == '-1':
    break
  t, prob, result = st.split()
  t = int(t)

  if result == 'wrong':
    penalty[prob] += 20
  elif result == 'right':
    total_time += t + penalty[prob]
    total_score += 1

print(total_score, total_time)
```

{% endtab %}
{% endtabs %}
