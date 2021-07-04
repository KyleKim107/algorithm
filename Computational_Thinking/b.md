# Java Introduction

* 자바는 분산처리에 유리하다

  * Tcp/IP 네트워크 기능 예장

  * Http/Ftp등과 같은 프로토콜 쉽게 사용 가능

* 자바는 인터프리터에 의해 실행됨

  * java -> javac (컴파일)-> .class (중간언어) -> interpreting (기계어) -> 실행

  * 자바는 견고하다

    * 포인터 사용 X, 가비지 컬렉터 사용, 데이터 타입 검수
  
  * 자바는 안전하다

    * 분산데이터에도 사용되기에 안전함

    * ![자바](images/20210704_233515.png)
  
  * 자바는 플랫폼 독립적이다

    ![java2](images/20210704_233603.png)

  * 높은 성능 제공

    * 가비지 컬렉터가 메모리 과용 방지

  * 멀티 뜨레드 제공

    * 스레드 : 독자적으로 수행하는 하나의 프로그램

    * 멀트 뜨레드: 한번에 여러개의 뜨레드가 동시에 수행됨

    * 하나의 CPU가 여러개의 프로그램을 동시에 수행하도록함 -> 수행속도를 빠르게함

  * 자바는 동적이다

    * 변화되는 환경에 잘 적응됨

    * 프로그램 사이에 사용되는 라이브러리를 실행시간에 수행함 -> 변화를 곧바로 적용할 수 있음

> 자바 플렛폼 종류

* JDK

  * SE (Standard Edition)

    * 가장 기본이 되는 에디션 대부분의 패키기자 포함

  * EE (Enterprise Edition)

    * gusdjqdptj tkdydehlsms API

  * ME (Micro edition)

    * 모바일 기기에 사용되는 API 포함된 에디션

> 자바 플렛폼 구조

* 자바 프로그램 -> 자바 VM -> 다양한 하드웨어 플랫폼

  * 자바 VM

    * 다른 OS들에서 프로그램이 돌아 갈 수 있도록 해야해

    * 대신 OS에 맞는 자바를 설치 해줘야 한다

* 자바 API

  * 프로그래머들이 필요로 하는 기본적 클래스들을 거대한 라이브러리로 미리 만들어 제공한다

  * 이런것들을 표준 클래스라함

  ![스탠다드](images/20210704_234745.png)

> 자바 개발환경

* 자바 디벨로퍼 킷 제공

  * SRE: Java Runtime Environment, 환경설정해줌, 이것만으로 프로그램을 컴파일 할 수 없다.

  * JDK: 개발과 실행에 필요한 모든 기능들이 들어가 있음

* 이클립스

  * 실시간 문법 체크

  * 디버깅 기능

  * 소스 자동생성

  * 사용이 용이한 인터페이스 구성

  * 워크 스페이스: 모든 프로젝트를 이 디렉토리 안에 둠

> 자바소스파일

* public: 자바 예약어로서 FirstClass.java 파일의 클래스를 외부에 공개함

* 주석문: // and /******/ (java doc type) and /******/

* compile: javac AppName.java 클래스 파일 생성

* run:  java AppName

> 입출력

* java.io

> 식별자

* 첫글자 대문자/ 특수문자 사용불가(!,@,#,%,&,*) /숫자사용 가능 하지만 첫문자 불가/ 예약어 포함가능, 하지만 예약어만 사용 불가

* 상수는 대문자

> 예약어

* 예약어는 보통 소문자다!

* const, goto, sizeof 예약어는 더는 사용안함

> 자바 데이터 타입

* boolean: 1 bit lowercase true or false

* char: 2 bytes

  * use '\u0000' ~ '\uffff'

* Integer

  * byte: 1 byte

    * 범위: -2^7 ~ 2^7 -1

  * short: 2 byte

    * 범위: -2^15 ~ 2^15 -1

  * int: 4 byte

    * 범위: -2^31 ~ 2^31 -1 (-2147483647~2147483647)

    * 023 -> 8진법 / 0xBAAC -> 16진법

  * long: 8 bytes. put l or L end of numbers

    * 범위: -2^63 ~ 2^63 -1

> 실수

* float: 4 byte

* double: 8 bytes

  * 1.718F - float 형의 실수

  * 6.02E23 - 큰실수

> 형변환

* 작은 데이터에서 큰 데이터 - promotion 묵시적

  * 4byte의 int에서 8byte의 double형으로 가능

  * ex) int age= 26
  
  * double avgAge = age(형변환)

  ![묵시적](images/20210705_011419.png)

* 큰데이터에서 작은 데이터로 - demotion 명시적

  * 데이터 축소후에도 값을 온전히 가질 수 있어야해

  * ex) int sum = 128;

  * byte data = (byte) sum; // b에 -128할당

  ![ex](images/20210705_012051.png)
