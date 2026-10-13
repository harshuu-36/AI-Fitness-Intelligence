/*============================================================

SQL Question 31

Title       : Rank Users by Total Calories Burned

Difficulty  : ⭐⭐⭐⭐

Concept     : SUM() + RANK() OVER()

Business Requirement:

The fitness analytics team wants to rank users based on
their total calories burned through workouts. Users with
the same total calories should receive the same rank.

============================================================*/

WITH UserCalories AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        SUM(W.CaloriesBurned) AS TotalCaloriesBurned

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
    TotalCaloriesBurned,

    RANK() OVER
    (
        ORDER BY TotalCaloriesBurned DESC
    ) AS UserRank

FROM UserCalories

ORDER BY UserRank;
GO


/*============================================================

SQL Question 32

Title       : Rank Users Within Each Workout Type

Difficulty  : ⭐⭐⭐⭐

Concept     : PARTITION BY + RANK()

Business Requirement:

The fitness analytics team wants to identify the top
performing users within each workout type based on the
total calories burned. Users should be ranked separately
for each workout category.

============================================================*/

WITH WorkoutRanking AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        W.WorkoutType,

        SUM(W.CaloriesBurned) AS TotalCaloriesBurned

    FROM Users U

    INNER JOIN Workouts W
        ON U.UserID = W.UserID

    GROUP BY

        U.UserID,
        U.FirstName,
        U.LastName,
        W.WorkoutType
)

SELECT

    UserID,
    FirstName,
    LastName,

    WorkoutType,

    TotalCaloriesBurned,

    RANK() OVER
    (
        PARTITION BY WorkoutType
        ORDER BY TotalCaloriesBurned DESC
    ) AS WorkoutRank

FROM WorkoutRanking

ORDER BY

    WorkoutType,
    WorkoutRank;
GO

/*============================================================

SQL Question 33

Title       : Dense Rank Users by Total Workout Duration

Difficulty  : ⭐⭐⭐⭐

Concept     : DENSE_RANK()

Business Requirement:

The fitness analytics team wants to rank users based on
their total workout duration. Users with the same workout
duration should receive the same rank without skipping
subsequent ranks.

============================================================*/

WITH UserWorkoutDuration AS
(
    SELECT
        U.UserID,
        U.FirstName,
        U.LastName,
        SUM(W.DurationMinutes) AS TotalWorkoutDuration
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
    TotalWorkoutDuration,

    DENSE_RANK() OVER
    (
        ORDER BY TotalWorkoutDuration DESC
    ) AS DenseRank

FROM UserWorkoutDuration
ORDER BY DenseRank;
GO

/*============================================================

SQL Question 34

Title       : Assign Users into Performance Quartiles

Difficulty  : ⭐⭐⭐⭐

Concept     : NTILE()

Business Requirement:

The business wants to divide users into four equal
performance groups based on total calories burned.
These groups will be used for targeted engagement
campaigns.

============================================================*/

WITH UserCalories AS
(
    SELECT
        U.UserID,
        U.FirstName,
        U.LastName,
        SUM(W.CaloriesBurned) AS TotalCaloriesBurned
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
    TotalCaloriesBurned,

    NTILE(4) OVER
    (
        ORDER BY TotalCaloriesBurned DESC
    ) AS PerformanceQuartile

FROM UserCalories
ORDER BY PerformanceQuartile,
         TotalCaloriesBurned DESC;
GO

/*============================================================

SQL Question 35

Title       : Compare Current Workout with Previous Workout

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : LAG()

Business Requirement:

The fitness team wants to compare each user's current
workout duration with their previous workout duration
to analyze consistency and identify performance changes.

============================================================*/

SELECT

    UserID,

    WorkoutDate,

    WorkoutType,

    DurationMinutes,

    LAG(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS PreviousWorkoutDuration,

    DurationMinutes -
    LAG(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS DurationDifference

FROM Workouts
ORDER BY
    UserID,
    WorkoutDate;
GO

/*============================================================

SQL Question 36

Title       : Compare Current Workout with Next Workout

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : LEAD()

Business Requirement:

The fitness analytics team wants to compare each user's
current workout duration with their next scheduled workout
to analyze future workout consistency.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    WorkoutType,
    DurationMinutes,

    LEAD(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS NextWorkoutDuration,

    LEAD(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) - DurationMinutes AS DurationDifference

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 37

Title       : Running Total of Calories Burned

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : SUM() OVER()

Business Requirement:

The fitness team wants to calculate the cumulative calories
burned by each user over time to monitor long-term progress.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    CaloriesBurned,

    SUM(CaloriesBurned)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS RunningCalories

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO


/*============================================================

SQL Question 38

Title       : Running Total of Workout Duration

Difficulty  : ⭐⭐⭐⭐

Concept     : SUM() OVER()

Business Requirement:

The business wants to monitor cumulative workout duration
for each user throughout their fitness journey.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    DurationMinutes,

    SUM(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS RunningWorkoutMinutes

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO


/*============================================================

SQL Question 39

Title       : Moving Average of Workout Duration

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : AVG() OVER()

Business Requirement:

The analytics team wants to calculate the moving average
of workout duration using the current and previous two
workout sessions to identify workout consistency.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    DurationMinutes,

    ROUND
    (
        AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
        OVER
        (
            PARTITION BY UserID
            ORDER BY WorkoutDate
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS MovingAverageDuration

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 40

Title       : First and Latest Recorded Weight

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : FIRST_VALUE() + LAST_VALUE()

Business Requirement:

The fitness coaches want to compare each user's first
recorded weight with their latest recorded weight to
measure overall progress.

============================================================*/

SELECT

    UserID,

    ProgressDate,

    WeightKG,

    FIRST_VALUE(WeightKG)
    OVER
    (
        PARTITION BY UserID
        ORDER BY ProgressDate
    ) AS FirstRecordedWeight,

    LAST_VALUE(WeightKG)
    OVER
    (
        PARTITION BY UserID
        ORDER BY ProgressDate
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING
    ) AS LatestRecordedWeight

FROM DailyProgress

ORDER BY UserID,
         ProgressDate;
GO

/*============================================================

SQL Question 41

Title       : Rank Users Using PERCENT_RANK()

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : PERCENT_RANK()

Business Requirement:

The analytics team wants to determine each user's
relative performance based on total calories burned.
The percentile ranking helps compare users against
the entire population.

============================================================*/

WITH UserCalories AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        SUM(W.CaloriesBurned) AS TotalCaloriesBurned

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
    TotalCaloriesBurned,

    ROUND
    (
        PERCENT_RANK()
        OVER(ORDER BY TotalCaloriesBurned),
        4
    ) AS PercentRank

FROM UserCalories

ORDER BY TotalCaloriesBurned DESC;
GO

/*============================================================

SQL Question 42

Title       : Analyze User Distribution Using CUME_DIST()

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : CUME_DIST()

Business Requirement:

The business wants to identify what percentage of users
have burned equal or fewer calories than each user.

============================================================*/

WITH UserCalories AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        SUM(W.CaloriesBurned) AS TotalCaloriesBurned

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
    TotalCaloriesBurned,

    ROUND
    (
        CUME_DIST()
        OVER(ORDER BY TotalCaloriesBurned),
        4
    ) AS CumulativeDistribution

FROM UserCalories

ORDER BY TotalCaloriesBurned DESC;
GO

/*============================================================

SQL Question 43

Title       : Find Top Performer in Each Workout Type

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : ROW_NUMBER() + PARTITION BY

Business Requirement:

Identify the highest calorie-burning user for each
workout type.

============================================================*/

WITH WorkoutRanking AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        W.WorkoutType,

        SUM(W.CaloriesBurned) AS TotalCalories,

        ROW_NUMBER()
        OVER
        (
            PARTITION BY W.WorkoutType
            ORDER BY SUM(W.CaloriesBurned) DESC
        ) AS RN

    FROM Users U

    INNER JOIN Workouts W
        ON U.UserID = W.UserID

    GROUP BY

        U.UserID,
        U.FirstName,
        U.LastName,
        W.WorkoutType
)

SELECT *

FROM WorkoutRanking

WHERE RN = 1;
GO

/*============================================================

SQL Question 44

Title       : Workout Duration Difference from User Average

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : AVG() OVER(PARTITION BY)

Business Requirement:

Compare each workout duration with the user's average
workout duration to identify above-average and
below-average sessions.

============================================================*/

SELECT

    UserID,

    WorkoutDate,

    WorkoutType,

    DurationMinutes,

    ROUND
    (
        AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
        OVER(PARTITION BY UserID),
        2
    ) AS AvgWorkoutDuration,

    ROUND
    (
        DurationMinutes -
        AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
        OVER(PARTITION BY UserID),
        2
    ) AS DifferenceFromAverage

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 45

Title       : Identify Consecutive Workout Improvement

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : LAG() + CASE

Business Requirement:

Determine whether each workout duration improved,
declined, or remained the same compared to the
previous workout.

============================================================*/

SELECT

    UserID,

    WorkoutDate,

    DurationMinutes,

    LAG(DurationMinutes)
    OVER
    (
        PARTITION BY UserID
        ORDER BY WorkoutDate
    ) AS PreviousDuration,

    CASE

        WHEN LAG(DurationMinutes)
             OVER(PARTITION BY UserID ORDER BY WorkoutDate)
             IS NULL
        THEN 'First Workout'

        WHEN DurationMinutes >
             LAG(DurationMinutes)
             OVER(PARTITION BY UserID ORDER BY WorkoutDate)
        THEN 'Improved'

        WHEN DurationMinutes <
             LAG(DurationMinutes)
             OVER(PARTITION BY UserID ORDER BY WorkoutDate)
        THEN 'Declined'

        ELSE 'No Change'

    END AS PerformanceStatus

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 46

Title       : 3-Workout Moving Average of Calories Burned

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : AVG() OVER() + ROWS BETWEEN

Business Requirement:

The fitness analytics team wants to calculate a rolling
average of calories burned using the current workout and
the previous two workouts for each user.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    CaloriesBurned,

    ROUND
    (
        AVG(CAST(CaloriesBurned AS DECIMAL(10,2)))
        OVER
        (
            PARTITION BY UserID
            ORDER BY WorkoutDate
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS RollingAvgCalories

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 47

Title       : User Performance Dashboard using Multiple Window Functions

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : RANK() + AVG() + SUM() OVER()

Business Requirement:

Create a dashboard showing each workout, cumulative
calories burned, average calories burned, and overall
user ranking.

============================================================*/

WITH UserCalories AS
(
    SELECT
        UserID,
        SUM(CaloriesBurned) AS TotalCalories
    FROM Workouts
    GROUP BY UserID
)

SELECT

    W.UserID,
    W.WorkoutDate,
    W.CaloriesBurned,

    SUM(W.CaloriesBurned)
    OVER
    (
        PARTITION BY W.UserID
        ORDER BY W.WorkoutDate
    ) AS RunningCalories,

    ROUND
    (
        AVG(CAST(W.CaloriesBurned AS DECIMAL(10,2)))
        OVER(PARTITION BY W.UserID),
        2
    ) AS AvgCalories,

    RANK()
    OVER
    (
        ORDER BY UC.TotalCalories DESC
    ) AS OverallRank

FROM Workouts W

INNER JOIN UserCalories UC
ON W.UserID = UC.UserID

ORDER BY
    OverallRank,
    W.UserID,
    W.WorkoutDate;
GO

/*============================================================

SQL Question 48

Title       : Categorize Workout Performance

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : CASE + AVG() OVER()

Business Requirement:

Compare every workout with the user's average workout
duration and classify the workout performance.

============================================================*/

SELECT

    UserID,
    WorkoutDate,
    DurationMinutes,

    ROUND
    (
        AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
        OVER(PARTITION BY UserID),
        2
    ) AS AvgDuration,

    CASE

        WHEN DurationMinutes >
             AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
             OVER(PARTITION BY UserID)
        THEN 'Above Average'

        WHEN DurationMinutes <
             AVG(CAST(DurationMinutes AS DECIMAL(10,2)))
             OVER(PARTITION BY UserID)
        THEN 'Below Average'

        ELSE 'Average'

    END AS PerformanceCategory

FROM Workouts

ORDER BY UserID,
         WorkoutDate;
GO

/*============================================================

SQL Question 49

Title       : Top Workout of Every User

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : ROW_NUMBER() + PARTITION BY

Business Requirement:

Identify the workout session with the highest calories
burned for each user.

============================================================*/

WITH RankedWorkouts AS
(
    SELECT

        WorkoutID,
        UserID,
        WorkoutDate,
        WorkoutType,
        CaloriesBurned,

        ROW_NUMBER()
        OVER
        (
            PARTITION BY UserID
            ORDER BY CaloriesBurned DESC
        ) AS RN

    FROM Workouts
)

SELECT

    WorkoutID,
    UserID,
    WorkoutDate,
    WorkoutType,
    CaloriesBurned

FROM RankedWorkouts

WHERE RN = 1

ORDER BY UserID;
GO

/*============================================================

SQL Question 50

Title       : Final User Fitness Performance Report

Difficulty  : ⭐⭐⭐⭐⭐

Concept     : CTE + Window Functions + Aggregation

Business Requirement:

Generate a final report summarizing each user's workout
performance, total calories burned, total workout
duration, average calories per workout, and overall rank.

============================================================*/

WITH UserSummary AS
(
    SELECT

        U.UserID,
        U.FirstName,
        U.LastName,

        SUM(W.CaloriesBurned) AS TotalCalories,

        SUM(W.DurationMinutes) AS TotalDuration,

        ROUND
        (
            AVG(CAST(W.CaloriesBurned AS DECIMAL(10,2))),
            2
        ) AS AvgCalories

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

    TotalCalories,
    TotalDuration,
    AvgCalories,

    DENSE_RANK()
    OVER
    (
        ORDER BY TotalCalories DESC
    ) AS OverallRank

FROM UserSummary

ORDER BY OverallRank;
GO
