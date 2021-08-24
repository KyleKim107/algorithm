# Graph Theory

## Union Find

{% tabs%}

```txt
6 4
1 4
2 3
2 4
5 6
```

{% endtabs%}

{% tabs%}
{% tab title='Union_Find.java' %}

```java

public class Union_Find {
    public static int[] parent;

    public static int path_compresstion( int x) {
        if (parent[x] != x)
            return parent[x] = path_compresstion(parent[x]);
            // 부모테이블에 저장한다
        return x;
    }


    public static int find_parent(int x) {
        if (parent[x] != x) // 자기 자신이 루트인것을 찾자
            return find_parent(parent[x]);
            //부모테이블에 따로 저장은 안해서 부모테이블에 변화는 없다.
        return x;
    }

    public static void union_parent(int x, int y) {
        x = find_parent(x);
        y = find_parent(y);
        if (x < y)
            parent[y] = x;
        else
            parent[x] = y;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Graph/Union_Find.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(str.nextToken()), E = Integer.parseInt(str.nextToken());
        parent = new int[V + 1];
        for (int i = 1; i < V + 1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < E; i++) {
            str = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(str.nextToken()), y = Integer.parseInt(str.nextToken());
            union_parent(x, y);
        }

        // # 각 원소가 속한 집합 출력하기
        for (int i = 1; i < V + 1; i++) {
            System.out.print(path_compresstion(i) + " ");
        }
        // 출력:1 1 1 1 5 5
        System.out.println();

        // # 부모 테이블 내용 출력하기
        for (int i = 1; i < V + 1; i++) {
            System.out.print(parent[i] + " ");
        }
        System.out.println();
      }
}

```

{% endtab%}
{% tab title='Union_Find.py' %}

```py

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # print('XX' , x , 'parent[x]', parent[x])
        return find_parent(parent, parent[x])
    # print('x' , x , 'parent[x]', parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # 작은것을 parent 노드로 설정, 낮은 노드로 부모 통일해주기 위함.
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기 1을 더해줘 0은 못쓰는 숫자

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

```

{% endtab%}
{% endtabs%}
