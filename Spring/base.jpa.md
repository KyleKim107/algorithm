# JPA

    > Create DB based on extended repository interface

    * EX)

    * public interface AppUserRepository extends JpaRepository<AppUser, Long> // Long for Id

        * JpaRepository를 상속받을 때는 사용될 Entity 클래스와 ID 값이 들어가게 된다. 즉, JpaRepository<T, ID> 가 된다.

        * Jpa create a DB based on AppUser class variables

            * AppUser class should have @Entity Annotation

        * JpaRepository를  단순하게 상속하는 것만으로 위의 인터페이스는 Entity 하나에 대해서 아래와 같은 기능을 제공하게 된다.

            * save(): 레코드 저장 (insert, update)

            * findOne(): primary key로 레코드 한건 찾기

            * count(): 전체 레코드 불러오기. 정렬(sort), 페이징(pageable) 가능

            * findAll(): 레코드 갯수

            *  delete(): 레코드 삭제

    > @Query

        * named parameter mapping

> JpaRepository< Employee , Long>
