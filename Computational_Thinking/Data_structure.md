# Java Data Structure

## Stack

{% tabs %}
{% tab title='stack.md' %}

* Stack.push() put a value into the stack
* Stack.pop() remove a value at the end of the stack
* stack.peek() return the vlaue at the top
* Stack.isEmpty() return true if the stack is empty
* Stack.size() return the size of the stack

```java

    Stack<Integer> stack = new Stack<>();

    stack.push(value);

    stack.pop();

    stack.peek();

    stack.isEmpty();

    stack.size();

```

{% endtab %}
{% endtabs %}

## Queue

{% tabs %}
{% tab title='queue.java' %}

* queue.add(value);
* queue.remove();
* queue.peek();
* q.size()

```java
Queue<T> queue = new LinkedList<>();

queue.add(value);
queue.remove();
queue.peek();
queue.size()

```

{% endtab %}
{% endtabs %}

## Deque

{% tabs %}
{% tab title='deque.java' %}

```java

Deque<> deque = new deque<>()

deque.add("Element 1 (Tail)");

// Add at the first
deque.addFirst("Element 2 (Head)");

// Add at the last
deque.addLast("Element 3 (Tail)");

// Add at the first
deque.push("Element 4 (Head)");

// Add at the last
deque.offer("Element 5 (Tail)");

// Add at the first
deque.offerFirst("Element 6 (Head)");

```

{% endtab %}
{% endtabs %}
