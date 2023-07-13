-- script that creates a table of users
CREATE IF NOT EXISTS users (
	id INT NOT NULL AUTO INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR (255),
	country ENUM('US', 'CO', 'TN') NOT NULL
);
