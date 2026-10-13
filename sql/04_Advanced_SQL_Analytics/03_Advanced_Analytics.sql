/*============================================================
Query 21
Title      : Rank Users by Total Workouts
Difficulty : ⭐⭐⭐⭐
Concept    : Window Function (RANK)
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalWorkouts,
    RANK() OVER (
        ORDER BY COUNT(W.WorkoutID) DESC
    ) AS WorkoutRank
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY WorkoutRank;
GO

/*============================================================
Query 22
Title      : Dense Rank Users by Total Workout Minutes
Difficulty : ⭐⭐⭐⭐
Concept    : DENSE_RANK() Window Function
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    SUM(W.DurationMinutes) AS TotalWorkoutMinutes,
    DENSE_RANK() OVER (
        ORDER BY SUM(W.DurationMinutes) DESC
    ) AS WorkoutRank
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY WorkoutRank;
GO

/*============================================================
Query 23
Title      : Unique Leaderboard using ROW_NUMBER()
Difficulty : ⭐⭐⭐⭐
Concept    : ROW_NUMBER() Window Function
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalWorkouts,
    ROW_NUMBER() OVER (
        ORDER BY COUNT(W.WorkoutID) DESC
    ) AS LeaderboardPosition
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY LeaderboardPosition;
GO

/*============================================================
Query 24
Title      : User Segmentation using NTILE()
Difficulty : ⭐⭐⭐⭐
Concept    : NTILE() Window Function + CTE
============================================================*/

WITH UserWorkoutSummary AS
(
    SELECT
        U.UserID,
        U.FirstName,
        U.LastName,
        SUM(W.DurationMinutes) AS TotalWorkoutMinutes
    FROM Users U
    INNER JOIN Workouts W
        ON U.UserID = W.UserID
    GROUP BY
        U.UserID,
        U.FirstName,
        U.LastName
)

SELECT
    UserID,
    FirstName,
    LastName,
    TotalWorkoutMinutes,
    NTILE(4) OVER (ORDER BY TotalWorkoutMinutes DESC) AS FitnessQuartile
FROM UserWorkoutSummary
ORDER BY FitnessQuartile, TotalWorkoutMinutes DESC;
GO

/*============================================================
Query 25
Title      : Compare Current Workout with Previous Workout
Difficulty : ⭐⭐⭐⭐
Concept    : LAG() Window Function
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes AS CurrentWorkoutDuration,
    LAG(DurationMinutes) OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS PreviousWorkoutDuration
FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================
Query 26
Title      : Compare Current Workout with Next Workout
Difficulty : ⭐⭐⭐⭐
Concept    : LEAD() Window Function
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes AS CurrentWorkoutDuration,
    LEAD(DurationMinutes) OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS NextWorkoutDuration
FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================
Query 27
Title      : First Workout Duration for Every User
Difficulty : ⭐⭐⭐⭐
Concept    : FIRST_VALUE() Window Function
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes AS CurrentWorkoutDuration,

    FIRST_VALUE(DurationMinutes) OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS FirstWorkoutDuration

FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================
Query 28
Title      : Last Workout Duration for Every User
Difficulty : ⭐⭐⭐⭐⭐
Concept    : LAST_VALUE() Window Function
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes AS CurrentWorkoutDuration,

    LAST_VALUE(DurationMinutes) OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
        ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    ) AS LastWorkoutDuration

FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================
Query 29
Title      : Running Total of Workout Minutes
Difficulty : ⭐⭐⭐⭐⭐
Concept    : SUM() OVER() - Running Total
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes,

    SUM(DurationMinutes) OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS RunningWorkoutMinutes

FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================
Query 30
Title      : 3-Workout Moving Average
Difficulty : ⭐⭐⭐⭐⭐
Concept    : AVG() OVER() - Moving Average
============================================================*/

SELECT
    UserID,
    WorkoutDate,
    DurationMinutes,

    ROUND(
        AVG(CAST(DurationMinutes AS DECIMAL(10,2))) OVER
        (
            PARTITION BY UserID
            ORDER BY WorkoutDate
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS MovingAverageDuration

FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO