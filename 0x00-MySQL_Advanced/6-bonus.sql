-- script that creates a stored procedure AddBonus having a new correction for a student

-- creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT)
BEGIN
    DECLARE project_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, project_id, score);
END
$$
DELIMITER ;


-- DELIMITER $$
-- CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
-- BEGIN
--	INSERT INTO projects(name)
--	SELECT project_name FROM DUAL
--	WHERE NOT EXISTS(SELECT * FROM projects WHERE name = project_name LIMIT 1);
--
--	INSERT INTO corrections(user_id, project_id score)
--	VALUES (
--	user_id,
--	(SELECT id FROM projects WHERE name = project_name),
--	score);
-- END $$
-- DELIMITER;
