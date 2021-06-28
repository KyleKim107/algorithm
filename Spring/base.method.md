# Method

> Collections Class

* 단일 요소의 배열에는 asList() 대신 singletonList()를 사용하자.

  * 무슨말? 메모리 절약을 위해서 요소가 없거나(empty) 하나인 경우에는 Collections.emptyList() 또는 Collections.singletonList()를 사용해라.
