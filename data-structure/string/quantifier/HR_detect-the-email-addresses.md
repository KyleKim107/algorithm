{% tabs %}
{% tab title='HR_detect-the-email-addresses.md' %}

> Question

* Print all the unique e-mail addresses detected by you, in one line, in lexicographical order, a semi-colon as the delimiter

```txt
Input:
5
HackerRank is more than just a company, hackers@hackerrank.com
    We are a tight group of hackers, bootstrappers, entrepreneurial thinkers and innovators.
    We are building an engaged community of problem solvers.
    Imagine the intelligence and value that a room would hold if it contained hackers/problem solvers from around the world?
    We're building this online.
Hypothesis: Every hacker loves a particular type of challenge presented in a certain set of difficulty.
If we build a large collection of real world challenges in different domains with an engaging interface,
it is going to be incredible! Join us to create history.
Available Positions interviewstreet@hackerrank.com
Product Hacker product@hackerrank.com

Output: hackers@hackerrank.com;interviewstreet@hackerrank.com;product@hackerrank.com
```

{% endtab %}
{% tab title='HR_detect-the-email-addresses.py' %}

```py
import re
N = int(input())
myStr = " ".join([input() for i in range(N)])
print(";".join(sorted(set([i for i in re.findall(r"([\w.]+@[\w.]+\w+)", myStr)]))))
```

{% endtab %}
{% endtabs %}
