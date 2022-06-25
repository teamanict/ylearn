CREATE DATABASE students;
CREATE TABLE `parents` (
    `Username` VARCHAR NOT NULL , 
    `Name` VARCHAR NOT NULL , 
    `Email` VARCHAR NOT NULL , 
    `Children` JSON NOT NULL , 
    `DOS` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    `Pass` VARCHAR NOT NULL , 
    PRIMARY KEY (`Username`));

INSERT INTO parents (
    Username, Name, Email, Children, Pass
) VALUES (
                        'passkey',
                        '2000-01-01 00:00:00',
                        3,
                        'email',
                        'Cedrick',
                        'scjstyles'
                    );

 CREATE TABLE children (
    Username         VARCHAR     PRIMARY KEY
                                 UNIQUE
                                 NOT NULL,
    Name             VARCHAR     NOT NULL,
    Class            INTEGER (1) NOT NULL,
    DOB              DATE        NOT NULL,
    Gender           BOOLEAN     NOT NULL,
    Parent           VARCHAR     NOT NULL
                                 REFERENCES parents (Username) ON UPDATE NO ACTION,
    Profile_Pictutre VARCHAR
);