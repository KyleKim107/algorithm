# Errors

> Cannot resolve symbol 'assertThat'

    * import static org.assertj.core.api.Assertions.assertThat;  //자동 import되지 않음

> java.sql.SQLException: Access denied for user 'root'@'localhost' (using password: YES)

    * Go to Application.Property file, then input spring.datasource.password= your password without double quot!!
