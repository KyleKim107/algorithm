# Method

## Printout

> BufferedReader

* Import

  * java.io.BufferedReader

  * java.io.InputStreamReader

* Used with InputStreamReader

  * BufferedReader br new BufferedReader( new InputStreamReader);

* br.read() : It is used for reading a single character.

* br.readLine() : It is used for reading a line of text.

## Sort

* Integer.compare()

{% tabs %}
{% tab title='BOJ10814.md' %}

* In this example you can compare two value (age and name in this case)

```java

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String[][] arr = new String[N][2];

    for (int i = 0; i < N; i++) {
    arr[i][0] = sc.next();
    arr[i][1] = sc.next();
    }

    Arrays.sort(arr, (s1, s2) -> {
    return Integer.compare(Integer.parseInt(s1[0]), Integer.parseInt(s2[0]));
    });

    Arrays.stream(arr).forEach((a) -> System.out.println(a[0] + " " + a[1]));
  }
}

```

{% endtab %}
{% tab title='input.md' %}

```txt
3
21 Junkyu
21 Dohyun
20 Sunyoung

```

{% endtab %}
{% endtabs %}

## get Length of Arrays

{% tabs %}
{% tab title='java.md' %}
> Get input
> object of length

* String

  * String.length()

```java

String.length()

```

{% endtab %}
{% endtabs %}

## Type Conversion

> From String to int

* Integer.parseInt(String)

* subtract number from the string

  * "A"- 64 ==> printout 1

* Convert from lower case to upper case

{% tabs %}
{% tab title='upper.java' %}

```jave
String name = "Kyle";

name = name..toUpperCase();

System.out.println(name)
// KYLE

```

{% endtab %}
{% endtabs%}
