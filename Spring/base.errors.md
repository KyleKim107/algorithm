# Errors

> Cannot resolve symbol 'assertThat'

    * import static org.assertj.core.api.Assertions.assertThat;  //자동 import되지 않음

> java.sql.SQLException: Access denied for user 'root'@'localhost' (using password: YES)

    * Go to Application.Property file, then input spring.datasource.password= your password without double quot!!

> Dependency 'org.webjars:bootstrap not found

    * Reload Maven or Gradle dependency

> org.hibernate.MappingException: Repeated column in mapping for entity:

    * That means you mapped the same database column twice

## Network Error

    * Port 8080 was already in use.

        * First off, you may be already running the app

        * otherwise check Activity Monitor so that you can check which process using port 8080

        * If the method above does not work, Kill the port listener with the command "lsof -n -i4TCP:8080" on Terminal
