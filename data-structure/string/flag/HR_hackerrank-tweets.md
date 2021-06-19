{% tabs %}
{% tab title='HR_hackerrank-tweets.md' %}

> Question

* Print the total number of tweets that has hackerrank (case insensitive) in it

```txt
Input:
4
I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
interesting talk by hari, co-founder of hackerrank

Output: 4
```

{% endtab %}
{% tab title='HR_hackerrank-tweets.js' %}

```js
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
  console.log(input.match(/hackerrank/ig).length);
});
```

{% endtab %}
{% tab title='HR_hackerrank-tweets.py' %}

```py
import re
input_ = ' '.join([input() for _ in range(int(input()))])
print(len(re.findall(r'hackerrank', input_, re.IGNORECASE)))
# print(sum('HACKERRANK' in input().upper() for i in range(int(input()))))
```

{% endtab %}
{% endtabs %}
