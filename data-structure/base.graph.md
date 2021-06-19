# Graph

* [Graph](https://docs.google.com/forms/d/1E8HkTLzD7yVQ3Vqr9RhAYax10HYzW8S8tRadvmUaZbo/edit)

> Terms

* Directed
  * DAGs : Directed acyclic graphs are directed graphs with no cycle
  * Weakly : Undirected version of directed graph is connected
  * Strongly Connected : Directed graph G is strongly connected a path exists for all ordered pair vertices
  * Strongly Connected Component : Strongly connected components is maximal strongly connected piece
  * Connectivity Deficit : minimum number of directed edges you have to add to make graph strongly connected

* Undirected
  * Connected : G is connected if for any pair of vertices v, w there is a path from v to w
  * CC : Connected components is maximal connected piece

![Edge](images/20210206_211500.png)

* Edge
  * Tree : solid edge included in the DFS output tree (pre u < pre v < post v < post u)
  * Back : leads to an ancestor (pre v < pre u < post u < post v)
  * Cross : leads to neither anc. or des (pre v < post v < pre u < post(u)

* Adjacent (coincident)
  * Two edges of a graph are called adjacent if they share a common vertex
  * Two vertices are called adjacent if they share a common edge

* incident : An edge and a vertex on that edge

* Path
  * Walk : Vertices may repeat. Edges may repeat (Closed or Open)
  * Trail : Vertices may repeat. Edges cannot repeat (Open)
  * Circuit : Vertices may repeat. Edges cannot repeat (Closed)
  * Path : Vertices cannot repeat. Edges cannot repeat (Open)
  * Cycle : Vertices cannot repeat. Edges cannot repeat (Closed)
  * Hamiltonian : Visits every vertex in the graph
  * Eulerian : Visits every edge in the graph

* Independent Set: Given graph G and a number k, does G contain a set of at least k independent vertices?
* Vertex Cover : Given a graph G and a number k, does G contain a vertex cover of size at most k

> Maximal independent set

* Given an undirected graph, find the largest set of vertices such that no two are connected with an edge
* Instance : an undirected graph
* Solution format : subset of vertices = S
* Constraint : no two vertices in S are connected by an edge
* Objective : Maximize |S|
* Runtime: 2T(n- 1) + O(n)

> Seven Bridge of Konigsberg

![Seven Bridge of Konigsberg](images/20210304_232224.png)

* Whenever one enters a vertex by a bridge, one leaves the vertex by a bridge
* In other words, during any walk in the graph, # enters a non-terminal vertex equals # one leaves it
* However, there are 4 vertices with odd degrees, so we cannot create a desired path

> Cycle Detect Proof

* Undirected connected graph G has a cycle if and only if it’s DFS output tree has a back edge

* Complexity O(V + E)
* Proof → : Suppose DFS tree has no back edge
  * Then all of the original edges are in the DFS tree. Then the graph itself is a tree (no cycles)
* ← : Suppose the graph is a tree (has no cycles) then there can’t be any backedges
  * because the DFS output tree is a tree with all the vertices

{% problem 'graph' %}

## Unweighted Graph

### Articulation

> Proof Articulation point

* case v = root
  * vertex will be the point of articulation iff this vertex has more than one child
* case v ≠ root
  * During DFS create traversal tree (v, to) is articulation
  * iff none of vertices or descendents has a back-edge to any of the ancestors of v then v is an articulation point
  * visited time ≤ low time of adjacent vertex

{% problem 'articulation' %}

### BFS

* [BFS vs DFS](https://www.youtube.com/watch?v=pcKY4hjDrxk)

> BFS Proof

* After BFS is done, dist(v) is the length of the shortest path from s to v
  * → After every iteration, dist(v) is the length of some path from s to v

* loop invariant
  * ← After BFS is done, dist(v) is the length of the shortest path from s to v for all vertices v in V

* Suppose there is a path p from s to v such that length(p) < dist(v)
* Then let z be the last vertex in the path st dist(z) = d(z) and let w be first vertex in thee path st dist(w) > d(w)

* Case 1: d(w) = d(z) + 1
  * Then in the algorithm z is put in the queue before q and when z is ejected, w is injected with dist(w) =
* Case 2: d(w) > d(z) + 1. Then the path p is actually not the shortest path

* Complexity
  * Notice that in BFS, each vertex enters the queue (F) at most one time
  * This was the assumption we made about graph search when we calculated its Complexity
  * So BFS runs in O V + E time

{% problem 'bfs' %}

### BFS 2d

{% problem 'bfs-2d' %}

### BFS 2d path

{% problem 'bfs-2d-path' %}

### BFS 01

{% problem 'bfs-01' %}

### Floodfill

{% problem 'floodfill' %}

### DFS

> DFS Proof

* After BFS is done, dist(v) is the length of the shortest path from s to v
* → After every iteration, dist(v) is the length of some path from s to v

* loop invariant : ← After BFS is done, dist(v) is the length of the shortest path from s to v for all vertices v in V
* Suppose there is a path p from s to v such that length(p) < dist(v)
* Then let z be last vertex in path s.t. dist(z) = d(z) and let w be first vertex in thee path s.t. dist(w) > d(w)

* Case 1: d(w) = d(z) + 1
  * Then in the algorithm z is put in the queue before q and when z is ejected, w is injected with dist(w) = d(z) + 1
* Case 2: d(w) > d(z) + 1
  * Then the path p is actually not the shortest path

* Complexity
  * Notice that in BFS, each vertex enters the queue (F) at most one time
  * This was the assumption we made about graph search when we calculated its Complexity
  * So BFS runs in O V + E time

{% problem 'dfs' %}

### Eulerian

{% problem 'eulerian' %}

### SCC

{% problem 'scc' %}

### BCC

* maximal biconnected subgraph
* connected graph decomposes into a tree of biconnected components called the block-cut tree of the graph

![BCC](images/20210602_015252.png)

{% problem 'bcc' %}

## Disjoint Set

> Terms

* Strongly Connected Component
  * [Visualization](https://www.cs.usfca.edu/~galles/JavascriptVisual/ConnectedComponent.html)
  * [Strongly Connected Component](https://www.youtube.com/watch?v=RpgcYiky7uw)

> SCC algorithm

* Run DFS on G and order the vertices in decreasing order of the postnumbers from the previous step
* Every time DFS increments cc, you have found a new SCC
* Complexity : O(V + E)

{% problem 'disjoint-set' %}

## Weighted Graph

### A Star

* cost = d(s,c) + h(c) (function h is heustic)

![A*](images/20210218_003647.png)

{% problem 'a-star' %}

### Bellman Ford

* Single source shortest path in O(V x E)
* Can be used to detect negative-weight cycles

{% problem 'bellman-ford' %}

### Dijkstra

* Doesn't work for negative edge weight
* Complexity: O(V \* O(deletemin) + E \* O(decreasekey))

> Proof of Dijkstra

* Claim: After Dijkstra’s is done, dist(v) is the length of the shortest path from s to v
* (→) After every iteration, dist(v) is the length of some path from s to v
* (←) After Dijkstra’s is done, dist(v) is the length of the shortest path from s to v for all vertices v ∈ V

| Type        | Array                               | Heap                               |
| ----------- | ----------------------------------- | ---------------------------------- |
| Approach    | indexed by vertex, giving key value | each key value is less than parent |
| deletemin   | O(V)                                | O(log(V))                          |
| decreasekey | O(1)                                | O(log(V))                          |

{% problem 'dijkstra' %}

### Floyd

* all pairs shortest pathSoftest path from every pair in O(V^3)

{% problem 'floyd' %}

### Ordering

{% problem 'ordering' %}

### TSP

{% problem 'tsp' %}

### Minimum Spanning Tree

> Prims Algorithm

* Put all vertices in U
* Pick any vertex s to start from
* Put s in X
* Repeat until all vertices are in X
  * Find the minimum edge that has one vertex in X and one vertex in U
  * Move the endpoint that is in U to X
  * Add that edge to the output

> Kruskal Algorithm

* Pick the next lightest edge that doesn't create a cycle

* Given an undirected, connected graph with positive edge weights:
  * Start with only the vertices
  * Repeat until graph is connected:
    * Add the lightest edge that doesn't create a cycle

{% problem 'minimum-spanning-tree' %}

## Flow

{% problem 'flow' %}

### Bipartite Matching

![Flow](images/20210530_131717.png)

* Reducible to max flow

{% problem 'bipartite-matching' %}
