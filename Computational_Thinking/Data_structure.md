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
queue.size();

```

{% endtab %}
{% endtabs %}

## Deque

{% tabs %}
{% tab title='deque.java' %}

```java

Deque<> deque = new LinkedList<>()

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

## Heap

* Max Heap

{% tabs %}
{% tab title='Heap.java' %}

Heaptify하는데 Log N 만큼의 시간복잡도가 요구된다
    자식 노드들과 비교하며, 자식보다 부모 노드가 클때까지 밑으로 타고 내려간다

```java

public class MaxHeap {
    int[] elements;
    int pos;

    public MaxHeap() {
        this(10);
    }

    public MaxHeap(int size) {
        elements = new int[size + 1];  // 0번 버리고 1번째부터 사용함
    }

    public boolean isFull() { return pos == elements.length - 1; }

    public void print() {
        for (int i = 1; i <= pos; i++) {
            System.out.print(elements[i] + " ");
        }
        System.out.println();
    }

    public void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void offer(int data) {
        if (isFull()) {
            increaseCapacity();
        }
        elements[++pos] = data;  // 힙크기 하나 증가하고 마지막 노드에 data 삽입
        int idx = pos; // 현재 위치 변수 설정
        while (idx > 1 && elements[idx] > elements[idx / 2]) { // 자식것이 크면 교환
            swap(elements, idx, idx / 2);
            idx /= 2;
        }
    }

    private void increaseCapacity() {
        elements = Arrays.copyOf(elements, elements.length * 2);
    }

    public int poll() {

        if (pos == 0) {
            return -1;// 데이터 없을때
        }
        int result = elements[1]; // 루트반환 - 현재 가장 큰 값
        elements[1] = elements[pos]; // 마지막 데이터를 루트 위치값으로 설정
        elements[pos] = 0; // 마지막 데이터를 지움
        pos--; // 사이즈 하나 줄임

        // 힙을 재정렬한다.
        heapify();
        return result;
    }

    public void heapify() { // 내부의 데이터를 heap 구조로 만드는 작업 (log N)
        // 첫번째 있던 정보와 그 자식노드와 비교해서 자식노드가 크면 그 노드와 변경하면서 가장 아래 level까지한다.
        int idx = 1;
        while (idx * 2 <= pos) {// 내가 자식들보다 크면 룹을 빠져 나온다
            if (elements[idx] >= elements[idx * 2] && elements[idx] >= elements[idx * 2 + 1]) {
                break;
            }

            // 그렇지 않으면 두 자식 중에 큰 값을 가진것과 교환한다.
            if (elements[idx * 2] > elements[idx * 2 + 1]) {
                swap(elements, idx, idx * 2);
                idx = idx * 2;
            } else {
                swap(elements, idx, idx * 2 + 1);
                idx = idx * 2 + 1;
            }
        }
    }
}



class HeepTest {
    public static void main(String[] args) {
        MaxHeap max = new MaxHeap(); // 현재 노드의 왼쪽을 보려면 i *2
        max.offer(3);   // 현재 노드의 왼쪽을 보려면 (i *2) + 1
        System.out.println(Arrays.toString(max.elements));
        max.offer(6);
        System.out.println(Arrays.toString(max.elements));
        max.offer(4);
        System.out.println(Arrays.toString(max.elements));
        max.offer(2);
        System.out.println(Arrays.toString(max.elements));
        max.offer(7);
        System.out.println(Arrays.toString(max.elements));
        max.offer(5);
        max.offer(1);
        max.offer(8);
        max.offer(9);
        max.offer(10);
        System.out.println(Arrays.toString(max.elements));
        System.out.println(max.poll());
        System.out.println(max.poll());
        System.out.println(max.poll());
        System.out.println(max.poll());
        System.out.println(max.poll());
        max.print();
    }
}

```

{% endtab %}
{% endtabs %}

## Set

* Set

* Set< Integer > set = new HashSet<>();

* set.add()

  * allow you add value into the set

* set.contains()

  * Check the set has the value
