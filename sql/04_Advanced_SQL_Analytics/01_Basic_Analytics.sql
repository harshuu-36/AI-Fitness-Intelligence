/*====================================================================
Project   : AI Fitness Intelligence Platform
Module    : 04_Advanced_SQL_Analytics
File      : 01_Basic_Analytics.sql
Author    : Harsh
Database  : AI_Fitness_DB

Description:
Basic SQL analytics queries for user and fitness insights.

====================================================================*/

USE AI_Fitness_DB;
GO

/*============================================================
Query 1
Title      : Total Registered Users
Difficulty : ⭐
Concept    : COUNT()
============================================================*/

SELECT COUNT(*) AS TotalUsers
FROM Users;

/*============================================================
Query 2
Title      : Total Workouts Recorded
Difficulty : ⭐
Concept    : COUNT()
============================================================*/

SELECT COUNT(*) AS TotalWorkouts
FROM Workouts;

/*============================================================
Query 3
Title : Users by Gender
============================================================*/

SELECT
    Gender,
    COUNT(*) AS TotalUsers
FROM Users
GROUP BY Gender
ORDER BY TotalUsers DESC;
GO

/*============================================================
Query 4
Title      : Average Height of Users
Difficulty : ⭐
Concept    : AVG(), ROUND()
============================================================*/

SELECT
    ROUND(AVG(HeightCM), 2) AS AverageHeightCM
FROM Users;
GO

/*============================================================
Query 5
Title      : Shortest and Tallest User Height
Difficulty : ⭐
Concept    : MIN(), MAX()
============================================================*/

SELECT
    MIN(HeightCM) AS ShortestHeightCM,
    MAX(HeightCM) AS TallestHeightCM
FROM Users;
GO

/*============================================================
Query 6
Title      : List All Unique Workout Types
Difficulty : ⭐
Concept    : DISTINCT
============================================================*/

SELECT DISTINCT WorkoutType
FROM Workouts
ORDER BY WorkoutType;
GO

/*============================================================
Query 7
Title      : Top 10 Most Recent Workouts
Difficulty : ⭐⭐
Concept    : TOP, ORDER BY
============================================================*/

SELECT TOP (10)
    WorkoutID,
    UserID,
    WorkoutType,
    WorkoutDate,
    DurationMinutes
FROM Workouts
ORDER BY WorkoutDate DESC;
GO

/*============================================================
Query 8
Title      : Top 10 Longest Workout Sessions
Difficulty : ⭐⭐
Concept    : TOP, ORDER BY
============================================================*/

SELECT TOP 10
    WorkoutID,
    UserID,
    WorkoutType,
    WorkoutDate,
    DurationMinutes
FROM Workouts
ORDER BY DurationMinutes DESC;
GO

/*============================================================
Query 9
Title      : Workouts Longer Than 60 Minutes
Difficulty : ⭐⭐
Concept    : WHERE
============================================================*/

SELECT
    WorkoutID,
    UserID,
    WorkoutType,
    WorkoutDate,
    DurationMinutes
FROM Workouts
WHERE DurationMinutes > 60
ORDER BY DurationMinutes DESC;
GO

/*============================================================
Query 10
Title      : Users with More Than 20 Workouts
Difficulty : ⭐⭐
Concept    : GROUP BY, HAVING, COUNT()
============================================================*/

SELECT
    UserID,
    COUNT(*) AS TotalWorkouts
FROM Workouts
GROUP BY UserID
HAVING COUNT(*) > 20
ORDER BY TotalWorkouts DESC;
GO