# Divide Concur

> multiply Algorithm

$$ x = 2^{n/2}x_L + x_R $$
$$ y = 2^{n/2}y_L + y_R $$

{% tabs %}
{% tab title='multiply.py' %}

```py
# O(N)
def multiply (x: int, y: int) -> int:
  If n = 1 : return xy
  xL, xR and yL, yR are left-most and right-most n/2 bits of x and y, respectively.
  P1 = multiply(xL, yL)
  P2 = multiply(xL, yR)
  P3 = multiply(xR, yL)
  P4 = multiply(xR, yR)
  return P1 * 2**n + (P2 + P3) * 2 ** (n / 2) + P4
```

{% endtab %}
{% endtabs %}

## Master theorem

* Calculates Complexity for divide and conquer algorithm

$$
T(n)=a T\left(\frac{n}{b}\right)+O\left(n^{d}\right)
$$

$$
T(n) \epsilon\left\{\begin{array}{ll}
O\left(n^{d}\right) & \text { top heavy: } a<b^d \\
O\left(n^{d} \log n\right) & \text { steady : } a=b^{d} \\
O\left(n^{\log _{b} a}\right) & \text { bottom heavy: } a>b^{d}
\end{array}\right.
$$

* Proof: After k levels, there are $$a^k$$ subproblems, each of size $$\frac{n}{b^k}$$
* So, during the kth level of recursion, the time complexity

$$
O\left(\left(\frac{n}{b^{k}}\right)^{d}\right) a^{k}=O\left(a^{k}\left(\frac{n}{b^{k}}\right)^{d}\right)=O\left(n^{d}\left(\frac{a}{b^{d}}\right)^{k}\right)
$$

> Cook Toom

* multiplication algorithm for large integers
* Run Time $$ Θ(n^{1.46}) $$

## Binary Search

{% tabs %}
{% tab title='python.md' %}

> bisect

* bisect_left(`nums`, `x`) : first insert point for x in `nums` to maintain sorted order
* bisect_right(`nums`, `x`) : last insert point for x in `nums` to maintain sorted order
  * lo=0, hi=len(a) : set where to start, end in array
* bisect.insort_left(a, x, lo=0, hi=len(a)) : insert x in a in sorted order
  * a.insert(bisect.bisect_left(a, x, lo, hi), x) (a is sorted)
  * O(log n) search is dominated by the slow O(n) insertion step
* bisect.insort(a, x, lo=0, hi=len(a)) : inserting x in a after any existing entries of x

```py
# 1. Search on sorted list
def index(a, x):
  'Locate the leftmost value exactly equal to x'
  i = bisect_left(a, x)
  if i != len(a) and a[i] == x: return i
  raise ValueError

def find_lt(a, x):
  'Find rightmost value less than x'
  i = bisect_left(a, x)
  if i: return a[i-1]
  raise ValueError

def find_le(a, x):
  'Find rightmost value less than or equal to x'
  i = bisect_right(a, x)
  if i: return a[i-1]
  raise ValueError

def find_gt(a, x):
  'Find leftmost value greater than x'
  i = bisect_right(a, x)
  if i != len(a): return a[i]
  raise ValueError

def find_ge(a, x):
  'Find leftmost item greater than or equal to x'
  i = bisect_left(a, x)
  if i != len(a): return a[i]
  raise ValueError
```

{% endtab %}
{% endtabs %}

{% problem 'binary-search' %}

### Parametric Search

{% problem 'parametric-search' %}

### Ternary Search

{% problem 'ternary-search' %}

## Quick Select

{% problem 'quick-select' %}

## Meet in the middle

{% problem 'meet-in-the-middle' %}

## Recursion

[Recursion](https://www.youtube.com/watch?v=kx6DfrYfWnQ)

[Finbonacci](https://www.youtube.com/watch?v=zg-ddPbzcKM)

{% problem 'recursion' %}

### backtrack

* Bounding function : kill some live nodes without actually expanding them
* generic method that can be applied to problems with large solution set, in search and optimization problems
* often be a first step towards finding a greedy or dynamic programming algorithm
* often gives a more efficient runtime over exhaustive search or brute force
* but may not result in a polynomial time algorithm, and is usually an improved exponential time (also for NP-complete problems)
* Often, they are better on typical inputs that their worst-cast
* Difference between divide and conquer is decrease size by a factor vs difference
* Problem analysis
  * Instance : What does the input look like?
  * Solution format : What does the output look like?
  * Constraints : What properties must a solution have?
  * Objective function : What makes a solution have?

> 8 Queen

* Put 8 queens on a chessboard such that no two are attacking
* Brute force : Put all possible arrangements of 8 queens on the chess board
  * Instance : An empty 8 x 8 chess board
  * Solution format : A placement of 8 queens
  * Constraint : No two queens are attacking
  * Object : Find a solution with the constraint
* Consider one row at a time, eliminating possible non-solution board positions early in their construction

{% problem 'backtrack' %}
