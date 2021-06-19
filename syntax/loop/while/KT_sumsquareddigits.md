{% tabs %}
{% tab title='KT_sumsquareddigits.md' %}

> Question

* N-test개의 줄에  k(data set 수),b,n 정수가 주어진다
* k개의 줄에 각 test 번호 k와 SSB(b,n)을 출력하라

```txt
Input:
3
1 10 1234
2 3 98765
3 16 987654321

Output:
1 30
2 19
3 696
```

{% endtab %}
{% tab title='KT_sumsquareddigits.py' %}

```py
n_test = int(input())
def SSD(b, n):
  ret = 0
  while n != 0:
    ret += (n % b) ** 2
    n //= b
  return ret
for _ in range(1, n_test + 1):
  K, b, n = map(int, input().split())
  print(f'{K} {SSD(b, n)}')
```

{% endtab %}
{% endtabs %}
