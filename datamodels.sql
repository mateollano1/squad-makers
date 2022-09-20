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
    FOREIGN KEY(user_id) REFERENCES users(id)
	PRIMARY KEY (`id`)
);
