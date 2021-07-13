# Method

> Collections Class

* 단일 요소의 배열에는 asList() 대신 singletonList()를 사용하자.

  * 무슨말? 메모리 절약을 위해서 요소가 없거나(empty) 하나인 경우에는 Collections.emptyList() 또는 Collections.singletonList()를 사용해라.

> ApplicationContext

* 스프링 콘테이너

* 기존에는 개발자가 AppConfig 를 사용해서 직접 객체를 생성하고 DI를 했지만, 이제부터는 스프링 컨테이 너를 통해서 사용한다.

  * applicationContext.getBean()

    * 이제부터는 스프링 컨테이너 를 통해서 필요한 스프링 빈(객체)를 찾아야 한다
