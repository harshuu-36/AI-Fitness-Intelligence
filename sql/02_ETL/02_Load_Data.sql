/*
==============================================================================
Project    : AI Fitness Intelligence Platform

Phase      : 02 - Python Analytics

Module     : 02_ETL

File       : 02_Load_Data.sql

Author     : Harsh

Description:
Load all generated CSV files into SQL Server staging tables.

==============================================================================
*/

USE AI_Fitness_DB;
GO

/*=============================================================================
BULK INSERT : USERS
=============================================================================*/

BULK INSERT dbo.Stg_Users
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
GO

SELECT COUNT(*) AS TotalUsers
FROM dbo.Stg_Users;
GO

/*=============================================================================
BULK INSERT : WORKOUTS
=============================================================================*/

BULK INSERT dbo.Stg_Workouts
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
GO

SELECT COUNT(*) AS TotalWorkouts
FROM dbo.Stg_Workouts;
GO

/*=============================================================================
BULK INSERT : DIET
=============================================================================*/

BULK INSERT dbo.Stg_Diet
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
GO

SELECT COUNT(*) AS TotalDiet
FROM dbo.Stg_Diet;
GO

/*=============================================================================
BULK INSERT : SLEEP
=============================================================================*/

BULK INSERT dbo.Stg_Sleep
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
GO

SELECT COUNT(*) AS TotalSleep
FROM dbo.Stg_Sleep;
GO

/*=============================================================================
BULK INSERT : DAILY PROGRESS
=============================================================================*/

BULK INSERT dbo.Stg_Weight
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
GO

SELECT COUNT(*) AS TotalWeight
FROM dbo.Stg_Weight;
GO

/*=============================================================================
BULK INSERT : FOOD ITEMS
=============================================================================*/

BULK INSERT dbo.Stg_FoodItems
FROM 'C:\ImportData\fooditems.csv'
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
GO

SELECT COUNT(*) AS TotalFoodItems
FROM dbo.Stg_FoodItems;
GO

/*=============================================================================
BULK INSERT : MEALS
=============================================================================*/

BULK INSERT dbo.Stg_Meals
FROM 'C:\ImportData\meals.csv'
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
GO

SELECT COUNT(*) AS TotalMeals
FROM dbo.Stg_Meals;
GO

/*=============================================================================
BULK INSERT : MEAL ITEMS
=============================================================================*/

BULK INSERT dbo.Stg_MealItems
FROM 'C:\ImportData\mealitems.csv'
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
GO

SELECT COUNT(*) AS TotalMealItems
FROM dbo.Stg_MealItems;
GO

/*=============================================================================
VERIFY STAGING DATA
=============================================================================*/

SELECT 'Users' AS TableName, COUNT(*) AS TotalRows
FROM dbo.Stg_Users

UNION ALL

SELECT 'Workouts', COUNT(*)
FROM dbo.Stg_Workouts

UNION ALL

SELECT 'Diet', COUNT(*)
FROM dbo.Stg_Diet

UNION ALL

SELECT 'Sleep', COUNT(*)
FROM dbo.Stg_Sleep

UNION ALL

SELECT 'DailyProgress', COUNT(*)
FROM dbo.Stg_Weight

UNION ALL

SELECT 'FoodItems', COUNT(*)
FROM dbo.Stg_FoodItems

UNION ALL

SELECT 'Meals', COUNT(*)
FROM dbo.Stg_Meals

UNION ALL

SELECT 'MealItems', COUNT(*)
FROM dbo.Stg_MealItems;
GO



/*=============================================================================
PRODUCTION LOAD : USERS
=============================================================================*/

SET IDENTITY_INSERT dbo.Users ON;
GO

INSERT INTO dbo.Users
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
    TRY_CONVERT(INT, UserID),
    FirstName,
    LastName,
    Email,
    CAST('placeholder' AS VARBINARY(256)),
    TRY_CONVERT(DATE, DateOfBirth),
    Gender,
    TRY_CONVERT(DECIMAL(5,2), HeightCM)
FROM dbo.Stg_Users;

GO

SET IDENTITY_INSERT dbo.Users OFF;
GO

SELECT COUNT(*) AS TotalUsers
FROM dbo.Users;
GO


/*=============================================================================
PRODUCTION LOAD : WORKOUTS
=============================================================================*/

SET IDENTITY_INSERT dbo.Workouts ON;
GO

INSERT INTO dbo.Workouts
(
    WorkoutID,
    UserID,
    WorkoutDate,
    WorkoutType,
    DurationMinutes
)
SELECT
    TRY_CONVERT(INT, REPLACE(WorkoutID, CHAR(13), '')),
    TRY_CONVERT(INT, REPLACE(UserID, CHAR(13), '')),
    TRY_CONVERT(DATE, WorkoutDate),
    WorkoutType,
    TRY_CONVERT(INT,
        LTRIM(RTRIM(
            REPLACE(REPLACE(DurationMinutes, CHAR(13), ''), CHAR(10), '')
        ))
    )
FROM dbo.Stg_Workouts;

GO

SET IDENTITY_INSERT dbo.Workouts OFF;
GO

SELECT COUNT(*) AS TotalWorkouts
FROM dbo.Workouts;
GO


/*=============================================================================
PRODUCTION LOAD : DIET
=============================================================================*/

INSERT INTO dbo.Diet
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
    TRY_CONVERT(INT, MealID),
    TRY_CONVERT(INT, UserID),
    TRY_CONVERT(DATE, MealDate),
    MealType,
    TRY_CONVERT(INT, CaloriesConsumed),
    TRY_PARSE(ProteinG AS DECIMAL(6,1)),
    TRY_PARSE(CarbsG AS DECIMAL(6,1)),
    TRY_PARSE(FatG AS DECIMAL(6,1))
FROM dbo.Stg_Diet;

GO

SELECT COUNT(*) AS TotalDiet
FROM dbo.Diet;
GO


/*=============================================================================
PRODUCTION LOAD : SLEEP
=============================================================================*/

SET IDENTITY_INSERT dbo.Sleep ON;
GO

INSERT INTO dbo.Sleep
(
    SleepID,
    UserID,
    SleepDate,
    SleepStart,
    SleepEnd,
    SleepQuality
)
SELECT
    TRY_CONVERT(INT, SleepID),
    TRY_CONVERT(INT, UserID),
    TRY_CONVERT(DATE, SleepDate),
    TRY_CONVERT(DATETIME2, SleepStart),
    TRY_CONVERT(DATETIME2, SleepEnd),
    TRY_CONVERT(TINYINT, SleepQuality)
FROM dbo.Stg_Sleep;

GO

SET IDENTITY_INSERT dbo.Sleep OFF;
GO

SELECT COUNT(*) AS TotalSleep
FROM dbo.Sleep;
GO


/*=============================================================================
PRODUCTION LOAD : DAILY PROGRESS
=============================================================================*/

SET IDENTITY_INSERT dbo.DailyProgress ON;
GO

INSERT INTO dbo.DailyProgress
(
    ProgressID,
    UserID,
    ProgressDate,
    WeightKG
)
SELECT
    TRY_CONVERT(INT, ProgressID),
    TRY_CONVERT(INT, UserID),
    TRY_CONVERT(DATE, ProgressDate),
    TRY_PARSE(WeightKG AS DECIMAL(5,2))
FROM dbo.Stg_Weight;

GO

SET IDENTITY_INSERT dbo.DailyProgress OFF;
GO

SELECT COUNT(*) AS TotalDailyProgress
FROM dbo.DailyProgress;
GO

/*=============================================================================
PRODUCTION LOAD : FOOD ITEMS
=============================================================================*/

SET IDENTITY_INSERT dbo.FoodItems ON;
GO

INSERT INTO dbo.FoodItems
(
    FoodItemID,
    FoodName,
    CaloriesPer100g,
    ProteinPer100g,
    CarbsPer100g,
    FatPer100g
)
SELECT
    TRY_CONVERT(INT, FoodItemID),
    FoodName,
    TRY_PARSE(CaloriesPer100g AS DECIMAL(8,2)),
    TRY_PARSE(ProteinPer100g AS DECIMAL(8,2)),
    TRY_PARSE(CarbsPer100g AS DECIMAL(8,2)),
    TRY_PARSE(FatPer100g AS DECIMAL(8,2))
FROM dbo.Stg_FoodItems;

GO

SET IDENTITY_INSERT dbo.FoodItems OFF;
GO

SELECT COUNT(*) AS TotalFoodItems
FROM dbo.FoodItems;
GO


/*=============================================================================
PRODUCTION LOAD : MEALS
=============================================================================*/

SET IDENTITY_INSERT dbo.Meals ON;
GO

INSERT INTO dbo.Meals
(
    MealID,
    UserID,
    MealDate,
    MealType,
    TotalCalories
)
SELECT
    TRY_CONVERT(INT, MealID),
    TRY_CONVERT(INT, UserID),
    TRY_CONVERT(DATE, MealDate),
    MealType,
    TRY_PARSE(TotalCalories AS DECIMAL(8,2))
FROM dbo.Stg_Meals;

GO

SET IDENTITY_INSERT dbo.Meals OFF;
GO

SELECT COUNT(*) AS TotalMeals
FROM dbo.Meals;
GO


/*=============================================================================
PRODUCTION LOAD : MEAL ITEMS
=============================================================================*/

SET IDENTITY_INSERT dbo.MealItems ON;
GO

INSERT INTO dbo.MealItems
(
    MealItemID,
    MealID,
    FoodItemID,
    QuantityGrams
)
SELECT
    TRY_CONVERT(INT, MealItemID),
    TRY_CONVERT(INT, MealID),
    TRY_CONVERT(INT, FoodItemID),
    TRY_PARSE(QuantityGrams AS DECIMAL(8,2))
FROM dbo.Stg_MealItems;

GO

SET IDENTITY_INSERT dbo.MealItems OFF;
GO

SELECT COUNT(*) AS TotalMealItems
FROM dbo.MealItems;
GO


/*=============================================================================
FINAL DATA VERIFICATION
=============================================================================*/

SELECT 'Users' AS TableName, COUNT(*) AS TotalRows FROM dbo.Users
UNION ALL
SELECT 'Workouts', COUNT(*) FROM dbo.Workouts
UNION ALL
SELECT 'Diet', COUNT(*) FROM dbo.Diet
UNION ALL
SELECT 'Sleep', COUNT(*) FROM dbo.Sleep
UNION ALL
SELECT 'DailyProgress', COUNT(*) FROM dbo.DailyProgress
UNION ALL
SELECT 'FoodItems', COUNT(*) FROM dbo.FoodItems
UNION ALL
SELECT 'Meals', COUNT(*) FROM dbo.Meals
UNION ALL
SELECT 'MealItems', COUNT(*) FROM dbo.MealItems;
GO


/*=============================================================================
OPTIONAL : CLEAR STAGING TABLES
=============================================================================*/

TRUNCATE TABLE dbo.Stg_Users;
TRUNCATE TABLE dbo.Stg_Workouts;
TRUNCATE TABLE dbo.Stg_Diet;
TRUNCATE TABLE dbo.Stg_Sleep;
TRUNCATE TABLE dbo.Stg_Weight;
TRUNCATE TABLE dbo.Stg_FoodItems;
TRUNCATE TABLE dbo.Stg_Meals;
TRUNCATE TABLE dbo.Stg_MealItems;
GO


/*=============================================================================
VERIFY STAGING TABLES ARE EMPTY
=============================================================================*/

SELECT 'Stg_Users' AS TableName, COUNT(*) AS RowsCount FROM dbo.Stg_Users
UNION ALL
SELECT 'Stg_Workouts', COUNT(*) FROM dbo.Stg_Workouts
UNION ALL
SELECT 'Stg_Diet', COUNT(*) FROM dbo.Stg_Diet
UNION ALL
SELECT 'Stg_Sleep', COUNT(*) FROM dbo.Stg_Sleep
UNION ALL
SELECT 'Stg_Weight', COUNT(*) FROM dbo.Stg_Weight
UNION ALL
SELECT 'Stg_FoodItems', COUNT(*) FROM dbo.Stg_FoodItems
UNION ALL
SELECT 'Stg_Meals', COUNT(*) FROM dbo.Stg_Meals
UNION ALL
SELECT 'Stg_MealItems', COUNT(*) FROM dbo.Stg_MealItems;
GO


/*=============================================================================
INDEX INFORMATION
=============================================================================*/

EXEC sp_helpindex 'Users';
EXEC sp_helpindex 'Workouts';
EXEC sp_helpindex 'Diet';
EXEC sp_helpindex 'Sleep';
EXEC sp_helpindex 'DailyProgress';
EXEC sp_helpindex 'FoodItems';
EXEC sp_helpindex 'Meals';
EXEC sp_helpindex 'MealItems';
GO


/*=============================================================================
LOAD COMPLETED
=============================================================================*/

PRINT '==============================================';
PRINT 'AI Fitness Database Load Completed Successfully';
PRINT '==============================================';
GO