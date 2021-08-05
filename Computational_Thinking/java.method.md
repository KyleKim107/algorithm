# Method

## Permutation

{% tabs %}
{% tab title='Permutation.java' %}

```java

public class Permutation {
    public static void func(int[] arr, int[] used, int depth) {
        if (depth == arr.length) {
            for (int n : arr) {
                System.out.print(n + " ");
            }
            System.out.println();
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            if (used[i] == 0) {
                used[i] = 1;
                arr[depth] = i + 1;
                func(arr, used, depth + 1);
                arr[depth] = 0;
                used[i] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] arr = new int[num];
        int[] used = new int[num];
        func(arr, used, 0);
    }

}

```

{% endtab %}
{% endtabs %}

## Printout

> BufferedReader

* Import

  * java.io.BufferedReader

  * java.io.InputStreamReader

* Used with InputStreamReader

  * BufferedReader br new BufferedReader( new InputStreamReader);

* br.read() : It is used for reading a single character.

* br.readLine() : It is used for reading a line of text.

* Exception:

  * throws IOException

{% tabs%}
{% tab title='BufferedReader.java' %}

```jave

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferedReaderWithProf {

      public static void main(String[] args) throws IOException {

          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

          int N = Integer.parseInt(br.readLine()); // 버퍼는 한번 읽을떄 한줄씩 읽어 버린다

          for (int i = 0; i < N; i++) {
                        grid[i] = br.readLine().replace(" ", "").toCharArray();
                        // 한줄을 읽은 다음 replace로 변경함 그리고 char array에 한글짜씩 넣음
                        System.out.println(Arrays.toString(grid[i]));
                    }

      }
}

```

{% endtab%}
{% endtabs%}

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

{% tabs %}
{% tab title = 'compare.java' %}

```java

 Arrays.sort(student, new Comparator<int[]>() {
                @Override
                public int compare(final int[] entry1, final int[] entry2) {

                    // To sort in descending order revert
                    // the '>' Operator
                    if (entry1[0] < entry2[0]) {
                        return 1;
                    } else {
                        return -1;
                    }
                }

            });
```

{% tab %}
{% tabs %}

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
