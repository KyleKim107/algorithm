# Stack

> Programers 짝지어 제거하기

{% tabs %}
{% tab title='짝지어 제거하기.md' %}

```txt
//가능한 케이스
baabaa
// 불가능한 케이스
abab

```

{% endtab %}
{% tab title='짝지어 제거하기.md' %}

기본적으로 괄호 짝지어 제거하는것과 같이 스택을 사용한다

```py

def solution(s):
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == i: stack.pop() # 스택이 마지막이 현재 문자와 같으면 짝이 맞으니까 팝
        else: stack.append(i) # 그 외 그택을 넣는다
    if len(stack) == 0: return 1 # 스택이 배워 있다면, 모두 제거한 케이스
    else: return 0 # 아닐경우 실패

```

{% endtab  %}
{% endtabs %}
