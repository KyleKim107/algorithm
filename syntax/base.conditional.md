# Conditional

{% tabs %}
{% tab title='java.md' %}

* public int compareTo(Object obj)
  * return 0: if the obj is equal to the other string
  * return < 0: if the obj is less than the other obj
  * return> 0: if the obj is greater than the other obj

{% endtab %}
{% endtabs %}

## If

{% problem 'if' %}

### If elif

{% problem 'if-elif' %}

### If and or

{% problem 'if-and-or' %}

### Min Max

* Supported Languages : python, cpp

* [Absolute value](https://www.youtube.com/watch?v=r6hS_8nm1jM)

{% problem 'min-max' %}

### Abs

{% problem 'abs' %}

## Switch

* Supported Languages : java, cpp
* Use when case value should be small, sorted

{% tabs %}
{% tab title='cpp.md' %}

* create jump table → optimize assembly code

```cpp
// read a, b, c
#include <stdio.h>
int main() {
  char input;
  printf("알파벳 : ");
  scanf("%c", &input);
  switch (input) {
    case 'a':
      printf("에이 \n");
      break;
    case 'b':
      printf("비 \n");
      break;
    default:
      printf("죄송해요.. 머리가 나빠서 못 읽어요  \n");
      break;
  }
  return 0;
}
```

{% endtab %}
{% endtabs %}

{% problem 'switch' %}

## Goto

* Bad practice
* Supported language : cpp

{% tabs %}
{% tab title='cpp.md' %}

```cpp
int n=10;
mylabel:
cout << n << ", ";
n--;
if (n>0) goto mylabel;
```

{% endtab %}
{% endtabs %}

## Exception

{% tabs %}
{% tab title='java.md' %}

* throw
* java.io.IOException : When dealing with I/O in Java

```java
// 1. Catch all excpetion
try {
  //
} catch (Exception e){
  //
}
```

{% endtab %}
{% tab title='python.md' %}

* Builtins exceptions
  * ImportError
  * NotImplementedError
  * ZeroDivisionError

```py
# 1. Catch all exception
test_cases = [(1, 0), ('1', 1), (1, 1)]
for x, y in test_cases:
  try:
    z = x / y
  except ZeroDivisionError as e:
    print(e)
  except:         # Catch all exception
    print(sys.exc_info()[0])
  else:
    print("Successful")

# 2. Raise exception quitely
class StopExecution(Exception):
  def _render_traceback_(self):
  pass

raise StopExecution

# 3. Raise exception on top of current
try:
  from django.core.management import execute_from_command_line
except ImportError as exc:
  raise ImportError("Couldn't import Django. Are you sure it's installed and "
                    "available on your PYTHONPATH environment variable? Did you "
                    "forget to activate a virtual environment?") from exc
```

{% endtab %}
{% tab title='exception.sh' %}

```sh
# 1. Simple try catch
{ # try
    command1 &&
    #save your output

} || { # catch
    # save log for exception
}
```

{% endtab %}
{% endtabs %}

### Try

{% problem 'try' %}
