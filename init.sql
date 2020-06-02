CREATE DATABASE Session;


CREATE TABLE `Session`.`EXAMS` (
 `Course Code` INT NOT NULL,
 `The Date` DATE NULL,
 `Discipline Code` INT NULL,
 `Rating` INT NULL,
 PRIMARY KEY (`Course Code`));


CREATE TABLE `Session`.`CADETS` (
 `Course Code` INT NOT NULL,
 `Surname` TEXT NULL,
 `Name` TEXT NULL,
 `Middle Name` TEXT NULL,
 `Course` INT NULL,
 `Group` TEXT NULL,
 PRIMARY KEY (`Course Code`));

 ALTER TABLE `Session`.`CADETS`
 CHANGE COLUMN `Course Code` `Course Code` INT NULL ,
 DROP PRIMARY KEY;
 ;
 
 ALTER TABLE `Session`.`EXAMS`
CHANGE COLUMN `Course Code` `Course Code` INT NULL ,
DROP PRIMARY KEY;
;



CREATE TABLE `Session`.`DISCIPLINES` (
 `Discipline Code` INT NOT NULL,
 `Discipline Name` TEXT NULL,
 `Number of Hours` INT NULL,
 PRIMARY KEY (`Discipline Code`));


CREATE TABLE `Session`.`OFFSETS` (
 `Course Code` INT NULL,
 `The Date` DATE NULL,
 `Discipline Code` INT NULL,
 `Offset` TINYINT NULL);
