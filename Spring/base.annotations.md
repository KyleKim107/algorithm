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

> @Entity

## Testing Annotations

> @AutoConfigureTestDatabase
> @Rollback
