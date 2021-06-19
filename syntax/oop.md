# OOP

## Function

> baekjoon

* [Level 4 : 싱기한 네자리 숫자](http://acmicpc.net/problem/6679)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/function/BJ_6679.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/function/BJ_1668.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/function/BJ_15596.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/function/BJ_1357.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/function/BJ_4673.md)

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

## Class

> baekjoon

* [Level 6 : 직사각형](http://acmicpc.net/problem/15687)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/BJ_15687.md)

{% tabs %}
{% tab title='BJ_15687.md' %}

> Question

* Deisng Rectangle class with following methods
  * get_width / get_height / set_width / set_height
  * area / perimeter / is_square

```txt
class Rectangle:
  # TODO
```

{% endtab %}
{% tab title='BJ_15687.cpp' %}

```cpp
class Rectangle{
  public:
  int width, height;
  Rectangle(int w, int h) : width(w), height(h) {}
  int get_width() const { return width; }
  int get_height() const { return height; }
  void set_width(int w) { if(w>0 && w<=1000) width = w; }
  void set_height(int h) { if(h>0 && h<=2000) height = h; }
  int area() const { return width * height; }
  int perimeter() const { return 2 * (width + height); }
  bool is_square() const { return width == height; }
};
```

{% endtab %}
{% endtabs %}

> leetcode

* [Level Easy : Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_346.md)

{% tabs %}
{% tab title='LC_346.md' %}

> Question

* Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window

```txt
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```

{% endtab %}
{% tab title='LC_346.py' %}

```py
class MovingAverage:
  def __init__(self, size):
    self.size = size
    self.arr = []

  def next(self, val):
    if len(self.arr) == self.size:
      self.arr.pop(0)

    self.arr.append(val)
    return sum(self.arr) / len(self.arr)
```

{% endtab %}
{% endtabs %}

* [Level Easy : Design Parking System](https://leetcode.com/problems/design-parking-system)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_1603.md)

{% tabs %}
{% tab title='LC_1603.md' %}

> Question

* Design parking system

```txt
Input:
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]

Output:
[null, true, true, false, false]
```

{% endtab %}
{% tab title='LC_1603.py' %}

```py
class ParkingSystem:
  def __init__(self, big, medium, small):
    self.A = [big, medium, small]

  def addCar(self, carType):
    self.A[carType - 1] -= 1
    return self.A[carType - 1] >= 0
```

{% endtab %}
{% endtabs %}

* [Level Easy : Design HashMap](https://leetcode.com/problems/design-hashmap)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_706.md)

{% tabs %}
{% tab title='LC_706.md' %}

> Question

* MyHashMap() initializes the object with an empty map
* void put(int key, int value) inserts a (key, value) pair into the HashMap
  * If the key already exists in the map, update the corresponding value
* int get(int key) returns the value to which the specified key is mapped
  * -1 if this map contains no mapping for the key
* void remove(key) removes the key and its corresponding value if the map contains the mapping for the key

```txt
Input:
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output: [null, null, null, 1, -1, null, 1, null, -1]
```

{% endtab %}
{% tab title='LC_706.cpp' %}

```cpp
struct Node {
public:
  int key, val;
  Node* next;
  Node(int k, int v, Node* n) : key (k), val (v), next (n) {}
};
class MyHashMap {
public:
  const static int size = 19997;
  const static int mult = 12582917;
  Node* data[size];
  int hash(int key) {
    return (int)((long)key * mult % size);
  }
  void put(int key, int val) {
    remove(key);
    int h = hash(key);
    Node* node = new Node(key, val, data[h]);
    data[h] = node;
  }
  int get(int key) {
    int h = hash(key);
    Node* node = data[h];
    for (; node != NULL; node = node->next)
      if (node->key == key) return node->val;
    return -1;
  }
  void remove(int key) {
    int h = hash(key);
    Node* node = data[h];
    if (node == NULL) return;
    if (node->key == key) data[h] = node->next;
    else
      for (; node->next != NULL; node = node->next)
        if (node->next->key == key) {
          node->next = node->next->next;
          return;
        }
  }
};
```

{% endtab %}
{% tab title='LC_706.java' %}

```java
class MyHashMap {
  final ListNode[] nodes = new ListNode[10000];

  public void put(int key, int value) {
    int i = idx(key);
    if (nodes[i] == null)
      nodes[i] = new ListNode(-1, -1);
    ListNode prev = find(nodes[i], key);
    if (prev.next == null)
      prev.next = new ListNode(key, value);
    else prev.next.val = value;
  }

  public int get(int key) {
    int i = idx(key);
    if (nodes[i] == null)
      return -1;
    ListNode node = find(nodes[i], key);
    return node.next == null ? -1 : node.next.val;
  }

  public void remove(int key) {
    int i = idx(key);
    if (nodes[i] == null) return;
    ListNode prev = find(nodes[i], key);
    if (prev.next == null) return;
    prev.next = prev.next.next;
  }

  int idx(int key) { return Integer.hashCode(key) % nodes.length;}

  ListNode find(ListNode bucket, int key) {
    ListNode node = bucket, prev = null;
    while (node != null && node.key != key) {
      prev = node;
      node = node.next;
    }
    return prev;
  }

  class ListNode {
    int key, val;
    ListNode next;

    ListNode(int key, int val) {
      this.key = key;
      this.val = val;
    }
  }
}
```

{% endtab %}
{% tab title='BJ_5613.js' %}

```js
class ListNode {
  constructor(key, val, next) {
    this.key = key
    this.val = val
    this.next = next
  }
}
class MyHashMap {
  constructor() {
    this.size = 19997
    this.mult = 12582917
    this.data = new Array(this.size)
  }
  hash(key) { return key * this.mult % this.size }
  put(key, val) {
    this.remove(key)
    let h = this.hash(key)
    let node = new ListNode(key, val, this.data[h])
    this.data[h] = node
  }
  get(key) {
    let h = this.hash(key), node = this.data[h]
    for (; node; node = node.next)
      if (node.key === key) return node.val
    return -1
  }
  remove(key) {
    let h = this.hash(key), node = this.data[h]
    if (!node) return
    if (node.key === key) this.data[h] = node.next
    else for (; node.next; node = node.next)
      if (node.next.key === key) {
        node.next = node.next.next
        return
      }
  }
};
```

{% endtab %}
{% tab title='LC_706.py' %}

```py
class ListNode:
  def __init__(self, key = None, val = None):
    self.pair = (key, val)
    self.next = None

class MyHashMap:
  def __init__(self):
    self.m = 1000
    self.h = [ListNode() for _ in range(self.m)]

  def put(self, key, value):
    idx = key % self.m
    cur = self.h[idx]
    while True:
      if cur.pair[0] == key:
        cur.pair = (key, value)
        return
      if cur.next == None:
        break
      cur = cur.next
    cur.next = ListNode(key, value)

  def get(self, key):
    idx = key % self.m
    cur = self.h[idx]
    while cur:
      if cur.pair[0] == key:
        return cur.pair[1]
      cur = cur.next
    return -1

  def remove(self, key):
    idx = key % self.m
    cur = prev = self.h[idx]
    cur = cur.next

    while cur:
      if cur.pair[0] == key:
        prev.next = cur.next
        break
      cur, prev = cur.next, prev.next
```

{% endtab %}
{% endtabs %}

* [Level Medium : Finding Pairs With a Certain Sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_1865.md)

{% tabs %}
{% tab title='LC_1865.md' %}

> Question

* given two integer arrays nums1 and nums2, implement a data structure that supports queries of two types:
  * Add a positive integer to an element of a given index in the array nums2
  * Count the number of pairs (i, j) s.t. nums1[i] + nums2[j] equals a given value

```txt
Input:
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]

Output:
[null, 8, null, 2, 1, null, null, 11]
```

{% endtab %}
{% tab title='LC_1865.py' %}

```py
class FindSumPairs:
  def __init__(self, nums1: List[int], nums2: List[int]):
    self.c1, c2 = Counter(nums1), Counter(nums2)
    self.l2 = nums2

  def add(self, idx: int, val: int) -> None:
    self.c2[self.l2[idx]] -= 1
    self.l2[idx] += val
    self.c2[self.l2[idx]] += 1

  def count(self, tot: int) -> int:
    return sum(v * self.c2[tot - k] for k, v in self.c1.items())
```

{% endtab %}
{% endtabs %}

* [Level Medium : Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_251.md)

{% tabs %}
{% tab title='LC_251.md' %}

> Question

* Design flattened 2D Vector

```txt
Input:
[
  [1,2],
  [3],
  [4,5,6]
]

Output: [1,2,3,4,5,6]
```

{% endtab %}
{% tab title='LC_251.py' %}

```py
class Vector2D:
  def __init__(self, lis):
    def it():
      for li in lis:
        for el in li:
          self.size -= 1
          yield el
    self.it = it()
    self.size = sum(len(li) for li in lis)

  def next(self) -> int:
    return next(self.it)

  def hasNext(self) -> bool:
    return self.size
```

{% endtab %}
{% endtabs %}

* [Level Medium : Design Twitter](https://leetcode.com/problems/design-twitter)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_355.md)

{% tabs %}
{% tab title='LC_355.md' %}

> Question

* Design twitter with following methods
  * postTweet(userId, tweetId)
  * getNewsFeed(userId)
  * follow(follwerId, followeeId)
  * unfollow(follwerId, follweeId)

```txt
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output: [null, null, [5], null, null, [6, 5], null, [5]]
```

{% endtab %}
{% tab title='LC_355.py' %}

```py
class Twitter(object):
  def __init__(self):
    self.timer = itertools.count(step=-1)
    self.tweets = collections.defaultdict(collections.deque)
    self.followees = collections.defaultdict(set)

  def postTweet(self, userId, tweetId):
    self.tweets[userId].appendleft((next(self.timer), tweetId))

  def getNewsFeed(self, userId):
    tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
    return [t for _, t in heapq.nsmallest(10, tweets)]

  def follow(self, followerId, followeeId):
    self.followees[followerId].add(followeeId)

  def unfollow(self, followerId, followeeId):
    self.followees[followerId].discard(followeeId)
```

{% endtab %}
{% endtabs %}

* [Level Medium : Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_535.md)

{% tabs %}
{% tab title='LC_535.md' %}

> Question

* Design url shortener

```txt
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
```

{% endtab %}
{% tab title='LC_535.py' %}

```py
class Codec:
  def __init__(self):
    self.long_short = {}
    self.short_long = {}
    self.alphabet = string.ascii_letters + string.digits

  def encode(self, longUrl):
    while longUrl not in self.long_short:
      code = "".join(choices(self.alphabet, k=6))
      if code not in self.short_long:
        self.short_long[code] = longUrl
        self.long_short[longUrl] = code
    return 'http://tinyurl.com/' + self.long_short[longUrl]

  def decode(self, shortUrl):
    return self.short_long[shortUrl[-6:]]
```

{% endtab %}
{% endtabs %}

* [Level Medium : Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_208.md)

{% tabs %}
{% tab title='LC_208.md' %}

> Question

* Design Trie

```txt
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]
```

{% endtab %}
{% tab title='LC_208.cpp' %}

```cpp
class Trie {
public:
  Trie() {}

  void insert(string word) {
    Trie* node = this;
    for (char ch : word) {
      if (!node->next.count(ch)) node->next[ch] = new Trie();
      node = node->next[ch];
    }
    node->isword = true;
  }

  bool search(string word) {
    Trie* node = this;
    for (char ch : word) {
      if (!node->next.count(ch)) return false;
      node = node->next[ch];
    }
    return node->isword;
  }

  bool startsWith(string prefix) {
    Trie* node = this;
    for (char ch : prefix) {
      if (!node->next.count(ch)) return false;
      node = node->next[ch];
    }
    return true;
  }

private:
  map<char, Trie*> next = {};
  bool isword = false;
};
```

{% endtab %}
{% tab title='LC_208.py' %}

```py
class Trie:
  def __init__(self):
    T = lambda: collections.defaultdict(T)
    self.root = T()

  def insert(self, word):
    reduce(dict.__getitem__, word, self.root)['#'] = True

  def search(self, word):
    return '#' in reduce(lambda cur, c: cur.get(c, {}), word, self.root)

  def startsWith(self, prefix):
    return bool(reduce(lambda cur, c: cur.get(c, {}), prefix, self.root))
```

{% endtab %}
{% endtabs %}

* [Level Medium : Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_676.md)

{% tabs %}
{% tab title='LC_676.md' %}

> Question

* Implement the MagicDictionary class:
  * MagicDictionary() Initializes the object
  * void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary
  * bool search(String searchWord) Returns if change exactly one character in searchWord to match any string in data structure

```txt
Input:
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

Output: [null, null, false, true, false, false]
```

{% endtab %}
{% tab title='LC_676.py' %}

```py
class MagicDictionary:
  def _candidates(self, word):
    for i in range(len(word)):
      yield word[:i] + '*' + word[i+1:]

  def buildDict(self, words):
    self.words = set(words)
    self.near = collections.Counter(cand for word in words for cand in self._candidates(word))

  def search(self, word):
    return any(self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidates(word))
```

{% endtab %}
{% endtabs %}

* [Level Hard : LFU Cache](https://leetcode.com/problems/lfu-cache)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_460.md)

{% tabs %}
{% tab title='LC_460.md' %}

> Question

* Deisng LFU Cache

```txt
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]
```

{% endtab %}
{% tab title='LC_460.py' %}

```py
from collections import defaultdict
from collections import OrderedDict

class Node:
  def __init__(self, key, val, count):
    self.key = key
    self.val = val
    self.count = count

class LFUCache(object):
  def __init__(self, capacity):
    self.cap = capacity
    self.key2node = {}
    self.count2node = defaultdict(OrderedDict)
    self.minCount = None

  def get(self, key):
    if key not in self.key2node:
      return -1

    node = self.key2node[key]
    del self.count2node[node.count][key]

    if not self.count2node[node.count]:
      del self.count2node[node.count]

    node.count += 1
    self.count2node[node.count][key] = node

    if not self.count2node[self.minCount]:
      self.minCount += 1

    return node.val

  def put(self, key, value):
    if not self.cap:
      return

    if key in self.key2node:
      self.key2node[key].val = value
      self.get(key) # NOTICE, put makes count+1 too
      return

    if len(self.key2node) == self.cap:
      # popitem(last=False) is FIFO, like queue
      k, n = self.count2node[self.minCount].popitem(last=False)
      del self.key2node[k]

    self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
    self.minCount = 1
```

{% endtab %}
{% endtabs %}

* [Level Hard : Design Skiplist](https://leetcode.com/problems/design-skiplist)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/class/LC_1206.md)

{% tabs %}
{% tab title='LC_1206.md' %}

> Question

* Design a Skiplist without using any built-in libraries
  * O(log(n)) time to add, erase and search

```txt
Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return false.
skiplist.add(4);
skiplist.search(1);   // return true.
skiplist.erase(0);    // return false, 0 is not in skiplist.
skiplist.erase(1);    // return true.
skiplist.search(1);   // return false, 1 has already been erased.
```

{% endtab %}
{% tab title='LC_1206.py' %}

```py
class Node:
  def __init__(self, val, levels):
    self.val = val
    self.levels = [None] * levels

class Skiplist(object):
  def __init__(self):
    self.head = Node(-1, 16)

  def _iter(self, num):
    cur = self.head
    for level in range(15, -1, -1):
      while True:
        future = cur.levels[level]
        if future and future.val < num:
          cur = future
        else:
          break
      yield cur, level

  def search(self, target):
    for prev, level in self._iter(target):
      pass
    cur = prev.levels[0]
    return cur and cur.val == target

  def add(self, num):
    nodelvls = min(16, 1 + int(math.log2(1.0 / random.random())))
    node = Node(num, nodelvls)
    for cur, level in self._iter(num):
      if level < nodelvls:
        future = cur.levels[level]
        cur.levels[level] = node
        node.levels[level] = future

  def erase(self, num):
    ans = False
    for cur, level in self._iter(num):
      future = cur.levels[level]
      if future and future.val == num:
        ans = True
        cur.levels[level] = future.levels[level]
    return ans
```

{% endtab %}
{% endtabs %}

## Import

> baekjoon

* [Level 3 : 경기 결과](http://acmicpc.net/problem/5523)
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_5523.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_12840.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_11718.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_1247.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_4806.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_15552.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_11719.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_11723.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_15688.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_11931.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_4375.md)

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
  * [Update solution](https://github.com/SeanHwangG/algorithm/edit/main/syntax/oop/import/BJ_13977.md)

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
