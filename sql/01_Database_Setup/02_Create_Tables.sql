USE AI_Fitness_DB;
GO

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
GO

CREATE TABLE Goals (
    GoalID              INT IDENTITY(1,1) PRIMARY KEY,
    UserID              INT NOT NULL,
    GoalType            NVARCHAR(50) NOT NULL,
    TargetWeightKG      DECIMAL(5,2) NULL,
    StartDate           DATE NOT NULL,
    TargetDate          DATE NULL,
    Status              NVARCHAR(20) NOT NULL DEFAULT 'Active',

    CONSTRAINT FK_Goals_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);
GO

CREATE TABLE Exercises (
    ExerciseID      INT IDENTITY(1,1) PRIMARY KEY,
    ExerciseName    NVARCHAR(100) NOT NULL,
    MuscleGroup     NVARCHAR(50) NOT NULL,
    CaloriesPerHour DECIMAL(6,2) NULL,
    DifficultyLevel NVARCHAR(20) NULL
);
GO

CREATE TABLE Workouts (
    WorkoutID          INT IDENTITY(1,1) PRIMARY KEY,
    UserID             INT NOT NULL,
    WorkoutDate        DATE NOT NULL,
    WorkoutType        NVARCHAR(50) NOT NULL,
    DurationMinutes    INT NOT NULL,
    CaloriesBurned     INT NULL,

    CONSTRAINT FK_Workouts_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);
GO

CREATE TABLE WorkoutExercises (
    WorkoutExerciseID  INT IDENTITY(1,1) PRIMARY KEY,
    WorkoutID          INT NOT NULL,
    ExerciseID         INT NOT NULL,
    Sets               INT NULL,
    Reps               INT NULL,
    WeightKG           DECIMAL(6,2) NULL,

    CONSTRAINT FK_WorkoutExercises_Workouts
        FOREIGN KEY (WorkoutID)
        REFERENCES Workouts(WorkoutID)
        ON DELETE CASCADE,

    CONSTRAINT FK_WorkoutExercises_Exercises
        FOREIGN KEY (ExerciseID)
        REFERENCES Exercises(ExerciseID)
);
GO

CREATE TABLE FoodItems (
    FoodItemID          INT IDENTITY(1,1) PRIMARY KEY,
    FoodName            NVARCHAR(100) NOT NULL,
    ServingSizeGrams    DECIMAL(6,2) NOT NULL,
    Calories            INT NOT NULL,
    ProteinG            DECIMAL(6,2) NULL,
    CarbsG              DECIMAL(6,2) NULL,
    FatG                DECIMAL(6,2) NULL
);
GO

CREATE TABLE Meals (
    MealID          INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT NOT NULL,
    MealDate        DATE NOT NULL,
    MealType        NVARCHAR(20) NOT NULL,
    TotalCalories   INT NULL,

    CONSTRAINT FK_Meals_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);
GO

CREATE TABLE MealItems (
    MealItemID      INT IDENTITY(1,1) PRIMARY KEY,
    MealID          INT NOT NULL,
    FoodItemID      INT NOT NULL,
    QuantityGrams   DECIMAL(6,2) NOT NULL,

    CONSTRAINT FK_MealItems_Meals
        FOREIGN KEY (MealID)
        REFERENCES Meals(MealID)
        ON DELETE CASCADE,

    CONSTRAINT FK_MealItems_FoodItems
        FOREIGN KEY (FoodItemID)
        REFERENCES FoodItems(FoodItemID)
);
GO

CREATE TABLE Sleep (
    SleepID         INT IDENTITY(1,1) PRIMARY KEY,
    UserID          INT NOT NULL,
    SleepDate       DATE NOT NULL,
    SleepStart      DATETIME2 NOT NULL,
    SleepEnd        DATETIME2 NOT NULL,
    DurationMinutes AS DATEDIFF(MINUTE, SleepStart, SleepEnd) PERSISTED,
    SleepQuality    TINYINT NOT NULL
        CHECK (SleepQuality BETWEEN 1 AND 10),

    CONSTRAINT FK_Sleep_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);
GO

CREATE TABLE DailyProgress (
    ProgressID     INT IDENTITY(1,1) PRIMARY KEY,
    UserID         INT NOT NULL,
    ProgressDate   DATE NOT NULL,
    WeightKG       DECIMAL(5,2) NOT NULL,

    CONSTRAINT FK_DailyProgress_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);
