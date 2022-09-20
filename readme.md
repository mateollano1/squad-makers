# Backend SquadMakers
CHALLENGE - Jokes

Creado por: Mateo Llano Avendaño

Ejecución del aplicativo:
1. Creación red docker
```sh
docker network create squadmakers
```
2. Ejecución Docker compose
```sh
docker-compose -f docker/Docker-compose.dev.yml up --build
```

Arquitectura propuesta:

Preguntas planteadas:


 1. ¿Qué repositorio utilizaras?

        Al momento de escoger que tipo de base de datos utilizar, se deben tener en cuenta varios factores, en este caso el problema planteado se presta para darle diferentes enfoques. En mi caso opto por una base de datos relacional tipo postgres ya que me imagino que el problema planteado puede tener una ampliabilidad a futuro para almacenar usuarios, que a su vez pueden tener roles, los cuales representarian realciones en nuestras tablas y una SQL podria tener un mejor rendimiento para este tipo de casos. Finalmente dentro de las SQL se opta por postgres debido al buen manejo de concurrencia que maneja que la hace una base de datos robusta.


2. Sentencia SQL
```sh
    CREATE DATABASE squad;

    CREATE TABLE `users` (
        `id` INT(20) NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(255),
        `username` VARCHAR(255) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        `created_at` DATETIME(20),
        `last_modified` DATETIME(20),
        PRIMARY KEY (`id`)
    );

    CREATE TABLE `jokes` (
        `id` INT(20) NOT NULL AUTO_INCREMENT,
        `joke_text` VARCHAR(255),
        `user_id` INT(20),
        `created_at` DATETIME(20),
        `last_modified` DATETIME(20),
        FOREIGN KEY(user_id) REFERENCES users(id) PRIMARY KEY (`id`)
```
3. Sentencia NoSQL

```sh
    use squad db.user.insert(
        { joke_text: "",
        username: "",
        kind_joke: "" }
    )
```
