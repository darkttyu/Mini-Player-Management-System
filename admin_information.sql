SELECT * FROM PLAYER;
SELECT * FROM ROLE;
SELECT * FROM TEAM;
SELECT * FROM COACH;
SELECT * FROM PLAYER_PERFORMANCE;
SELECT * FROM ADMIN;

DROP TABLE PLAYER;
DROP TABLE TEAM;
DROP TABLE COACH;
DROP TABLE PLAYER_PERFORMANCE;

-- Creating Player Table

CREATE TABLE player (
  playerName VARCHAR(20) NOT NULL,
  pFName VARCHAR(20) NULL,
  pLName VARCHAR(45) NULL,
  age INT NULL,
  role_ID INT NULL,
  team_ID INT NULL,
  PRIMARY KEY (`playerName`));

-- Creating Table Role 
CREATE TABLE role (
  role_ID INT NOT NULL,
  roleName VARCHAR(10) NULL,
  PRIMARY KEY (role_ID));
  
-- Creating Team Table
CREATE TABLE team (
  team_ID INT NOT NULL,
  teamName VARCHAR(20) NULL,
  recent_match VARCHAR(20) NULL,
  coachName VARCHAR(20) NULL,
  PRIMARY KEY (team_ID));

-- Creating Coach Table

CREATE TABLE COACH (
coach_ID INT NOT NULL, 
coachName VARCHAR(20),
coachFName VARCHAR(20),
coachLName VARCHAR(20),
PRIMARY KEY (coach_ID));

-- Team Insert
INSERT INTO TEAM (team_ID, teamName, recent_match, coach_ID)
VALUES 
	(1, 'SK Telecom', 'Generation Gaming', 1),
	(2, 'Bilibili Gaming', 'Weibo Gaming', 2);

-- Coach Insert
INSERT INTO COACH (coach_ID, coachName, coachFName, coachLName)
VALUES 
	(1, 'Kkoma', 'Jeong-gyun', 'Kim'),
    (2, 'BigWei', 'Chien-Wei', 'Fu');
    
-- Role Insert
INSERT INTO ROLE (role_id, roleName)
VALUES 
	(1, 'Top'),
    (2, 'Jungle'),
    (3, 'Mid'),
    (4, 'Bottom'),
    (5, 'Support');
    
INSERT INTO PLAYER (playerName, pFname, pLName, age, role_ID, team_ID)
VALUES
	('faker', 'Sang-hyeok', 'Lee', 28, 3, 1),
    ('Zeus', 'Woo-je', 'Choi', 20, 1, 1),
    ('Keria', 'Min-seok', 'Ryu', 21, 5, 1),
    ('Oner', 'Hyeon-jun', 'Mun', 21, 2, 1),
    ('Gumayusi', 'Min-hyeong', 'Lee', 22, 4, 1),
    ('Bin', 'Ze-Bin', 'Chen', 20, 1, 2),
    ('Xun', 'Li-Xun', 'Peng', 22, 2, 2),
    ('knight', 'Ding', 'Zhuo', 24, 3, 2),
    ('Elk', 'Jia-Hao', 'Zhao', 22, 4, 2),
    ('ON', 'Wen-Jun', 'Luo', 21, 5, 2);

INSERT INTO PLAYER_PERFORMANCE (playerName, year, games_played, most_used, win_rate, player_participation)
VALUES ('faker', 2023, 157, 'Azir', 80.56, 92.25),
	('Zeus', 2022, 212, 'K''Sante', 70.10, 86.36),
    ('Zeus', 2023, 144, 'Aatrox', 95.69, 93.45),
    ('Keria', 2023, 216,  'Bard', 92.87, 92.75),
    ('Oner', 2022, 209, 'Lee Sin', 86.32, 88.32),
    ('Oner', 2022, 169, 'Rell', 80.26, 81.30),
    ('Gumayusi', 2022, 193, 'Lucian', 93.24, 77.65),
    ('Gumayusi', 2023, 148, 'Jhin', 87.23, 82.74),
    ('Bin', 2022, 229, 'Jax', 93.56, 78.89),
    ('Bin', 2023, 120, 'Renekton', 76.38, 82.46),
    ('Xun', 2023, 236, 'Kindred', 96.87, 94.23),
    ('knight', 2023, 191, 'Orianna', 86.32, 91.65),
    ('Elk', 2022, 163, 'Aphelios', 86.98, 93.62),
    ('Elk', 2023, 153, 'Varus', 92.34, 82.59),
    ('ON', 2023, 194, 'Rakan', 82.24, 79.65);
  
INSERT INTO ADMIN (admin_user, password)
VALUES ('hatdog', 1234567890);

