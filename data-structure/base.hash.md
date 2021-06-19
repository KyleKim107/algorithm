# Hash

| Term             | Meaning                                 |
| ---------------- | --------------------------------------- |
| Identity law     | $A \cup \varnothing=A$                  |
| Idempotent Law   | $A \cup A =A$                           |
| Domination Law   | $A \cup U =U$                           |
| Communtative Law | $A \cup B =B \cup A$                    |
| Associative Law  | $(A \cup B) \cup C = A \cup (B \cup C)$ |

> Bloom Filter (Burton Howard Bloom, 1970)

* space-efficient probabilistic data structure used to test whether an element is a member of a set
* False positive matches are possible, but false negatives are not

> Cuckoo hashing

* Use two hash functions
* O(1) : worst case insert / lookup

![cuckoo hasing](images/20210218_232251.png)

## Encoding

{% tabs %}
{% tab title='python.md' %}

> hashlib

* implements a common interface to many different secure hash and message digest algorithms

* sha224(str_.encode()).hexdigest()

{% endtab %}
{% endtabs %}

{% problem 'encoding' %}

## Decoding

{% problem 'decoding' %}

## Set

{% tabs %}
{% tab title='javascript.md' %}

* length
* add()
* clear()
* delete(`value`) : Delete `value` in set
* has(`value`) : Check existance of `value` in set

```js
// 1. Basic example
var set = new Set();
new Set([1, 2, 3, 4, 5]);

// 2. Remove duplicate in array
const numbers = [2,3,4,4,2,3,3,4,4,5,5,6,6,7,5,32,3,4,5]
console.log([...new Set(numbers)])
```

{% endtab %}
{% endtabs %}

{% problem 'set' %}

### Multiset

{% problem 'multiset' %}

### Ordered Set

* Natively supported in c++ (Implemented in BST)

{% problem 'ordered-set' %}

## Map

{% tabs %}
{% tab title='javascript.md' %}

* Map object holds key-value pairs and remembers the original insertion order of the keys

```js
// 1. CRUD Object
var person = {firstName:"John", lastName:"Doe", age:50};
var person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;

obj.[key] || 0           // Use default
delete dict[entry[0]]    // Delete Keys
Object.keys(obj).reduce((a, b) => obj[a] > obj[b] ? a : b);    // Get the largest keys
delete query["obsolte"];

// 2. Merge Object using spread operator
var obj2 = { foo: 'baz', y: 13 };
var mergedObj = { ...obj1, ...obj2 };                    // merge objects

const person = {firstName: “sean”, lastName: “hwang”}   // Destruct object

Object.keys(myObject).length                            // Iterate key value
Object.entries(obj).forEach(([key, value]) => { console.log(key, value); });

where: {
  ...(params.val && {key : val}), // optional key
}

// 3. Destructuring
const {firstName: fn, lastName: ln} = person
console.log(`${fn} ${ln}`)
let [first, last] = ['sean', 'hwang']    // Destruct Array
console.log(first);
```

{% endtab %}
{% endtabs %}

{% problem 'map' %}

### Counter

{% tabs %}
{% tab title='python.md' %}

> Counter

* subclass of dict
* [Counter](https://docs.google.com/forms/d/1m1F3h8PzaSuVO6rqFZko9amMXTo_-NNj1UdfiD5ihGU/edit)
  * elements() : iterator over elements repeating count | ignore if less than one
  * most_common([k]) : Return k most common key value pair in order in O(n log k)
  * subtract([iterable-or-mapping]) : Subtract another mapping
  * update([iterable-or-mapping]) : Add another mapping

```py
from collections import Counter

# 1. CRUD Counter
Counter()
Counter('gallahad')            # new counter from an iterable
Counter({'red': 4, 'blue': 2}) # new counter from a mapping
Counter(cats=4, dogs=8)        # keyword args

co['a'] += 1      # update
del c['sausage']  # remove
```

{% endtab %}
{% endtabs %}

{% problem 'counter' %}
