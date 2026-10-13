USE AI_Fitness_DB;
GO

/*--------------------------------------------------------------
STEP C - LOAD USERS
--------------------------------------------------------------*/

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
GO

SELECT COUNT(*) AS TotalUsers
FROM Users;

/*--------------------------------------------------------------
STEP D - LOAD WORKOUTS
--------------------------------------------------------------*/

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
GO

SELECT COUNT(*) AS TotalWorkouts
FROM Workouts;

/*--------------------------------------------------------------
STEP E - LOAD DIET
--------------------------------------------------------------*/

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
GO

SELECT COUNT(*) AS TotalDiet
FROM Diet;

/*--------------------------------------------------------------
STEP F - LOAD SLEEP
--------------------------------------------------------------*/

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
GO

SELECT COUNT(*) AS TotalSleep
FROM Sleep;

/*--------------------------------------------------------------
STEP G - LOAD DAILY PROGRESS
--------------------------------------------------------------*/

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
GO

SELECT COUNT(*) AS TotalProgress
FROM DailyProgress;

/*--------------------------------------------------------------
STEP H - CLEAN STAGING TABLES
--------------------------------------------------------------*/

TRUNCATE TABLE Stg_Users;
TRUNCATE TABLE Stg_Workouts;
TRUNCATE TABLE Stg_Diet;
TRUNCATE TABLE Stg_Sleep;
TRUNCATE TABLE Stg_Weight;
GO

SELECT COUNT(*) AS Users FROM Stg_Users;
SELECT COUNT(*) AS Workouts FROM Stg_Workouts;
SELECT COUNT(*) AS Diet FROM Stg_Diet;
SELECT COUNT(*) AS Sleep FROM Stg_Sleep;
SELECT COUNT(*) AS Weight FROM Stg_Weight;