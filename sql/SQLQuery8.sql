/*--------------------------------------------------------------
STEP A - CREATE STAGING TABLES
--------------------------------------------------------------*/

IF OBJECT_ID('dbo.Stg_Users', 'U') IS NOT NULL DROP TABLE Stg_Users;
CREATE TABLE Stg_Users (
    UserID              NVARCHAR(20),
    FirstName           NVARCHAR(50),
    LastName            NVARCHAR(50),
    Email               NVARCHAR(255),
    DateOfBirth         NVARCHAR(20),
    Gender              NVARCHAR(5),
    HeightCM            NVARCHAR(20),
    StartingWeightKG    NVARCHAR(20),
    GoalType            NVARCHAR(20)
);
 
IF OBJECT_ID('dbo.Stg_Workouts', 'U') IS NOT NULL DROP TABLE Stg_Workouts;
CREATE TABLE Stg_Workouts (
    WorkoutID       NVARCHAR(20),
    UserID          NVARCHAR(20),
    WorkoutDate     NVARCHAR(20),
    WorkoutType     NVARCHAR(50),
    DurationMinutes NVARCHAR(20)
);
 
IF OBJECT_ID('dbo.Stg_Diet', 'U') IS NOT NULL DROP TABLE Stg_Diet;
CREATE TABLE Stg_Diet (
    MealID              NVARCHAR(20),
    UserID              NVARCHAR(20),
    MealDate            NVARCHAR(20),
    MealType            NVARCHAR(20),
    CaloriesConsumed    NVARCHAR(20),
    ProteinG            NVARCHAR(20),
    CarbsG              NVARCHAR(20),
    FatG                NVARCHAR(20)
);
 
IF OBJECT_ID('dbo.Stg_Sleep', 'U') IS NOT NULL DROP TABLE Stg_Sleep;
CREATE TABLE Stg_Sleep (
    SleepID         NVARCHAR(20),
    UserID          NVARCHAR(20),
    SleepDate       NVARCHAR(20),
    SleepStart      NVARCHAR(30),
    SleepEnd        NVARCHAR(30),
    DurationMinutes NVARCHAR(20),   -- present in CSV, but computed in production table -> excluded in Step C
    SleepQuality    NVARCHAR(10)
);
 
IF OBJECT_ID('dbo.Stg_Weight', 'U') IS NOT NULL DROP TABLE Stg_Weight;
CREATE TABLE Stg_Weight (
    ProgressID      NVARCHAR(20),
    UserID          NVARCHAR(20),
    ProgressDate    NVARCHAR(20),
    WeightKG        NVARCHAR(20)
);
GO

IF OBJECT_ID('dbo.Diet', 'U') IS NULL
BEGIN
    CREATE TABLE Diet (
        MealID           INT PRIMARY KEY,
        UserID           INT NOT NULL,
        MealDate         DATE NOT NULL,
        MealType         NVARCHAR(20) NOT NULL,
        CaloriesConsumed INT NOT NULL,
        ProteinG         DECIMAL(6,1) NULL,
        CarbsG           DECIMAL(6,1) NULL,
        FatG             DECIMAL(6,1) NULL,

        CONSTRAINT FK_Diet_Users
            FOREIGN KEY (UserID)
            REFERENCES Users(UserID)
            ON DELETE CASCADE
    );
END;

BULK INSERT Stg_Users
FROM 'C:\ImportData\users.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK,
    MAXERRORS = 50
);

SELECT COUNT(*) AS TotalUsers
FROM Stg_Users;

BULK INSERT Stg_Workouts
FROM 'C:\ImportData\workouts.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK,
    MAXERRORS = 50
);

SELECT COUNT(*) AS TotalWorkouts
FROM Stg_Workouts;

BULK INSERT Stg_Diet
FROM 'C:\ImportData\diet.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK,
    MAXERRORS = 50
);

SELECT COUNT(*) AS TotalDiet
FROM Stg_Diet;

BULK INSERT Stg_Sleep
FROM 'C:\ImportData\sleep.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK,
    MAXERRORS = 50
);

SELECT COUNT(*) AS TotalSleep
FROM Stg_Sleep;

BULK INSERT Stg_Weight
FROM 'C:\ImportData\weight.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK,
    MAXERRORS = 50
);

SELECT COUNT(*) AS TotalWeight
FROM Stg_Weight;

SELECT 'Users' AS TableName, COUNT(*) AS Rows FROM Stg_Users
UNION ALL
SELECT 'Workouts', COUNT(*) FROM Stg_Workouts
UNION ALL
SELECT 'Diet', COUNT(*) FROM Stg_Diet
UNION ALL
SELECT 'Sleep', COUNT(*) FROM Stg_Sleep
UNION ALL
SELECT 'Weight', COUNT(*) FROM Stg_Weight;

SELECT COUNT(*) AS StgUsers FROM Stg_Users;
SELECT COUNT(*) AS ProdUsers FROM Users;


--Production Load
SET IDENTITY_INSERT Users ON;

INSERT INTO Users
(
    UserID,
    FirstName,
    LastName,
    Email,
    PasswordHash,
    DateOfBirth,
    Gender,
    HeightCM
)
SELECT
    CAST(UserID AS INT),
    FirstName,
    LastName,
    Email,
    CAST('placeholder' AS VARBINARY(256)),
    CAST(DateOfBirth AS DATE),
    Gender,
    CAST(HeightCM AS DECIMAL(5,2))
FROM Stg_Users;

SET IDENTITY_INSERT Users OFF;

SELECT COUNT(*) AS TotalUsers
FROM Users;

SET IDENTITY_INSERT Workouts ON;

INSERT INTO Workouts
(
    WorkoutID,
    UserID,
    WorkoutDate,
    WorkoutType,
    DurationMinutes
)
SELECT
    CAST(REPLACE(WorkoutID, CHAR(13), '') AS INT),
    CAST(REPLACE(UserID, CHAR(13), '') AS INT),
    CAST(WorkoutDate AS DATE),
    WorkoutType,
    CAST(TRIM(REPLACE(DurationMinutes, CHAR(13), '')) AS INT)
FROM Stg_Workouts;

SET IDENTITY_INSERT Workouts OFF;


INSERT INTO Diet
(
    MealID,
    UserID,
    MealDate,
    MealType,
    CaloriesConsumed,
    ProteinG,
    CarbsG,
    FatG
)
SELECT
    CAST(REPLACE(MealID, CHAR(13), '') AS INT),
    CAST(REPLACE(UserID, CHAR(13), '') AS INT),
    CAST(MealDate AS DATE),
    MealType,
    CAST(TRIM(REPLACE(CaloriesConsumed, CHAR(13), '')) AS INT),
    CAST(TRIM(REPLACE(ProteinG, CHAR(13), '')) AS DECIMAL(6,1)),
    CAST(TRIM(REPLACE(CarbsG, CHAR(13), '')) AS DECIMAL(6,1)),
    CAST(TRIM(REPLACE(FatG, CHAR(13), '')) AS DECIMAL(6,1))
FROM Stg_Diet;

SELECT COUNT(*) AS TotalDiet
FROM Diet;


SET IDENTITY_INSERT Sleep ON;

INSERT INTO Sleep
(
    SleepID,
    UserID,
    SleepDate,
    SleepStart,
    SleepEnd,
    SleepQuality
)
SELECT
    CAST(REPLACE(SleepID, CHAR(13), '') AS INT),
    CAST(REPLACE(UserID, CHAR(13), '') AS INT),
    CAST(SleepDate AS DATE),
    CAST(SleepStart AS DATETIME2),
    CAST(SleepEnd AS DATETIME2),
    CAST(TRIM(REPLACE(SleepQuality, CHAR(13), '')) AS TINYINT)
FROM Stg_Sleep;

SET IDENTITY_INSERT Sleep OFF;

SELECT COUNT(*) AS TotalSleep
FROM Sleep;


SET IDENTITY_INSERT DailyProgress ON;

INSERT INTO DailyProgress
(
    ProgressID,
    UserID,
    ProgressDate,
    WeightKG
)
SELECT
    CAST(REPLACE(ProgressID, CHAR(13), '') AS INT),
    CAST(REPLACE(UserID, CHAR(13), '') AS INT),
    CAST(ProgressDate AS DATE),
    CAST(TRIM(REPLACE(WeightKG, CHAR(13), '')) AS DECIMAL(5,2))
FROM Stg_Weight;

SET IDENTITY_INSERT DailyProgress OFF;

SELECT COUNT(*) AS TotalProgress
FROM DailyProgress;

SELECT 'Users' AS TableName, COUNT(*) AS TotalRows FROM Users
UNION ALL
SELECT 'Workouts', COUNT(*) FROM Workouts
UNION ALL
SELECT 'Diet', COUNT(*) FROM Diet
UNION ALL
SELECT 'Sleep', COUNT(*) FROM Sleep
UNION ALL
SELECT 'DailyProgress', COUNT(*) FROM DailyProgress;


TRUNCATE TABLE Stg_Users;
TRUNCATE TABLE Stg_Workouts;
TRUNCATE TABLE Stg_Diet;
TRUNCATE TABLE Stg_Sleep;
TRUNCATE TABLE Stg_Weight;


SELECT COUNT(*) AS Users FROM Stg_Users;
SELECT COUNT(*) AS Workouts FROM Stg_Workouts;
SELECT COUNT(*) AS Diet FROM Stg_Diet;
SELECT COUNT(*) AS Sleep FROM Stg_Sleep;
SELECT COUNT(*) AS Weight FROM Stg_Weight;


sp_help Diet;
GO

sp_help Sleep;
GO

sp_help DailyProgress;
GO

sp_help Workouts;
GO

sp_help Users;
GO

CREATE NONCLUSTERED INDEX IX_Diet_User_Date
ON Diet (UserID, MealDate)
INCLUDE (CaloriesConsumed, ProteinG, CarbsG, FatG);

CREATE NONCLUSTERED INDEX IX_Sleep_User_Date
ON Sleep (UserID, SleepDate)
INCLUDE (DurationMinutes, SleepQuality);

CREATE NONCLUSTERED INDEX IX_DailyProgress_User_Date
ON DailyProgress (UserID, ProgressDate)
INCLUDE (WeightKG);

CREATE NONCLUSTERED INDEX IX_Workouts_User_Date_Covering
ON Workouts (UserID, WorkoutDate)
INCLUDE (WorkoutType, DurationMinutes);


EXEC sp_helpindex 'Users';


SELECT 'Users' AS TableName, COUNT(*) AS TotalRows FROM Users
UNION ALL SELECT 'Workouts', COUNT(*) FROM Workouts
UNION ALL SELECT 'Diet', COUNT(*) FROM Diet
UNION ALL SELECT 'Sleep', COUNT(*) FROM Sleep
UNION ALL SELECT 'DailyProgress', COUNT(*) FROM DailyProgress;