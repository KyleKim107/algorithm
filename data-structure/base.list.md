# List

* data organization, management, and storage format that enables efficient access and modification

{% tabs %}
{% tab title='java.md' %}

> Staitc methods

* List\<T\> asList​(T... a) : Returns a fixed-size list backed by the specified array
* T binarySearch​() : Searches a range of the specified array for the specified object using the binary search algorithm
  * T[] a, int fromIndex, int toIndex, T key, Comparator<? super T> c

* int compare​(T[] a, T[] b) : Compares two double arrays lexicographically
* byte[] copyOf​(T[] original, int newLength) : Copies the specified array, truncating or padding with zeros
* boolean equals​(T[] a, T[] a2) : Returns true if the two specified arrays of longs are equal to one another
* void fill​(T[] a, T val) : Assigns the specified char value to each element of the specified array of T
* int hashCode​(T[] a) : Returns a hash code based on the contents of the specified array
* int mismatch​() : Finds and returns relative index of first mismatch between two byte arrays over the specified ranges
  * T[] a, int aFromIndex, int aToIndex
  * T[] b, int bFromIndex, int bToIndex
* void parallelSort​(T[] a) : Sorts the specified array into ascending numerical order (Faster than sort)

```java
// 1. Array iterate
int arr[] = {1, 2, 3};
for (int d : arr) System.out.println(d);

// 2. Custom object
Object[] myArray = new Object[100]
Java allocates 100 places to put your objects in. It does NOT instantiate your objects for you.

You can do this:

SomeClass[] array = new SomeClass[100];

for (int i = 0; i < 100; i++) {
    SomeClass someObject = new SomeClass();
    // set properties
    array[i] = someObject;
}

// 3. Pass array to function
void foo(int[] numPlayers) { }

foo(new int[] { 10, 15, 20 });
```

{% endtab %}
{% tab title='javascript.md' %}

* Spread : ..., use to copy contents of objects

> Array

* length : Size of array
* concat()
* copyWithin()
* entries()
* every()
* fill()
* filter() : array.filter(value => value < 0);
* find()
* findIndex()
* forEach() : arr.forEach((num, index) => { arr[index] = num * 2; });
* from()
* includes()
* indexOf()
* isArray()
* join()
* keys()
* lastIndexOf()
* map() : let doubled = arr.map(num => { return num * 2; });
* pop()
* prototype
* push()
* reduce() : [].reduce((a, b) => a + b);        // sum
* reduceRight()
* reverse() : loop backward
* shift() : get first element = poll in queue
* slice()
* some()
* sort() : items.sort((a, b) => { return a.value - b.value; });
* splice() : items.splice(pos, num, newval);
* toString()
* unshift()
* valueOf()
* splice(index, delete); : remove elements
* split(',').map(Number); : split as an integer
* map(x=>x[0]); : first column of 2d array

```js
new Array(len).fill(0);

// 1. Uppercase all array
var fruits = ["Banana", "Orange", "Apple", "Mango"];
Array.prototype.myUcase = function() {
  for (i = 0; i < this.length; i++)
    this[i] = this[i].toUpperCase();
};

// 2. Spread
var arr = ['a','b', 'c']
var added = [...arr, 'd']                // Copy Array

function add(x, y, z) { console.log(x+y+z) }  // Pass array as parameter
var args = [0, 1, 2, 3]
add(...args)

var obj1 = { foo: 'bar', x: 42 };
var clonedObj = { ...obj1 };            // Clone and merge object

var obj2 = { foo: 'baz', y: 13 };
var mergedObj = { ...obj1, ...obj2 };    // merge objects
```

{% endtab %}
{% endtabs %}

{% problem 'list' %}

## Dimension 2

{% problem 'dimension-2' %}

## LinkedList

| Type          | Access | Search | Insert | Delete |
| ------------- | ------ | ------ | ------ | ------ |
| Array         | 1      | n      | n      | n      |
| Stack         | n      | n      | 1      | 1      |
| Queue         | n      | n      | 1      | 1      |
| Singly-Linked | n      | n      | 1      | 1      |
| Doubly-Linked | n      | n      | 1      | 1      |

{% problem 'linkedlist' %}

### Iterator

{% problem 'iterator' %}

{% tabs %}
{% tab title='java.md' %}

> Iterator

* remove() : Removes from the underlying collection the last element returned by this iterator

* ListIterator
  * `List`.listIterator() : Create list iterator

```java
// 1. Traverse backwards
ListIterator listIterator = list.listIterator(list.size());

while (listIterator.hasPrevious()) {
  System.out.println(listIterator.previous());
}
```

{% endtab %}
{% endtabs %}

### Skiplist

{% problem 'skiplist' %}

## Deck

> Maximum in sliding window

* Question
  * Given a large array of integers and a window of size w
  * find the current maximum value in the window as the window slides through the entire array

* Solution
  * O(N)
  * Remove the indices of all elements from the back of the deque, which are smaller than or equal to the current element
  * If the element no longer falls in the current window, remove the index of the element from the front
  * Push the current element index at the back of the window
  * The index of the current maximum element is at the front

{% problem 'deck' %}

### Stack

{% problem 'stack' %}

### Queue

{% problem 'queue' %}

### Priority queue

{% tabs %}
{% tab title='python.md' %}

> heapq

* smallest element is always the root
* If you want to use max heap, multiply by -1
* heappush(heap, item)
* heappop(heap)
* heapify(x) : Transform list x into a heap, in-place, in linear time
* merge(*iterables, key=N, reverse=F) : Merge sorted inputs into a single sorted output
* nlargest(n, iterable, key=N) : return n th largest index and number
* nsmallest(n, iterable, key=N)

```py
# 1. print_order
heapify lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heapify(lst)    # [0, 1, 3, 2, 5, 4, 7, 9, 6, 8]
heappush(lst, 10)
for i in range(k):
  ans = heapq.heappop(lst)
```

{% endtab %}
{% endtabs %}

{% problem 'priority-queue' %}

### Monotonic Deque

{% problem 'monotonic-deque' %}
