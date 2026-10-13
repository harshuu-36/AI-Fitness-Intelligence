/*============================================================
Query 11
Title      : Users Taller Than Average Height
Difficulty : ⭐⭐
Concept    : Subquery, AVG(), WHERE
============================================================*/

SELECT
    UserID,
    FirstName,
    LastName,
    HeightCM
FROM Users
WHERE HeightCM >
(
    SELECT AVG(HeightCM)
    FROM Users
)
ORDER BY HeightCM DESC;
GO

/*============================================================
Query 12
Title      : Categorize Users by Height
Difficulty : ⭐⭐
Concept    : CASE WHEN
============================================================*/

SELECT
    UserID,
    FirstName,
    LastName,
    HeightCM,
    CASE
        WHEN HeightCM < 160 THEN 'Short'
        WHEN HeightCM BETWEEN 160 AND 175 THEN 'Average'
        ELSE 'Tall'
    END AS HeightCategory
FROM Users
ORDER BY HeightCM DESC;
GO

/*============================================================
Query 13
Title      : Users with Height Between 165 cm and 180 cm
Difficulty : ⭐⭐
Concept    : BETWEEN
============================================================*/

SELECT
    UserID,
    FirstName,
    LastName,
    HeightCM
FROM Users
WHERE HeightCM BETWEEN 165 AND 180
ORDER BY HeightCM DESC;
GO

/*============================================================
Query 14
Title      : Users by Gender using IN
Difficulty : ⭐⭐
Concept    : IN Operator
============================================================*/

SELECT
    UserID,
    FirstName,
    LastName,
    Gender
FROM Users
WHERE Gender IN ('M', 'F')
ORDER BY Gender, FirstName;
GO

/*============================================================
Query 15
Title      : Users Whose First Name Starts with 'A'
Difficulty : ⭐⭐
Concept    : LIKE Operator
============================================================*/

SELECT
    UserID,
    FirstName,
    LastName,
    Email
FROM Users
WHERE FirstName LIKE 'A%'
ORDER BY FirstName;
GO

/*============================================================
Query 16
Title      : User Workout History
Difficulty : ⭐⭐⭐
Concept    : INNER JOIN
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    W.WorkoutID,
    W.WorkoutDate,
    W.WorkoutType,
    W.DurationMinutes
FROM Users AS U
INNER JOIN Workouts AS W
    ON U.UserID = W.UserID
ORDER BY
    W.WorkoutDate DESC,
    U.UserID;
GO

/*============================================================
Query 17
Title      : All Users with Their Workout Details
Difficulty : ⭐⭐⭐
Concept    : LEFT JOIN
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    W.WorkoutID,
    W.WorkoutDate,
    W.WorkoutType,
    W.DurationMinutes
FROM Users AS U
LEFT JOIN Workouts AS W
    ON U.UserID = W.UserID
ORDER BY
    U.UserID,
    W.WorkoutDate;
GO

/*============================================================
Query 18
Title      : User Workout and Sleep Report
Difficulty : ⭐⭐⭐
Concept    : Multiple INNER JOIN
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    W.WorkoutDate,
    W.WorkoutType,
    W.DurationMinutes,
    S.SleepDate,
    S.DurationMinutes AS SleepDuration,
    S.SleepQuality
FROM Users AS U
INNER JOIN Workouts AS W
    ON U.UserID = W.UserID
INNER JOIN Sleep AS S
    ON U.UserID = S.UserID
   AND W.WorkoutDate = S.SleepDate
ORDER BY
    W.WorkoutDate DESC,
    U.UserID;
GO

/*============================================================
Query 19
Title      : Total Workouts Completed by Each User
Difficulty : ⭐⭐⭐
Concept    : INNER JOIN + GROUP BY + COUNT()
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalWorkouts
FROM Users AS U
INNER JOIN Workouts AS W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY
    TotalWorkouts DESC;
GO

/*============================================================
Query 20
Title      : Users with More Than 200 Workouts
Difficulty : ⭐⭐⭐
Concept    : HAVING + GROUP BY + JOIN
============================================================*/

SELECT
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalWorkouts
FROM Users AS U
INNER JOIN Workouts AS W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
HAVING COUNT(W.WorkoutID) > 200
ORDER BY
    TotalWorkouts DESC;
GO