--  2 запрос
select * from Session.EXAMS;
-- 3 запрос
SELECT `Name`, `Surname`,`Middle Name`, `Course`, `Session`.`EXAMS`.`Rating`
FROM `Session`.`CADETS` INNER JOIN  `Session`.`EXAMS`
ON  `Session`.`CADETS`.`Course Code` =  `Session`.`EXAMS`.`Course Code`
WHERE `Session`.`EXAMS`.`Rating` > 3
-- 4 запрос
SELECT `Name`, `Surname`,`Middle Name`, `Course`, if(`Session`.`OFFSETS`.`Offset`, 'Сдал', 'Не сдал') as Зачёт
FROM `Session`.`CADETS` INNER JOIN  `Session`.`OFFSETS`
ON  `Session`.`CADETS`.`Course Code` = `Session`.`OFFSETS`.`Course Code`;
