# Theory

## Spring MVC

* client - > dispacher Servlet -> Controller - business components

* business components -> Controller -> View Resolver - > Views -> Dispatch Servlet

* Client

![mvc](images/20210720_011920.png)

* Single ton

> Bean Factory

* 스프링 컨테이너의 최상위 인터페이스

* 스프링빈을 관리하고 조회하는 역할을 담당한다

* getBean()을 제공한다

> ApplicationContext

* Beanfactory기능을 모두 상속받아 제공

* BeanFactory기능을 모두 상속받아 제공한다

  * 애플리케이션을 개발할 때는 빈은 관리하고 조회하는 기능은 물론이고, 수 많은 부가기능이 필요하다.

![application Context 부가기능](images/20210711_231617.png)

> Singleton

* 스프링은태생이 온라인 서비스를 지원하기 위한 기술이다

* 웹앱은 보통 고객들이 동시에 요청한다

* 우리가 만들었던 스프링 없는 순수한 DI 컨테이너인 AppConfig는 요청을 할 때 마다 객체를 새로 생성한 다.

  * 고객 트래픽이 초당 100이 나오면 초당 100개 객체가 생성되고 소멸된다!

  * 해결방안은 해당 객체가 딱 1개만 생성되고, 공유하도록 설계하면 된다.

  * String은 기본적으로 싱글톤으로 컨테이너를 관리해준다

> 싱글톤 방식의 주의점

* 객체가 상태유지하게 설계하면 안된다 - 무상태로 설계해야한다

  * 특정 클라이언트에 의존적인 필드가 있으면 안된다

    * 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다

    * 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다

  * 가급적 읽기만 가능해야 한다.

## 의존관계 주입

* 생성자 주입

  * @Autowired

  * @Autowired 의 기본 동작은 주입할 대상이 없으면 오류가 발생한다.

    * 주입할 대상이 없어도 동작하게 하려면 @Autowired(required = false) 로 지정하면 된다.

{% tabs %}
{% tab title = AutoWired.java %}

생성자를 호출할때 @Autowired가 있으면 스프링이 컨테이너에서 빈을 꺼내서 알아주 주입한다.
이런식으로 스프링은 싱글톤을 보장한다. 생성자가 딱 하나 있다면 @Autowired를 생략 가능하다.

```java

  @Component
  public class OrderServiceImpl implements OrderService {
      private final MemberRepository memberRepository;
      private final DiscountPolicy discountPolicy;

@Autowired //  생성자(Constructor)가 딱 하나라면, 생략 가능하다.
      public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy
discountPolicy) {
          this.memberRepository = memberRepository;
          this.discountPolicy = discountPolicy;
      }
}

```

{% endtab %}
{% endtabs %}

* 수정자 주입

  * setter라 불리는 필드의 값을 변경하는 수정자 메서드를 통해서 의존관계를 주입하는 방법이다.

  {% tabs %}
  {% tab title = setter.java %}

  ```java

  @Component
    public class OrderServiceImpl implements OrderService {
        private MemberRepository memberRepository;
        private DiscountPolicy discountPolicy;

        @Autowired(required = false) // 만약 주입할 대상이 없어도 작동하게 하려면.
        public void setMemberRepository(MemberRepository memberRepository) {
            this.memberRepository = memberRepository;
        }

        @Autowired
        public void setDiscountPolicy(DiscountPolicy discountPolicy) {
            this.discountPolicy = discountPolicy;
        }
    }

  ```

  {% endtab %}
  {% endtabs %}

* 필드 주입

  * 생성자를 통해 빈을 초기화 할 필요가 없다. 코드가 간결해 지는 효과를 볼 수 있다.

  * !!!!! 하지만 !!!!!!!

  *

{% tabs %}
  {% tab title = field.java %}

  ```java

@Component
    public class OrderServiceImpl implements OrderService {
        @Autowired
        private MemberRepository memberRepository;
        @Autowired
        private DiscountPolicy discountPolicy;
  }

  ```

  {% endtab %}
  {% endtabs %}

* 일반 메서드 주입

* 의존관계에 사용할 객체들을 선언할떄 private final을 꼭 사용하자

{% tabs %}
{% tab title = field.java %}

  ```java

final키워드를 넣으면 생성자만 의존관계를 조종할 수 있고, 만약 필요한 객체가 생성자에 빠진다면 컴파일 에러가 난다.
(fianl은 생성자를 통한 DI방식만 사용가능하다.)

@Component
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) { //DYP를 지키고 있다
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
  }

  ```

  {% endtab %}
  {% endtabs %}
