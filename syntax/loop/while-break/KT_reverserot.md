{% tabs %}
{% tab title='KT_reverserot.md' %}

> Question

* 숫자 a, 문자 b가 매 줄마다 주어진다
* 이 때 문자를 뒤집어서 a만큼 회전한 문자를 출력한다. (단 Z → _ → . → A 으로 순환된다)
* last line is 0

```txt
Input:
1 ABCD
3 YO_THERE.
1 .DOT
14 ROAD
9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING
2 STRING_TO_BE_CONVERTED
1 SNQZDRQDUDQ
0

Output:
EDCB
CHUHKWBR.
UPEA
ROAD
PWRAYF_LWNHAXWH.RHPWRAJAX_HMWJHPWRAORQ.
FGVTGXPQEAGDAQVAIPKTVU
REVERSE_ROT
```

{% endtab %}
{% tab title='KT_reverserot.py' %}

```py
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
  raw = input()
  if raw == '0':
    break
  shift, st = raw.split()
  shift = int(shift)
  for ch in reversed(st):
    print(alp[(alp.find(ch) + shift) % len(alp)], end='')
  print()
```

{% endtab %}
{% endtabs %}
