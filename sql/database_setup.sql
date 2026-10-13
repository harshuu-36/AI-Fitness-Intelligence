/* =============================================================
   AI FITNESS INTELLIGENCE PLATFORM — SQL SERVER SCHEMA (3NF)
   ============================================================= */

/* -------------------------------------------------------------
   1. USERS  (root entity)
   ------------------------------------------------------------- */
CREATE TABLE Users (
    UserID          INT IDENTITY(1,1) PRIMARY KEY,
    FirstName       NVARCHAR(50)    NOT NULL,
    LastName        NVARCHAR(50)    NOT NULL,
    Email           NVARCHAR(255)   NOT NULL UNIQUE,
    PasswordHash    VARBINARY(256)  NOT NULL,
    DateOfBirth     DATE            NOT NULL,
    Gender          CHAR(1)         NULL CHECK (Gender IN ('M','F','O')),
    HeightCM        DECIMAL(5,2)    NULL,
    CreatedAt       DATETIME2       NOT NULL DEFAULT SYSUTCDATETIME(),
    IsActive        BIT             NOT NULL DEFAULT 1
);

/* -------------------------------------------------------------
   2. GOALS  (one user -> many goals)
   ------------------------------------------------------------- */
CREATE TABLE Goals (
    GoalID          INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT             NOT NULL,
    GoalType        NVARCHAR(50)    NOT NULL,   -- e.g. 'WeightLoss','MuscleGain','Endurance'
    TargetValue     DECIMAL(6,2)    NOT NULL,   -- e.g. target kg, target 5k time
    StartDate       DATE            NOT NULL,
    TargetDate      DATE            NOT NULL,
    Status          NVARCHAR(20)    NOT NULL DEFAULT 'Active'
                        CHECK (Status IN ('Active','Completed','Abandoned')),
    CONSTRAINT FK_Goals_Users FOREIGN KEY (UserID)
        REFERENCES Users(UserID) ON DELETE CASCADE
);

/* -------------------------------------------------------------
   3. EXERCISES  (master / reference data — standalone)
   ------------------------------------------------------------- */
CREATE TABLE Exercises (
    ExerciseID          INT IDENTITY(1,1) PRIMARY KEY,
    ExerciseName        NVARCHAR(100)   NOT NULL UNIQUE,
    Category            NVARCHAR(50)    NOT NULL,   -- 'Cardio','Strength','Flexibility'
    PrimaryMuscleGroup  NVARCHAR(50)    NULL,
    EquipmentNeeded     NVARCHAR(100)   NULL,
    CaloriesPerMinute   DECIMAL(5,2)    NULL
);

/* -------------------------------------------------------------
   4. WORKOUTS  (a session, belongs to a user)
   ------------------------------------------------------------- */
CREATE TABLE Workouts (
    WorkoutID       INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT             NOT NULL,
    WorkoutDate     DATE            NOT NULL,
    WorkoutType     NVARCHAR(50)    NULL,        -- 'Strength','Cardio','Mixed'
    DurationMinutes INT             NULL,
    Notes           NVARCHAR(500)   NULL,
    CONSTRAINT FK_Workouts_Users FOREIGN KEY (UserID)
        REFERENCES Users(UserID) ON DELETE CASCADE
);

/* -------------------------------------------------------------
   5. WORKOUT_EXERCISES  (junction: resolves many-to-many
      between Workouts and Exercises, 3NF-critical table)
   ------------------------------------------------------------- */
CREATE TABLE WorkoutExercises (
    WorkoutExerciseID  INT IDENTITY(1,1) PRIMARY KEY,
    WorkoutID          INT             NOT NULL,
    ExerciseID         INT             NOT NULL,
    SetsCompleted      INT             NULL,
    RepsCompleted      INT             NULL,
    WeightUsedKG       DECIMAL(6,2)    NULL,
    DurationSeconds    INT             NULL,       -- for cardio/time-based exercises
    SequenceOrder      INT             NOT NULL DEFAULT 1,
    CONSTRAINT FK_WE_Workouts FOREIGN KEY (WorkoutID)
        REFERENCES Workouts(WorkoutID) ON DELETE CASCADE,
    CONSTRAINT FK_WE_Exercises FOREIGN KEY (ExerciseID)
        REFERENCES Exercises(ExerciseID) ON DELETE CASCADE
);

/* -------------------------------------------------------------
   6. FOOD_ITEMS  (master / reference data — standalone)
   ------------------------------------------------------------- */
CREATE TABLE FoodItems (
    FoodItemID      INT IDENTITY(1,1) PRIMARY KEY,
    FoodName        NVARCHAR(150)   NOT NULL UNIQUE,
    CaloriesPerUnit DECIMAL(6,2)    NOT NULL,
    ProteinPerUnitG DECIMAL(6,2)    NULL,
    CarbsPerUnitG   DECIMAL(6,2)    NULL,
    FatPerUnitG     DECIMAL(6,2)    NULL,
    UnitOfMeasure   NVARCHAR(20)    NOT NULL DEFAULT 'serving' -- 'gram','ml','serving'
);

/* -------------------------------------------------------------
   7. MEALS  (a meal event, belongs to a user)
   ------------------------------------------------------------- */
CREATE TABLE Meals (
    MealID          INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT             NOT NULL,
    MealDate        DATE            NOT NULL,
    MealType        NVARCHAR(20)    NOT NULL
                        CHECK (MealType IN ('Breakfast','Lunch','Dinner','Snack')),
    CONSTRAINT FK_Meals_Users FOREIGN KEY (UserID)
        REFERENCES Users(UserID) ON DELETE CASCADE
);

/* -------------------------------------------------------------
   8. MEAL_ITEMS  (junction: resolves many-to-many between
      Meals and FoodItems, 3NF-critical table)
   ------------------------------------------------------------- */
CREATE TABLE MealItems (
    MealItemID      INT IDENTITY(1,1) PRIMARY KEY,
    MealID          INT             NOT NULL,
    FoodItemID      INT             NOT NULL,
    Quantity        DECIMAL(6,2)    NOT NULL DEFAULT 1,
    CONSTRAINT FK_MI_Meals FOREIGN KEY (MealID)
        REFERENCES Meals(MealID) ON DELETE CASCADE,
    CONSTRAINT FK_MI_FoodItems FOREIGN KEY (FoodItemID)
        REFERENCES FoodItems(FoodItemID) ON DELETE CASCADE
);

/* -------------------------------------------------------------
   9. SLEEP  (one record per user per night)
   ------------------------------------------------------------- */
CREATE TABLE Sleep (
    SleepID         INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT             NOT NULL,
    SleepDate       DATE            NOT NULL,      -- the night this record refers to
    SleepStart      DATETIME2       NOT NULL,
    SleepEnd        DATETIME2       NOT NULL,
    DurationMinutes AS DATEDIFF(MINUTE, SleepStart, SleepEnd) PERSISTED,
    SleepQuality    TINYINT         NULL CHECK (SleepQuality BETWEEN 1 AND 10),
    CONSTRAINT FK_Sleep_Users FOREIGN KEY (UserID)
        REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT UQ_Sleep_User_Date UNIQUE (UserID, SleepDate)
);

/* -------------------------------------------------------------
   10. DAILY_PROGRESS  (daily rollup snapshot per user)
   ------------------------------------------------------------- */
CREATE TABLE DailyProgress (
    ProgressID          INT IDENTITY(1,1) PRIMARY KEY,
    UserID              INT             NOT NULL,
    ProgressDate        DATE            NOT NULL,
    WeightKG            DECIMAL(5,2)    NULL,
    BodyFatPercentage   DECIMAL(4,2)    NULL,
    CaloriesConsumed    INT             NULL,
    CaloriesBurned      INT             NULL,
    StepsCount          INT             NULL,
    WaterIntakeML       INT             NULL,
    CONSTRAINT FK_DP_Users FOREIGN KEY (UserID)
        REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT UQ_DP_User_Date UNIQUE (UserID, ProgressDate)
);

/* -------------------------------------------------------------
   HELPFUL INDEXES (not part of 3NF, but essential for a
   time-series-heavy app — see "Best Practices" section)
   ------------------------------------------------------------- */
CREATE INDEX IX_Workouts_User_Date        ON Workouts(UserID, WorkoutDate);
CREATE INDEX IX_Meals_User_Date           ON Meals(UserID, MealDate);
CREATE INDEX IX_WorkoutExercises_Workout  ON WorkoutExercises(WorkoutID);
CREATE INDEX IX_MealItems_Meal            ON MealItems(MealID);
CREATE INDEX IX_Goals_User_Status         ON Goals(UserID, Status);


-- verify tables
select * from Users;
select * from Exercises;

-- check table structure
sp_help Users;
EXEC sp_help 'Users';

--check foriegn keys
EXEC sp_fkeys 'Goals';

-- check all tables
SELECT name
FROM sys.tables;

-- the basic select
SELECT UserID, FirstName, LastName, Email
FROM Users;

--filtering with where
SELECT WorkoutID, WorkoutDate, WorkoutType, DurationMinutes
FROM Workouts
WHERE UserID = 5
  AND WorkoutDate >= '2026-08-01';

-- join - combining a transactional table with its parent
SELECT u.FirstName, u.LastName, w.WorkoutDate, w.WorkoutType
FROM Workouts w
INNER JOIN Users u ON w.UserID = u.UserID
WHERE w.WorkoutDate >= '2026-08-01';

-- join through a junction table(the 3nf payoff)
SELECT
    w.WorkoutDate,
    e.ExerciseName,
    we.SetsCompleted,
    we.RepsCompleted,
    we.WeightUsedKG
FROM Workouts w
INNER JOIN WorkoutExercises we ON w.WorkoutID = we.WorkoutID
INNER JOIN Exercises e ON we.ExerciseID = e.ExerciseID
WHERE w.UserID = 5
ORDER BY w.WorkoutDate, we.SequenceOrder;

-- aggregation with group by
SELECT
    w.UserID,
    w.WorkoutDate,
    SUM(we.SetsCompleted * we.RepsCompleted) AS TotalReps,
    COUNT(DISTINCT we.ExerciseID) AS ExercisesPerformed
FROM Workouts w
INNER JOIN WorkoutExercises we ON w.WorkoutID = we.WorkoutID
GROUP BY w.UserID, w.WorkoutDate
ORDER BY w.WorkoutDate;

-- subquery - comparing against a computed value
SELECT dp.UserID, dp.ProgressDate, dp.CaloriesBurned
FROM DailyProgress dp
WHERE dp.CaloriesBurned > (
    SELECT AVG(dp2.CaloriesBurned)
    FROM DailyProgress dp2
    WHERE dp2.UserID = dp.UserID
      AND dp2.ProgressDate >= DATEADD(DAY, -30, dp.ProgressDate)
);

-- windows functions - trend analysis without collapsing rows
SELECT
    UserID,
    ProgressDate,
    WeightKG,
    AVG(WeightKG) OVER (
        PARTITION BY UserID
        ORDER BY ProgressDate
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS SevenDayAvgWeight
FROM DailyProgress
ORDER BY UserID, ProgressDate;
