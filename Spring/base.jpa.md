# JPA

    > Create DB based on extended repository interface

    * EX)

    * public interface AppUserRepository extends JpaRepository<AppUser, Long> { // Long for Id

        * Jpa create a DB based on AppUser class variables

            * AppUser class should have @Entity Annotation
