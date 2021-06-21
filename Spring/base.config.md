# Config

* spring.jpa.hibernate.ddl-auto = parameter

  * none: 아무것도 실행하지 않는다 (대부분의 DB에서 기본값이다)

  * create-drop: SessionFactory가 시작될 때 drop및 생성을 실행하고, SessionFactory가 종료될 때 drop을 실행한다 (in-memory DB의 경우 기본값이다)

  * create: SessionFactory가 시작될 때 데이터베이스 drop을 실행하고 생성된 DDL을 실행한다

  * update: 변경된 스키마를 적용한다

  * validate: 변경된 스키마가 있다면 변경점을 출력하고 애플리케이션을 종료한다
