# Syntax

{% tabs %}
{% tab title='javscript.md' %}

* All JavaScript values, except primitives, are objects
* Don’t Declare Number, String, Boolean Objects → slows down execution speed
* typeof() returns data types
* Objects are mutable: They are addressed by reference, not by value

```js
// 1. Loosely typed
var x = 5 + "7";    // x.valueOf() is 57,  typeof x is a string
var x = "5" + 7;    // x.valueOf() is 57,  typeof x is a string
var x = 5 - "x";    // x.valueOf() is NaN, typeof x is a number
```

{% endtab %}
{% endtabs %}

## Comment

{% tabs %}
{% tab title='cpp.md' %}

```cpp
// 1. single line
/*
2.
multi
line
*/
```

{% endtab %}
{% tab title='python.md' %}

```py
# 1. single line comment
"""
2. multiline comment
"""
```

{% endtab %}
{% endtabs %}

## Const

{% tabs %}
{% tab title='const.cpp' %}

* compile time constraint / self documenting, compile optimization, can put in ROM (embedded)
* cannot modify anything that exists outside of the const function
* const applies to the thing left of it. If there is nothing on the left then it applies to the right of it
* pointers / references to that data must be as restrictive of how they allow data to be changed

> constexpr

* can be used unless goto / try (after C++ 20) / uninitialized, non-literal variable / non constexpr function
* if constexpr should be boolean (true → else won’t compile, vice versa)
* rhs of constexpr must be number

```cpp
#include <iostream>
using namespace std;
struct X {
  X& ref() { return *this; }
};

// 1. Const examples
const int * p = &f;           // data is const, pointer is not
int * const p = &f;           // data is not, pointer is const
const int * const p = &f;     // data is const, pointer is const
const int i = 9;
const_cast<int&>(i) = 6;      // cast away const
int j;
static_cast<const int &>(j) = 7; // set data into const
void setName(const string& name) // const parameters
const string& getName() {}       // const return value
void getName() const {}     // cannot change member variable (only call const function)
void getName() {}           // non const object call this function

// 2. constexpr
// Error
int a;
constexpr int b = a;

// constexpr function
constexpr int Factorial(int n) {
  int total = 1;
  for (int i = 1; i <= n; i++)
    total *= i;
  return total;
}

// can be used in template
template <int N>
struct A {
  int operator()() { return N; }
};

int main() {
  constexpr int size = 3;
  int arr[size];
  constexpr int N = 10;
  A<N> a;
  cout << a() << std::endl;        # 10
  constexpr int number = 3;
  enum B { x = number, y, z };
  cout << B::x << std::endl;        # 3
}

// 3. Const Errors
// non-const lvalue reference to type 'X'
// -> X().ref()
X& x = X();

int a = 5;
// error: const' qualifier may not be applied to a reference
// int &const ref1 = a;

const int &ref2 = a;  // valid
// error: cannot assign to variable 'ref2' with const-qualified type 'const int &'
// -> const cannot be modified
// ref2 = 7;

const int b = 6;
// error: binding reference of type 'int' to value of type 'const int' drops 'const' qualifier
// -> cannot create non const pointed by  const pointer
// int &ref = b;

int c = 1, e = 2;
int const *d = &c;
d = &e;
// error: read-only variable is not assignable
// -> cannot modify const pointed int
// *d = 3;
cout << *d;

int const f = 5;
int *ptr = (int *)&f;
*ptr = 10;
cout << f;  // depends on compiler
```

{% endtab %}
{% tab title='' %}

```py
from typing import Final

VERSION: Final = "1.0.0"
```

{% endtab %}
{% endtabs %}

## Enum

* Used when representing fixed set of constants. less error-prone than string, with IDE Support

{% tabs %}
{% tab title='cpp.md' %}

```cpp
// 1. enum class
enum Color { red, green, blue };
enum class CarColor { red, blue, black };         // strongly typed enum can share variable name

enum class BattleCondition { red, yellow, green };
auto currentLight = BattleCondition::green;
const auto shieldLevel = [&]() {  // reference scoping
  switch (currentLight) {
    case BattleCondition::green:
      return 30;
    case BattleCondition::yellow:
      return 50;
    case BattleCondition::red:
    default:
      return 100;
  }
}();

std::cout << "current shield " << shieldLevel << std::endl;
```

{% endtab %}
{% tab title='enum.java' %}

```java
// 1. Simple enum
public enum Day {
  SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}

// 2. Enum class
public enum Planet {
  MERCURY (3.303e+23, 2.4397e6),
  VENUS   (4.869e+24, 6.0518e6),
  EARTH   (5.976e+24, 6.37814e6),
  MARS    (6.421e+23, 3.3972e6),
  JUPITER (1.9e+27,   7.1492e7),
  SATURN  (5.688e+26, 6.0268e7),
  URANUS  (8.686e+25, 2.5559e7),
  NEPTUNE (1.024e+26, 2.4746e7);

  private final double mass;   // in kilograms
  private final double radius; // in meters
  Planet(double mass, double radius) {
    this.mass = mass;
    this.radius = radius;
  }
  private double mass() { return mass; }
  private double radius() { return radius; }

  // universal gravitational constant  (m3 kg-1 s-2)
  public static final double G = 6.67300E-11;

  double surfaceGravity() {
    return G * mass / (radius * radius);
  }
  double surfaceWeight(double otherMass) {
    return otherMass * surfaceGravity();
  }
  public static void main(String[] args) {
    if (args.length != 1) {
      System.err.println("Usage: java Planet <earth_weight>");
      System.exit(-1);
    }
    double earthWeight = Double.parseDouble(args[0]);
    double mass = earthWeight/EARTH.surfaceGravity();
    for (Planet p : Planet.values())
      System.out.printf("Your weight on %s is %f%n", p, p.surfaceWeight(mass));
  }
}
```

{% endtab %}
{% tab title='python.md' %}

```py
from enum import Enum

class Shape(Enum):
  BIG = 1
  MEDIUM = 2
  SMALL = 3

class Animal:
  SHAPE = Shape

class Lion(Animal):
  def introduce(self):
    return self.SHAPE
lion = Lion()
print(lion.introduce())
```

{% endtab %}
{% endtabs %}

## Type

{% tabs %}
{% tab title='cpp.md' %}

* typeinfo
* type_traits

```cpp
#include <iostream>
#include <typeinfo>

using namespace std;

// 1. sizeof
cout << sizeof(bool) << endl;        // 1
cout << typeid(true).name() << endl; // b

cout << sizeof(char) << endl;        // 1
cout << typeid('a').name() << endl;  // c

cout << sizeof(int) << endl;       // 4
cout << typeid(1).name() << endl;  // i

cout << sizeof(float) << endl;       // 4
cout << typeid(1.5f).name() << endl; // f

cout << sizeof(long) << endl;       // 8
cout << typeid(1l).name() << endl;  // l

cout << sizeof(long long) << endl;   // 8
cout << typeid(1ll).name() << endl;  // x

cout << sizeof(double) << endl;      // 8
cout << typeid(1.5).name() << endl;  // d

cout << sizeof(long double) << endl; // 16

bool *p_bool;
cout << sizeof(p_bool) << endl;  // 8

float a = 3.5;
int b = static_cast<int>(a);
b = 3;
const volatile int *bp = &b;
cout << "bp " << typeid(bp).name() << endl;  // bp PVKi
int *cp = const_cast<int *>(bp);
*cp = 'A';
cout << "cp " << typeid(cp).name() << endl;  // cp Pi

#include <iostream>
#include <type_traits>

using namespace std;

// 2. show type
template <typename T>
void show_value(T t) {
  if constexpr (is_pointer<T>::value) { // std::is_pointer_t<T>
    cout << "Pointer " << *t << endl;
  } else {
    cout << "Not Pointer " << t << endl;
  }
}

int x = 3;
show_value(x);

int *p = &x;
show_value(p);
```

{% endtab %}
{% tab title='javascript.md' %}

* // @ts-nocheck : file level ignore on top of the file
* // @ts-ignore : single line next to line

{% endtab %}
{% endtabs %}

## Number

{% tabs %}
{% tab title='cpp.md' %}

> size_t

* basic unsigned integer → depends on system
* improve code's portability and efficiency → indexing containers should use

> long

* 0LL for constant
* right shift checks whether the data is signed or not

{% tabs %}
{% tab title='java.md' %}

* automatic cast
  * ex : float → double / byte → short → int → long

```java
// 1. int to byte array
public static void bytesFromInt(byte[] array, int offset, int value) {
  array[offset + 0] = (byte) ((value >> 0) & 0xFF);
  array[offset + 1] = (byte) ((value >> 8) & 0xFF);
  array[offset + 2] = (byte) ((value >> 16) & 0xFF);
  array[offset + 3] = (byte) ((value >> 24) & 0xFF);
}
```

{% endtab %}
{% tab title='javascript.md' %}

> Number

* EPSILON
* MAX_SAFE_INTEGER
* MAX_VALUE
* MIN_SAFE_INTEGER
* MIN_VALUE          // the smallest positive numeric value
* NEGATIVE_INFINITY
* NaN
* POSITIVE_INFINITY
* prototype

* isFinite()
* isInteger()
* isNaN()
* isSafeInteger()
* parseFloat()
* parseInt((radix))
* toString((radix))
* Number((6.688689).toFixed(1));  // 6.7

{% endtab %}
{% endtabs %}

### Char

{% tabs %}
{% tab title='cpp.md' %}

> Char

* isdigit / isalpha / isalnum(‘1’)
* islower(‘A’)
* scanf("%c", &c);

{% endtab %}
{% endtabs %}

## Function

* Pure Function : Don't attempt to change inputs, same outputs for same input
* Impure function: modify contents of argument

{% tabs %}
{% tab title='javascript.md' %}

* function is called with a missing argument, the value of the missing argument is set to undefined

```js
// 1. Impure function Example
function withdraw(account, amount) {
  account.total -= amount;
}

// 2. map 6 returns new object
var elements = ['Hydrogen', 'Helium', 'Lithium',];
elements.map(function(element) {  return element.length;});        // [8, 6, 7]
elements.map((element) => {  return element.length;});
elements.map(element => element.length);
```

{% endtab %}
{% endtabs %}

> baekjoon

* [Level 4 : 싱기한 네자리 숫자](http://acmicpc.net/problem/6679)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/function/BJ_6679.md)

{% tabs %}
{% tab title='BJ_6679.md' %}

> Question

* Find all number from [1000, 9999] such that
* numbers represented by decimal, twelfth, and sixteenth digits
* for each number, when the digits of each number are added, all three values ​​should be the same

```txt
Output:
2992
...
```

{% endtab %}
{% tab title='BJ_6679.py' %}

```py
def sum_digit(dec, n):
  ret = 0
  while n != 0:
    ret += n % dec
    n //= dec
  return ret

for n in range(1000, 10000):
  if sum_digit(10, n) == sum_digit(12, n) == sum_digit(16, n):
    print(n)
```

{% endtab %}
{% endtabs %}

* [Level 4 : 트로피 진열](http://acmicpc.net/problem/1668)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/function/BJ_1668.md)

{% tabs %}
{% tab title='BJ_1668.md' %}

> Question

* Outputs the number of views on the left side of the first line and the number on the right side of the second line

```txt
Input:
5
1
2
3
4
5

Output:
5
1
```

{% endtab %}
{% tab title='BJ_1668.py' %}

```py
def count_visible(li):
  count, cur_mx = 0, 0
  for e in li:
    if e > cur_mx:
      count += 1
      cur_mx = e
  return count
li=[int(input()) for _ in range(int(input()))]
print(count_visible(li))
print(count_visible(reversed(li)))
```

{% endtab %}
{% endtabs %}

* [Level 4 : 정수 N개의 합](http://acmicpc.net/problem/15596)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/function/BJ_15596.md)

{% tabs %}
{% tab title='BJ_15596.md' %}

> Question

* Write function to return sum

```txt
def solve(a: list) -> int:
  # TODO
```

{% endtab %}
{% tab title='BJ_15596.py' %}

```py
def solve(a):
  return sum(a)
```

{% endtab %}
{% endtabs %}

* [Level 5 : 뒤집힌 덧셈](http://acmicpc.net/problem/1357)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/function/BJ_1357.md)

{% tabs %}
{% tab title='BJ_1357.md' %}

> Question

* find rev(rev(a) + rev(b))

```txt
Input: 123 100
Output: 223
```

{% endtab %}
{% tab titlepyJ_1357.md'' %}

```py
a, b = map(int, input().split())
def rev(a):
  return int("".join(reversed(str(a))))
print(rev(rev(a) + rev(b)))
```

{% endtab %}
{% endtabs %}

* [Level 6 : 셀프 넘버](http://acmicpc.net/problem/4673)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/function/BJ_4673.md)

{% tabs %}
{% tab title='BJ_4673.md' %}

> Question

* For positive integer n, define d(n) as a function that adds each digit of n and n, for example, d(75) = 75+7+5 = 87
* Find all self number below 10000

```txt
Output:
1
3
5
7
9
20
31
42
53
64
 |
 |       <-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
```

{% endtab %}
{% tab title='BJ_4673.py' %}

```py
li = [True] * 10090
def d(n):
  ret = n
  while n:
    ret += n % 10
    n //= 10
  return ret

for n in range(10000):
  li[d(n)] = False

for i in range(10001):
  if li[i]:
    print(i)
n = int(input())
```

{% endtab %}
{% endtabs %}

### Lambda

{% tabs %}
{% tab title='cpp.md' %}

![lambda](images/20210304_231730.png)

* capture clause / lambda-introducer
* parameter list / lambda declarator Optional
* mutable specification Optional
* exception-specification Optional
* trailing-return-type Optional
* lambda body
  * [&] : captured by reference
  * [=] : captured by value

```cpp
// If capture clause includes capture-default &, then no identifier can have the form & identifier
struct S { void f(int i); };
void S::f(int i) {
  [&, i]{};          // OK
  [&, &i]{};         // ERROR: i preceded by & when & is the default
  [=, this]{};       // ERROR: this when = is the default
  [=, *this]{ };     // OK: captures this by value. See below.
  [i, i]{};          // ERROR: i repeated
}

// returns same result for same argument values and it has no side effects like modifying an argument
g = lambda x: x*x*x    // print(g(7))

vector<int> vecVals = GenerateRandVec(10, 1, 50);
int x = 1;
auto valueLambda = [=]() { cout << x << endl; };
auto refLambda = [&]() { cout << x << endl; };

x = 13;

valueLambda();     // 1
refLambda();       // 13

// lambda function
#include <iostream>
using namespace std;

int main() {
  auto change = [&](int &num, int to) { num = to; };
  auto change_2 = [&](int &num) { change(num, 2); };
  int a = 1;
  change_2(a);
  cout << a << endl;
}
```

{% endtab %}
{% tab title='java.md' %}

* in Java 8

```java
// 1. Print using lambda
(p1, p2) -> System.out.println("Multiple parameters: " + p1 + ", " + p2);
ArrayList<Integer> arrL = new ArrayList<Integer>({1, 2, 3, 4});
arrL.forEach(n -> System.out.println(n));
arrL.forEach(n -> { if (n%2 == 0) System.out.println(n); });
```

{% endtab %}
{% tab title='javascript.md' %}

```js
hello = () => "Hello World!";   // works if only has one statement
```

{% endtab %}
{% endtabs %}

### Closure

* the function we return still has access to the internal scope of the function that returned it

{% tabs %}
{% tab title='javascript.md' %}

```js
// 1. Basic tag closure
function html_tag(tag) {
  function wrap_text(msg) {
    console.log('<' + tag + '>' + msg + '</' + tag + '>')
  }
  return wrap_text
}

print_h1 = html_tag(‘h1’)
print_h1(‘sean’)

// 2. Private variable using closure
var makeCounter = function() {
  var privateCounter = 0;
  function changeBy(val) { privateCounter += val; }
  return {
    increment: function() { changeBy(1); },
    decrement: function() { changeBy(-1); },
    value: function() { return privateCounter; }
  }
};

var counter1 = makeCounter();
var counter2 = makeCounter();

alert(counter1.value());  // 0.

counter1.increment();
counter1.increment();
alert(counter1.value()); // 2.

counter1.decrement();
alert(counter1.value()); // 1.
alert(counter2.value()); // 0.
```

{% endtab %}
{% tab title='python.md' %}

* Python’s closures are late binding

```py
# 1. Closure
def outer_func(msg):
  def inner_func():
    print('Hi' + msg)
  return inner_func()

my_func = outer_func(‘Sean’)
my_func()  # Hi Sean

# 2. Late binding
def create_multipliers():
  return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
  print(multiplier(2), end=" ")    # 8 8 8 8 8

def create_multipliers():
  return [lambda x, i = i : i * x for i in range(5)]  # Solution
```

{% endtab %}
{% endtabs %}

## Import

> baekjoon

* [Level 3 : 경기 결과](http://acmicpc.net/problem/5523)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_5523.md)

{% tabs %}
{% tab title='BJ_5523.md' %}

> Question

* Given the scores of A and B in N rounds
* prints the number of times A has won, and the number of times B has won

```txt
Input:
4
100 0
5 6
40 50
74 75

Output: 1 3
```

{% endtab %}
{% tab title='BJ_5523.py' %}

```py
import sys
input = sys.stdin.readline
N = int(input())
li = []
a_win, b_win = 0, 0
for _ in range(N):
  a, b = map(int, input().split())
  if a > b:
    a_win += 1
  elif b > a:
    b_win += 1

print(a_win, b_win)
```

{% endtab %}
{% endtabs %}

* [Level 3 : 창용이의 시계](http://acmicpc.net/problem/12840)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_12840.md)

{% tabs %}
{% tab title='BJ_12840.md' %}

> Question

* When T is 1, take C as input and turn the clock forward for C seconds
* When T is 2, take C as input and turn the clock back for C seconds
* When T is 3, the situation of the clock operated by Changyong is printed

```txt
Input:
0 1 0
4
1 4263
3
2 1175
3

Output:
1 12 3
0 52 28
```

{% endtab %}
{% tab title='BJ_12840.py' %}

```py
import sys
input = sys.stdin.readline
h, m, s = map(int, input().split())
s += (h * 3600 + m * 60)

for i in range(int(input())):
  l = list(map(int, input().split()))
  if len(l) == 2:
    q, c = l
  else:
    q, c = l, 0

  if q == 1:
    s += c
  elif q == 2:
    s -= c
  else:
    print(s // 3600 % 24, (s % 3600) // 60, s % 60)
```

{% endtab %}
{% endtabs %}

* [Level 3 : 그대로 출력하기](http://acmicpc.net/problem/11718)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_11718.md)

{% tabs %}
{% tab title='BJ_11718.md' %}

> Question

* Print as input

```txt
Input:
Hello
Baekjoon
Online Judge

Output:
Hello
Baekjoon
Online Judge
```

{% endtab %}
{% tab title='BJ_11718.cpp' %}

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
  string str;
  while (getline(cin, str)){
    cout << str << endl;
  }
  return 0;
}
```

{% endtab %}
{% tab title='BJ_11718.sh' %}

```sh
while read a
do
  echo "$a"
done
```

{% endtab %}
{% tab title='BJ_11718.py' %}

```py
import sys
print(sys.stdin.read())
```

{% endtab %}
{% endtabs %}

* [Level 3 : 부호](http://acmicpc.net/problem/1247)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_1247.md)

{% tabs %}
{% tab title='BJ_1247.md' %}

> Question

* Given N integers, find the sign of these summed integers

```txt
Input:
3
0
0
0
10
1
2
4
8
16
32
64
128
256
-512
6
9223372036854775807
9223372036854775806
9223372036854775805
-9223372036854775807
-9223372036854775806
-9223372036854775804

Output:
0
-
+
```

{% endtab %}
{% tab title='BJ_1247.py' %}

```py
import sys
for _ in range(3):
  N = int(input())
  li = [int(sys.stdin.readline()) for _ in range(N)]
  total = sum(li)
  if total > 0:
    print('+')
  elif total < 0:
    print('-')
  else:
    print(0)
```

{% endtab %}
{% endtabs %}

* [Level 4 : 줄 세기](http://acmicpc.net/problem/4806)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_4806.md)

{% tabs %}
{% tab title='BJ_4806.md' %}

> Question

* Count number of line

```txt
Input:
one
and two
three

Output: 3
```

{% endtab %}
{% tab title='BJ_4806.py' %}

```py
import sys
print(sys.stdin.read().count("\n"))
```

{% endtab %}
{% endtabs %}

* [Level 4 : 빠른 A+B](http://acmicpc.net/problem/15552)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_15552.md)

{% tabs %}
{% tab title='BJ_15552.md' %}

> Question

* Print a + b for each line

```txt
Input:
5
1 1
12 34
5 500
40 60
1000 1000

Output:
2
46
505
100
2000
```

{% endtab %}
{% tab title='BJ_15552.cpp' %}

```cpp
#include <iostream>
using namespace std;
int main() {
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  while (T--) {
    int A, B;
    cin >> A >> B;
    cout << A + B << '\n';
  }
}
```

{% endtab %}
{% tab title='BJ_15552.py' %}

```py
import sys
input = sys.stdin.readline
n_test = int(input())
for _ in range(n_test):
  a, b = map(int, input().split())
  print(a + b)
```

{% endtab %}
{% endtabs %}

* [Level 5 : 그대로 출력하기 2](http://acmicpc.net/problem/11719)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_11719.md)

{% tabs %}
{% tab title='BJ_11719.md' %}

> Question

* Print all input

```txt
Input:
    Hello

Baekjoon
   Online Judge

Output:
    Hello

Baekjoon
   Online Judge
```

{% endtab %}
{% tab title='BJ_11719.cpp' %}

```cpp
#include <iostream>
int main() {
  char c;
  while ((c = std::cin.get()) != -1) {
    std::cout << c;
  }
}
```

{% endtab %}
{% tab title='BJ_11719.py' %}

```py
import sys
print(sys.stdin.read())
```

{% endtab %}
{% endtabs %}

* [Level 6 : 집합](http://acmicpc.net/problem/11723)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_11723.md)

{% tabs %}
{% tab title='BJ_11723.md' %}

> Question

* When an empty set of balls S is given, write a program that performs the operation below
  * add x: Add x to S.  If S already has x, ignore the operation
  * remove x: remove x from S  If S does not have x, ignore the operation
  * check x: print 1 if S has x and 0 if not
  * toggle x: If S has x, remove x; if not, add x
  * all: Change S to {1, 2, ..., 20}
  * empty: Replace S with a covalent set

```txt
Input:
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

Output:
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
```

{% endtab %}
{% tab title='BJ_11723.py' %}

```py
import sys
input = sys.stdin.readline
M = int(input())
my_list = [False] * 20  # 0 ~ 19
for _ in range(M):
  c = input().split()
  if len(c) > 1:
    n = int(c[1]) - 1  # 1 ~ 20 -> 0 ~ 19
  if c[0] == 'add':
    my_list[n] = True
  elif c[0] == 'remove':
    my_list[n] = False
  elif c[0] == 'check':
    print(1 if my_list[n] else 0)
  elif c[0] == 'toggle':
    my_list[n] = not my_list[n]
  elif c[0] == 'all':
    my_list = [True] * 20
  elif c[0] == 'empty':
    my_list = [False] * 20
```

{% endtab %}
{% endtabs %}

* [Level 6 : 수 정렬하기 5](http://acmicpc.net/problem/15688)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_15688.md)

{% tabs %}
{% tab title='BJ_15688.md' %}

> Question

* When given N numbers, sort them in descending order

```txt
Input:
5
5
4
3
2
1

Output:
1
2
3
4
5
```

{% endtab %}
{% tab title='BJ_15688.py' %}

```py
import sys
l = []
for _ in range(int(sys.stdin.readline())):
  l.append(int(sys.stdin.readline()))
print("\n".join(map(str, sorted(l))))
```

{% endtab %}
{% endtabs %}

* [Level 6 : 수 정렬하기 4](http://acmicpc.net/problem/11931)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_11931.md)

{% tabs %}
{% tab title='BJ_11931.md' %}

> Question

* Print list in reversed order

```txt
Input:
5
1
2
3
4
5

Output:
5
4
3
2
1
```

{% endtab %}
{% tab title='BJ_11931.py' %}

```py
import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
for e in sorted(li, reverse=True):
  print(e)
```

{% endtab %}
{% endtabs %}

* [Level 8 : 1](http://acmicpc.net/problem/4375)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_4375.md)

{% tabs %}
{% tab title='BJ_4375.md' %}

> Question

* 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때
* Find multiple of n that consists of only 1

```txt
Input:
3
7
9901

Output:
3
6
12
```

{% endtab %}
{% tab title='BJ_4375.py' %}

```py
import sys
for line in sys.stdin:
  st = '1'
  while True:
    if int(st) % int(line) == 0:
      print(len(st))
      break
    st += '1'
```

{% endtab %}
{% endtabs %}

* [Level 15 : 이항 계수와 쿼리](http://acmicpc.net/problem/13977)
  * [Update solution](https://github.com/seanhwangg/algorithm/edit/main/syntax/syntax/import/BJ_13977.md)

{% tabs %}
{% tab title='BJ_13977.md' %}

> Question

* Given list of N, K print N choose K mod 1,000,000,007

```txt
Input:
5
5 2
5 3
10 5
20 10
10 0

Output:
10
10
252
184756
1
```

{% endtab %}
{% tab title='BJ_13977.py' %}

```py
from sys import stdin
input = stdin.readline

MOD = 1000000007
fac = [1]
for i in range(1,4000001):
  fac.append((fac[-1]*i)%MOD)
for i in range(int(input())):
  n, k = map(int,input().split())
  f = fac[n]
  f = (f * pow(fac[k], MOD-2, MOD)) % MOD
  f = (f * pow(fac[n-k], MOD-2, MOD)) % MOD
  print(f)
```

{% endtab %}
{% endtabs %}
