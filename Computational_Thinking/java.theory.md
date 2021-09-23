# Algorithm Theory

## MST

{% tabs%}

- 시작점과 끝점을 우선순위큐나 ArrayList에 담고 소트로 cost가 적은 오름차순으로 정렬해줍니다

- 큐를 하나씩 꺼내주며 시작점과 끝점의 부모를 찾은후 부모가 같다면 Cycle이기에 무시해줍니다.

- 부모가 다르다면 두 점을 서로 연결해주고 값을 더해줍니다.

{% tab title='MST.java' %}

```java

public class SW3124 {
    public static int[] arr;

    static int find(int x) {
        if (arr[x] != x) {
            return arr[x] = find(arr[x]);
        }
        return x;
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if ( x > y) {
            arr[x] = y;
        } else {
            arr[y] = x;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= TC; test_case++) {

            StringTokenizer str = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(str.nextToken()), E = Integer.parseInt(str.nextToken());
            arr = new int[V + 1];
            for (int i = 1; i < V + 1; i++) {
                arr[i] = i;
            }
            PriorityQueue<Node> PQ = new PriorityQueue<Node>();
            for (int i = 0; i < E; i++) {
                str = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(str.nextToken());
                int end = Integer.parseInt(str.nextToken());
                int value = Integer.parseInt(str.nextToken());
                PQ.offer(new Node(start, end, value));
            }

            long answer = 0;
            for (int i = 0; i < PQ.size(); i++) {
                Node tmp = PQ.poll();
                int start = tmp.start, end = tmp.end, value = tmp.value;
                if (find(start) == find(end))
                    continue;
                union(start, end);
                answer += value;
            }
            System.out.println("#" + test_case + " " + answer);
        }
    }

    static class Node implements Comparable<Node> {
        int value, end, start;

        public Node(int start, int end, int value) {
            super();
            this.value = value;
            this.end = end;
            this.start = start;
        }

        @Override
        public int compareTo(Node a) { // compareTo는 상대꺼만, compare은 둘다
            return Integer.compare(this.value , a.value);
        }
    }

}

```

{% endtab %}
{% endtabs %}

## KMP

{% tabs%}
{% tab title='input.txt' %}

input

```txt

ababacabacaabacaaba
abacaaba

```

{% endtab %}
{% tab title='KMP.java' %}

- 불일치가 발생한 텍스트 문자열의 앞부분에 어떤 문자가 있는지 미리 알고 있기 때문에 불일치가 발생한 앞부분에 대해서 다시 비교하지 않으면서 매칭이 일어나는지 판단할 수 있는 알고리즘입니다.

j 위치의 문자열과 i 위치의 문자열이 일치하지 않을 경우:

- 접두사와 접미사가 일치하지 않는다는 것이므로 다시 검사를 해야하는데 이때 아예 처음으로 돌아갈 수도 있으나 비효율적입니다.

- 그래서 여태까지 일치했던 곳에서부터 다시 검사를 하는 것이 유리합니다. 따라서 pi배열을 참고하여 j의 위치를 pi[j - 1]에서 가리키는 위치로 이동시켜봅니다.

- j - 1인 이유는 최소 j - 1 위치까지는 접두사와 접미사가 일치했다는 것이므로 이동을 최소화할 수 있기 때문입니다. 이동을 시킨 후 다시 일치하는지 검사를 합니다.

TIME COMPLEXITY: O(word + pattern)

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
