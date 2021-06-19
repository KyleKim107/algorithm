{% tabs %}
{% tab title='HR_ip-address-validation.md' %}

> Question

* IPv4 address is A.B.C.D where A, B, C and D are Integers lying between 0 and 255
* IPv6 8 groups of 16 bits each
  * Each group is written as 4 hexadecimal digits and the groups are separated by colons (:)
  * Leading 0 may be omitted

```txt
Input:
3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329

Output:
Neither
IPv4
IPv6
```

{% endtab %}
{% tab title='HR_ip-address-validation.py' %}

```py
import re

number = int(input())
RE_IPV4 = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
RE_IPV6 = r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$'
for n in range(number):
  string = input()
  if re.search(RE_IPV4, string):
    print('IPv4')
  elif re.search(RE_IPV6, string):
    print('IPv6')
  else:
    print('Neither')
```

{% endtab %}
{% endtabs %}
