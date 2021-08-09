# Method

## PowerSet

* 부분수열의 모든 경우를 고려한다

{% tabs %}
{% tab title='SW5215.java' %}

평소 햄버거를 좋아하던 민기는 최근 부쩍 늘어난 살 때문에 걱정이 많다.

그렇다고 햄버거를 포기할 수 없었던 민기는 햄버거의 맛은 최대한 유지하면서 정해진 칼로리를 넘지 않는 햄버거를 주문하여 먹으려고 한다.

민기가 주로 이용하는 햄버거 가게에서는 고객이 원하는 조합으로 햄버거를 만들어서 준다.

하지만 재료는 미리 만들어서 준비해놓기 때문에 조합에 들어가는 재료를 잘라서 조합해주지는 않고, 재료를 선택하면 준비해놓은 재료를 그대로 사용하여 조합해준다.

민기는 이 가게에서 자신이 먹었던 햄버거의 재료에 대한 맛을 자신의 오랜 경험을 통해 점수를 매겨놓았다.

민기의 햄버거 재료에 대한 점수와 가게에서 제공하는 재료에 대한 칼로리가 주어졌을 때,

민기가 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서 민기가 가장 선호하는 햄버거를 조합해주는 프로그램을 만들어보자.

```java


    public static int satisfy = 0;
    public static int total, hamNum;
    public static int[][] arr;

    public static void func(int numEle , int totalSatisfaction , int totalCal ){
        if(totalCal > total){
            return;
        }
        if(numEle == hamNum){
            satisfy = Math.max(totalSatisfaction ,satisfy );
            return;
        }
        func(numEle +1 , totalSatisfaction + arr[numEle][0] , totalCal + arr[numEle][1] ); // 고르고
        func(numEle +1 , totalSatisfaction  , totalCal ); // 안고르고
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt( br.readLine());
                StringTokenizer str = null;

        for(int test_case = 1; test_case <= TC; test_case++)
        {
            satisfy = 0;
             str = new StringTokenizer(br.readLine()) ;
            hamNum = Integer.parseInt(str.nextToken());
            total = Integer.parseInt(str.nextToken());
            arr = new int[hamNum][2];
            int[] visit = new int[hamNum];
            for(int i = 0 ; i < hamNum ; i++){
                str = new StringTokenizer(br.readLine()) ;
                    arr[i][0]=  Integer.parseInt(str.nextToken());
                    arr[i][1]= Integer.parseInt(str.nextToken());
            }
            func( 0,0,0);
            System.out.printf("#%d %d\n" ,test_case, satisfy);
        }
    }

```

{% endtab %}
{% endtabs %}

* 부분수열의 특정 경우만 고려하는 경우

{% tabs %}
{% tab title='SW9229.java' %}

```java


import java.util.*;
import java.io.*;

public class SW9229 {
    public static int max;
    public static int[]  arr;
    public static int  maxV = -1;

    public static void func(  int currWeight , int depth,  int r){
        if (currWeight > max){return;}
        if(r == 0){
            maxV = Math.max(maxV ,currWeight );
            return;
        }
        if(depth == arr.length){return;}

        func(  currWeight + arr[depth] , depth+1 ,   r -1);
        func(  currWeight , depth+1 ,   r);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt( br.readLine());
        StringTokenizer str = null;
        for(int test_case = 1; test_case <= TC; test_case++){
            str = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(str.nextToken());
            max = Integer.parseInt(str.nextToken());
            str = new StringTokenizer(br.readLine());
            arr = new int[len];
            for(int i = 0 ; i < len ; i++){
                arr[i] = Integer.parseInt(str.nextToken());
            }
            maxV = -1;
            func(  0 , 0 ,   2);
            System.out.println("#" + test_case + " "+maxV);
        }
    }

}


```

{% endtab %}
{% endtabs %}

## Combination

{% tabs %}
{% tab title='Permutatoin.java' %}

```java

 // 재귀 사용
        // 사용 예시 : comb(arr, visited, 0, n, r)
        static void comb(int[] arr, boolean[] visited, int depth, int n, int r) {
            if (r == 0) {
                print(arr, visited, n);
                return;
            }
            if (depth == n) {
                return;
            }

            visited[depth] = true; // visit에 표시해서 선택한다
            comb(arr, visited, depth + 1, n, r - 1); // depth가 하나씩 더해지면서 인덱스를 높인다
                                                // r로 선택하고 선택 안하고를 결정
            visited[depth] = false;
            comb(arr, visited, depth + 1, n, r);
        }

public class Combination {
    public static void main(String[] args) {
        int n = 4;
        int[] arr = {1, 2, 3, 4};
        boolean[] visited = new boolean[n];

        for (int i = 1; i <= n; i++) {
            System.out.println("\n" + n + " 개 중에서 " + i + " 개 뽑기");
            comb(arr, visited, 0, n, i);
        }

    }

    // 배열 출력
    static void print(int[] arr, boolean[] visited, int n) {
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}

```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title='Permutatoin.java' %}

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
