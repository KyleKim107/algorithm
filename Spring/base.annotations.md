# Annotations

> @ID

    * Indicates that the property is the primary key.

        * Object can directly access the property

            * You can use variable without GetterSetter if you want to acess Getter of varaiable

> @GenetatedValue

    * Decide the policy for primary key

    * Parameters


        * AUTO : (persistence provider가) 특정 DB에 맞게 자동 선택

        * IDENTITY : DB의 identity 컬럼을 이용

        * SEQUENCE : DB의 시퀀스 컬럼을 이용

        * TABLE : 유일성이 보장된 데이터베이스 테이블을 이용

> @ Bean

    * @Controller, @Service, and @Repository annotation make them bean object in root container.

    * then let the spring use them on demand.

    * @Bean(name="memberService2")

    * 항상 다른 이름을 사용하자

> @Service

    * 내부에서 자바 로직을 처리함

> @Controller

    * 웹 요청과 응답을 처리함

> Repository

    * DB나 파일같은 외부 I/O 작업을 처리함

## LOMBOK

> @Getter and @Setter

    * Declare above class header

    * 아마 Lombok에서 가장 많이 사용되는 어노테이션.

        * 예를 들어, xxx라는 필드에 선언하면 자동으로 getXxx()(boolean 타입인 경우, isXxx())와 setXxx() 메소드를 생성해줍니다.

> @AllArgsConstructor

    * 생성자도 자동으로 생성할 수 있습니다.

    *  모든 필드 값을 파라미터로 받는 생성자를 만들어줍니다.

> @NoArgsConstructor

    * 파라미터가 없는 기본 생성자를 생성해줍니다.

> @RequiredArgsConstructor

    * final이나 @NonNull인 필드 값만 파라미터로 받는 생성자를 만들어줍니다.

> @ToString
> @Data

    * @Data는 위에서 설명드린 @Getter, @Setter, @RequiredArgsConstructor, @ToString, @EqualsAndHashCode을 한꺼번에 설정.

## JPA Annotations

    > @Entity

        * 데이터베이스에 저장하기 위해 유저가 정의한 클래스가 필요한데 그런 클래스를 Entity라고 한다

        * 일반적으로 RDBMS에서 Table을 객체화 시킨 것으로 보면 된다.

    > @Id

        * primary key를 가지는 변수를 선언하는 것을 뜻한다

        * The @Id annotation is mandatory for entities,

        * @GeneratedValue 어노테이션은 해당 Id 값을 어떻게 자동으로 생성할지 전략을 선택할 수 있다

    > @Table

        * 별도의 이름을 가진 데이터베이스 테이블과 매핑한다.

        * 기본적으로 @Entity로 선언된 클래스의 이름은 실제 데이터베이스의 테이블 명과 일치하는 것을 매핑한다.

        * 따라서 @Entity의 클래스명과 데이터베이스의 테이블명이 다를 경우에 @Table(name=" ")과 같은 형식을 사용해서 매핑이 가능하다.<br/>

    > @Column

        * @Column 선언이 꼭 필요한 것은 아니다.

        * 하지만 @Column에서 지정한 변수명과 데이터베이스의 컬럼명을 서로 다르게 주고 싶다면 @Column(name=" ") 같은 형식으로 작성하면 된다.

        * 그렇지 않은 경우에는 기본적으로 멤버 변수명과 일치하는 데이터베이스 컬럼을 매핑한다.

    > @OneToMany

        * EX) if one department can employ for several employees

    > @ManyToOne

        * 회원과 팀은 N:1 관계

        * many employees work in one department

        * Many readers live in one area.

        * Many subscriptions can be of one and the same reader.

    > @GeneratedValue (strategy , generator)

        * Generates Primary Key

        * Without specifying a @GeneratedValue annotation, entity identifiers must be assigned manually.

        * strategy:

            * GenerationType:

                * IDENTITY: allows using a table identity column, like the MySQL AUTO_INCREMENT.

                    * For JPA and Hibernate, you should prefer using SEQUENCE

                * SEQUENCE: allows using a database sequence object to generate identifier values.

                * TABLE: emulates the database sequence generator using a separate table.

        * generator

    > @SequenceGenerator(name ,sequenceName , allocationSize )

        * Allow you customize the sequence generation process

        * parameter

            * name: he generator attribute of the @GeneratedValue  references the name attribute of the @SequenceGenerator

            * sequence name: the name of the sequence in the DB

            * needs to be the same value that the DB sequence uses as its "auto increment", usually use 1<br/>

    > @Query

        * 쿼리메서드 외에 JPA정의에 따른 sql문을 작성하고 싶을때, 혹은 DB종속적인 native쿼리를 작성하고 싶을 때 사용하는 어노테이션

        * EX) @Query("SELECT b.bno, b.title, +"FROM Board b " + "LEF JOIN b.replies r WHERE b.bno > 0 GROUP BY b ")<br/>

    > @Transactional

        * 데이터베이스의 상태를 변경하는 작업 또는 한번에 수행되어야 하는 연산들을 의미한다.

        * @Transactional(rollbackFor = Exception.class)하면 자동 롤백처리 됨으로

    > @JoinColumn

        * 외래키를 맵핑할떄

    > @Component

        * Spring will autodetect these classes for dependency injection

        * @Component("classNameExample")

        > @Service
        > @Repository
        > @Controller

    > @Configuration

        * indicates that the class has @Bean definition methods.

        * @Configuration 을 적용하지 않고, @Bean 만 적용하면 어떻게 될까?

            * Configuration 을 붙이면 바이트코드를 조작하는 CGLIB 기술을 사용해서 싱글톤을 보장하지만, 만약 @Bean만 적용하면 보장불가(순수한 자바코드)

        * 파라메터 안에 원하는 빈 이름을 지정할 수 있다
    
    > @ComponentScan()

        * parameter: 
        
            * excludeFilters = @ComponentScan.Filter()

            * basePackages 스캔할 패키지를 정해준다.

        * componentScan은 configuration과 항상 함께온다

        * configuration는 이게 xml을 대체하는 성정파일인것을 알려주고, componentscan으로 등록한다

> @EqualsAndHashCode
> @NoArgsConstructor
> @Enuerated
> @RestController
> @RequestMapping
> @Autowired

## Testing Annotations

> @AutoConfigureTestDatabase
> @Rollback
