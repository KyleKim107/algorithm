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

{% problem 'function' %}

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

{% problem 'import' %}
