# Algorithm Theory

## KMP

{% tabs%}
{% tab title='LIS.java' %}

// ababacabacaabacaaba
// abacaaba

```java

public class KMP {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        char[] text = in.readLine().toCharArray();
        char[] pattern = in.readLine().toCharArray();

        int tLength = text.length, pLength = pattern.length;
        // 실패함수 만들기 : KMP의 아이디어를 똑같이 적용, W에서 W를 찾는 듯한 행위를 해서...
        int[] pi = new int[pLength];
        for (int i = 1, j = 0; i < pLength; i++) {
        // i:접미사 포인터(i=1부터 시작: 우리는 실패함수를 만드는게 목적이므로 첫글자 틀리면 0위치로 가야하므로.),
            // j:접두사 포인터
            while (j > 0 && pattern[i] != pattern[j]) {
                j = pi[j - 1];
            }
            if (pattern[i] == pattern[j])
                pi[i] = ++j;
        }
        System.out.println(Arrays.toString(pi));
        int cnt = 0;
        ArrayList<Integer> list = new ArrayList<Integer>();
        // i : 텍스트 포인터 , j: 패턴 포인터
        for (int i = 0, j = 0; i < tLength; ++i) {

            while (j > 0 && text[i] != pattern[j]) {
                j = pi[j - 1];
            }

            if (text[i] == pattern[j]) { // 두 글자 일치
                if (j == pLength - 1) { // j가 패턴의 마지막 인덱스라면
                    cnt++; // 카운트 증가
                    list.add((i + 1) - pLength);
                    j = pi[j];
                } else {
                    j++;
                }
            }
        }

        System.out.println(cnt);
        if (cnt > 0) {
            System.out.println(list);
        }
    }

}

```

{% endtab %}
{% endtabs %}

## LIS

{% tabs%}
{% tab title='LIS.java' %}

```java

  for (int test = 1; test <= TC; test++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            int[] dp = new int[N];
            dp[0] = 1;// 처음엔 무조건 하나가 오기에
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(str.nextToken());
            }
            System.out.println(Arrays.toString(arr) + "\n");
            int maxV = Integer.MIN_VALUE;
            for (int i = 1; i < N; i++) {
                dp[i] = 1;
                for (int j = 0; j < i; j++) {
                    // 이전값이 자신보다 작고, 이전것의 최대 길이의 +1 이 더 긴경우
                    if (arr[j] < arr[i] && dp[j] + 1 > dp[i])
                    // 자신과 앞의 dp값들을 비교하면서 변경시켜준다
                        dp[i] = dp[j] + 1;
                }
                System.out.println(Arrays.toString(dp));
                maxV = Math.max(dp[i], maxV);
            }
            System.out.println("#" + test + " " + maxV);

        }

```

{% endtab%}
{% endtabs%}
