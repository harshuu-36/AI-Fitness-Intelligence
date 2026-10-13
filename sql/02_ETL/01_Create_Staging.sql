USE AI_Fitness_DB;
GO

/*--------------------------------------------------------------
STEP A - CREATE STAGING TABLES
--------------------------------------------------------------*/

IF OBJECT_ID('dbo.Stg_Users', 'U') IS NOT NULL
    DROP TABLE dbo.Stg_Users;

CREATE TABLE dbo.Stg_Users
(
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

IF OBJECT_ID('dbo.Stg_Workouts', 'U') IS NOT NULL
    DROP TABLE dbo.Stg_Workouts;

CREATE TABLE dbo.Stg_Workouts
(
    WorkoutID           NVARCHAR(20),
    UserID              NVARCHAR(20),
    WorkoutDate         NVARCHAR(20),
    WorkoutType         NVARCHAR(50),
    DurationMinutes     NVARCHAR(20)
);

IF OBJECT_ID('dbo.Stg_Diet', 'U') IS NOT NULL
    DROP TABLE dbo.Stg_Diet;

CREATE TABLE dbo.Stg_Diet
(
    MealID              NVARCHAR(20),
    UserID              NVARCHAR(20),
    MealDate            NVARCHAR(20),
    MealType            NVARCHAR(20),
    CaloriesConsumed    NVARCHAR(20),
    ProteinG            NVARCHAR(20),
    CarbsG              NVARCHAR(20),
    FatG                NVARCHAR(20)
);

IF OBJECT_ID('dbo.Stg_Sleep', 'U') IS NOT NULL
    DROP TABLE dbo.Stg_Sleep;

CREATE TABLE dbo.Stg_Sleep
(
    SleepID             NVARCHAR(20),
    UserID              NVARCHAR(20),
    SleepDate           NVARCHAR(20),
    SleepStart          NVARCHAR(30),
    SleepEnd            NVARCHAR(30),
    DurationMinutes     NVARCHAR(20),
    SleepQuality        NVARCHAR(10)
);

IF OBJECT_ID('dbo.Stg_Weight', 'U') IS NOT NULL
    DROP TABLE dbo.Stg_Weight;

CREATE TABLE dbo.Stg_Weight
(
    ProgressID          NVARCHAR(20),
    UserID              NVARCHAR(20),
    ProgressDate        NVARCHAR(20),
    WeightKG            NVARCHAR(20)
);
GO