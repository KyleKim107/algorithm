# java Syntex

{% tabs %}
{% tab title='java.md' %}
> Get input
> object of length

* String

  * String.length()

```java

String.length()

```

{% endtab %}
{% endtabs %}

> Serializable

* Implements Serializable (interface)  enable the class serializable.

* 필드 선언에 static이나 transient가 붙어있으면 직렬화 불가, 생성자와 메서드는 포함 X

> ObjectInputStream

* ObjectOutputStream : 객체 직렬화 역할

  * 객체 직렬화 하려면 writeObject()메서드를 사용.

  * oos.writeObject(객체);

> new FileInputStream

* ObjectInputStream : 역직렬화 역할

  * 역직렬화를 하려면 readObject()메서드 사용.

  * 객체타입 변수 = (객체타입) ois.readObject();
