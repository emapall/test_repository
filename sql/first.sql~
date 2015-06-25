CREATE TABLE IF NOT EXISTS person(
ID_Person INT_UNSIGNED AUTO INCREMENT PRIMARY KEY,
Name VARCHAR[50],
Age INT_UNSIGNED NOT NULL, 
Sex CHAR 
);

INSERT INTO person(Name,Age,Sex) VALUES ("pippo",18,"m");
INSERT INTO person(Name,Age,Sex) VALUES ("cane",21,"f");
INSERT INTO person(Name,Age,Sex) VALUES ("as",221,"m");

CREATE TABLE IF NOT EXISTS pet(
id INT UNSIGNED AUTO INCREMENT PRIMARY KEY,
name VARCHAR[50],
age INT UNSIGNED NOT NULL,
race VARCHAR[50] 
);




INSERT INTO pet(name, age, race) VALUES ("came",200,"asdasds");
INSERT INTO per(name, age, race) VALUES ("bla",2,"border");

CREATE TABLE IF NOT EXISTS pet_man(
person_id INTEGER, 
pet_id INTEGER, 
FOREIGN KEY (person_id) REFERENCES (person.ID_person), 
FOREIGN KEY (pet_id) REFERENCES (pet.id) 
);
