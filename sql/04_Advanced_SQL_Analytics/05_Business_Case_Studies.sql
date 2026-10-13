/*====================================================================
Project   : AI Fitness Intelligence Platform
Module    : Business Case Studies
File      : 05_Business_Case_Studies.sql
Case Study: 01 - User Engagement Analysis
Author    : Harsh
Database  : AI_Fitness_DB

Description:
Analyze user engagement and workout activity to help the
management understand platform usage.

====================================================================*/

USE AI_Fitness_DB;
GO

/*=================================================
Case Study 1 — User Engagement Analysis
Business Scenario

The CEO of AI Fitness Intelligence Platform wants answers to the following questions:

Who are the most active users?
Who are the least active users?
Which workout type is the most popular?
Which workout type has the highest average duration?
How many workouts are performed each day?
================================================================================================*/

/*============================================================
Case Study 1 - Task 1
Title : Top 10 Most Active Users
============================================================*/

SELECT TOP (10)
    UserID,
    COUNT(*) AS TotalWorkouts
FROM Workouts
GROUP BY UserID
ORDER BY TotalWorkouts DESC;
GO

/*============================================================
Case Study 1 - Task 2
Title : Top 10 Least Active Users
============================================================*/

SELECT TOP (10)
    UserID,
    COUNT(*) AS TotalWorkouts
FROM Workouts
GROUP BY UserID
ORDER BY TotalWorkouts ASC;
GO

/*============================================================
Case Study 1 - Task 3
Title : Most Popular Workout Type
============================================================*/

SELECT
    WorkoutType,
    COUNT(*) AS TotalSessions
FROM Workouts
GROUP BY WorkoutType
ORDER BY TotalSessions DESC;
GO

/*============================================================
Case Study 1 - Task 4
Title : Average Workout Duration by Workout Type
============================================================*/

SELECT
    WorkoutType,
    ROUND(AVG(DurationMinutes),2) AS AverageDuration
FROM Workouts
GROUP BY WorkoutType
ORDER BY AverageDuration DESC;
GO

/*============================================================
Case Study 1 - Task 5
Title : Daily Workout Trend
============================================================*/

SELECT
    WorkoutDate,
    COUNT(*) AS TotalWorkouts
FROM Workouts
GROUP BY WorkoutDate
ORDER BY WorkoutDate;
GO

/*============================================================
Business Insights

1. UserID 42 is the most active user on the platform with
   244 completed workout sessions, indicating exceptional
   engagement and consistency.

2. Even the least active users in the Top 10 list have
   completed between 48 and 76 workouts, suggesting that
   overall user engagement on the platform is relatively strong.

3. Flexibility workouts are the most popular workout category
   with 19,815 completed sessions, while Mixed workouts have
   the lowest participation among the available workout types.

4. The average workout duration is approximately 44 minutes
   across all workout categories, indicating a standardized
   workout session length within the platform.

5. Daily workout volume remains stable between approximately
   200 and 240 sessions per day, demonstrating consistent
   user activity without major fluctuations.

============================================================*/

/*============================================================
Business Recommendations

1. Reward highly engaged users such as UserID 42 through
   badges, leaderboards, loyalty points, or premium membership
   benefits to encourage long-term retention.

2. Analyze the workout patterns of highly active users and use
   them to build personalized workout recommendations for
   less active members.

3. Increase the promotion of Mixed workout programs through
   personalized recommendations, challenges, and educational
   content to improve participation.

4. Since the average workout duration is already consistent,
   focus on increasing workout frequency and user retention
   rather than extending workout length.

5. Launch fitness challenges and marketing campaigns during
   periods of consistently high daily engagement to maximize
   participation and platform activity.

============================================================*/

/*============================================================
Executive Summary

The analysis indicates a healthy level of user engagement across
the AI Fitness Intelligence Platform. Several users consistently
complete a high number of workouts, demonstrating strong platform
retention. Flexibility is currently the most preferred workout
category, while Mixed workouts present an opportunity for
increased promotion. Daily workout activity remains stable,
suggesting consistent platform usage. Overall, the platform
should focus on rewarding highly engaged users, improving
participation in less popular workout categories, and enhancing
personalized recommendations to further increase user retention.

============================================================*/




/*====================================================================
Project   : AI Fitness Intelligence Platform
Module    : Business Case Studies
Case Study: 02 - User Performance & Engagement Analysis
Author    : Harsh
Database  : AI_Fitness_DB

Description:
Analyze user workout activity to identify highly engaged users,
inactive users, and workout performance trends.

====================================================================*/

USE AI_Fitness_DB;
GO

/*===========================================================================
🏢 Business Scenario

The management team wants to evaluate user engagement and workout performance to improve retention, identify loyal users, and launch personalized fitness campaigns.
====================================================================================================================================================================*/

/*============================================================
Case Study 2 - Task 1
Top 10 Most Active Users
============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalWorkouts
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY TotalWorkouts DESC;
GO

/*============================================================
Business Insights

1. UserID 42 (Stanley Suarez) is the most active user on the
   platform with 244 completed workout sessions, indicating
   excellent engagement and workout consistency.

2. The Top 10 users have completed between 229 and 244 workout
   sessions, showing a strong core group of highly active users.

============================================================*/

/*============================================================
Business Recommendation

• Introduce a loyalty rewards program and monthly leaderboard
  for the most active users to improve retention and motivate
  other users to increase their workout frequency.

============================================================*/

/*============================================================
Case Study 2 - Task 2
Top 5 user by total workout time
============================================================*/

SELECT TOP (5)
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
ORDER BY TotalWorkoutMinutes DESC;
GO

/*============================================================
Case Study 2 - Task 2
Top 5 user by total workout time
============================================================*/

SELECT TOP (5)
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
ORDER BY TotalWorkoutMinutes DESC;
GO

/*============================================================
Business Insights

1. UserID 42 (Stanley Suarez) has accumulated the highest total
   workout duration (11,137 minutes), demonstrating exceptional
   long-term commitment and exercise consistency.

2. The top-performing users have invested over 10,000 workout
   minutes, indicating a highly engaged user segment that can
   serve as role models for community-driven fitness programs.

============================================================*/

/*============================================================
Business Recommendation

• Introduce milestone-based rewards (e.g., 10,000 workout
  minutes badge) and personalized achievement programs to
  recognize highly committed users and encourage long-term
  engagement across the platform.

============================================================*/


/*============================================================
Case Study 2 - Task 3
Total Workout Minutes by Workout Type
============================================================*/

SELECT
    WorkoutType,
    COUNT(*) AS TotalSessions,
    SUM(DurationMinutes) AS TotalWorkoutMinutes,
    ROUND(AVG(DurationMinutes),2) AS AverageWorkoutDuration
FROM Workouts
GROUP BY WorkoutType
ORDER BY TotalWorkoutMinutes DESC;
GO

/*============================================================
Business Insights

1. 885299 recorded the highest total workout minutes,
   indicating that it is the most time-intensive workout
   category among users.

2. The average workout duration helps understand whether
   users prefer shorter high-frequency workouts or longer
   training sessions.

============================================================*/

/*============================================================
Business Recommendation

• Allocate trainers, equipment, and class schedules based on
  the most time-consuming workout category to improve resource
  utilization and user experience.

============================================================*/

/*============================================================
Case Study 2 - Task 4
Peak Workout Days Analysis
Difficulty : ⭐⭐⭐
Concept    : GROUP BY + COUNT + ORDER BY
============================================================*/

SELECT TOP (10)
    WorkoutDate,
    COUNT(*) AS TotalWorkouts,
    SUM(DurationMinutes) AS TotalWorkoutMinutes,
    ROUND(AVG(DurationMinutes),2) AS AverageWorkoutDuration
FROM Workouts
GROUP BY WorkoutDate
ORDER BY TotalWorkouts DESC, TotalWorkoutMinutes DESC;
GO

/*============================================================
Business Insights

1. 11487 recorded the highest number of workout sessions,
   making it the busiest training day in the dataset.

2. Peak workout days indicate periods of high user engagement
   and can help optimize trainer availability and gym resources.

============================================================*/

/*============================================================
Business Recommendation

• Increase trainer availability and equipment allocation on
  peak workout days to reduce waiting time and improve the
  overall user experience.

============================================================*/

/*============================================================
Case Study 2 - Task 5
Average Calories Burned by Workout Type
Difficulty : ⭐⭐⭐
Concept    : AVG + GROUP BY
============================================================*/

SELECT
    WorkoutType,
    COUNT(*) AS TotalSessions,
    ROUND(AVG(CaloriesBurned),2) AS AvgCaloriesBurned,
    MAX(CaloriesBurned) AS MaxCaloriesBurned,
    MIN(CaloriesBurned) AS MinCaloriesBurned
FROM Workouts
GROUP BY WorkoutType
ORDER BY AvgCaloriesBurned DESC;
GO

/*============================================================
Business Insights

1. The CaloriesBurned field contains no valid values, preventing
   calorie-based workout performance analysis.

2. This indicates a data quality issue that should be resolved
   before building dashboards or machine learning models.

============================================================*/

/*============================================================
Business Recommendation

• Validate the ETL pipeline and source data to ensure the
  CaloriesBurned values are correctly imported before
  performing fitness analytics.

============================================================*/

/*============================================================
Case Study 2 - Task 6
Average Workout Duration per User
Difficulty : ⭐⭐⭐
Concept    : AVG + JOIN + GROUP BY
============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(W.WorkoutID) AS TotalSessions,
    ROUND(AVG(W.DurationMinutes),2) AS AvgWorkoutDuration
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY AvgWorkoutDuration DESC,
         TotalSessions DESC;
GO

/*============================================================
Business Insights

1. UserID 371 (Cathy Davidson) has the highest average workout
   duration of 48 minutes per session, indicating a preference
   for longer and more consistent workout sessions.

2. Most of the top users maintain an average workout duration
   between 47–48 minutes, suggesting that highly engaged users
   follow a similar workout pattern.

============================================================*/

/*============================================================
Business Recommendation

• Recommend personalized long-duration workout programs to
  users with higher average session durations and design
  shorter workout plans for users with lower engagement to
  improve overall platform retention.

============================================================*/

/*============================================================
Case Study 2 - Task 7
User Distribution by Workout Type
Difficulty : ⭐⭐⭐
Concept    : GROUP BY + COUNT(DISTINCT)
============================================================*/

SELECT
    WorkoutType,
    COUNT(DISTINCT UserID) AS TotalUsers,
    COUNT(*) AS TotalSessions,
    ROUND(AVG(DurationMinutes),2) AS AvgDuration
FROM Workouts
GROUP BY WorkoutType
ORDER BY TotalUsers DESC;
GO

/*============================================================
Business Insights

1. All 500 users have participated in every workout category,
   indicating complete user coverage across Flexibility,
   Strength, Mixed, and Cardio workouts.

2. Workout sessions and average duration are almost equally
   distributed across all workout types, suggesting a balanced
   synthetic dataset without a dominant workout preference.

============================================================*/

/*============================================================
Business Recommendation

• In future data generation, introduce realistic user behavior
  by varying workout preferences (e.g., some users preferring
  Strength, others Cardio) to produce more meaningful business
  insights and machine learning models.

============================================================*/

/*============================================================
Case Study 2 - Task 8
Users with Highest Workout Consistency
Difficulty : ⭐⭐⭐⭐
Concept    : COUNT(DISTINCT) + GROUP BY
============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    COUNT(DISTINCT W.WorkoutDate) AS ActiveWorkoutDays,
    COUNT(W.WorkoutID) AS TotalWorkouts
FROM Users U
INNER JOIN Workouts W
    ON U.UserID = W.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY
    ActiveWorkoutDays DESC,
    TotalWorkouts DESC;
GO

/*============================================================
Business Insights

1. Stanley Suarez achieved the highest workout consistency by
   completing workouts on 244 unique days, demonstrating
   exceptional long-term engagement.

2. Since ActiveWorkoutDays equals TotalWorkouts for all users,
   the dataset indicates that each user performs only one
   workout session per day, reflecting consistent synthetic
   data generation.

============================================================*/

/*============================================================
Business Recommendation

• Introduce daily workout streaks and consistency badges to
  encourage users to maintain regular workout habits and
  improve long-term engagement.

============================================================*/

/*============================================================
Case Study 2 - Task 9
Monthly Workout Trend
Difficulty : ⭐⭐⭐⭐
Concept    : YEAR() + MONTH() + GROUP BY
============================================================*/

SELECT
    YEAR(WorkoutDate) AS WorkoutYear,
    MONTH(WorkoutDate) AS WorkoutMonth,
    COUNT(*) AS TotalWorkouts,
    COUNT(DISTINCT UserID) AS ActiveUsers,
    ROUND(AVG(DurationMinutes),2) AS AvgWorkoutDuration
FROM Workouts
GROUP BY
    YEAR(WorkoutDate),
    MONTH(WorkoutDate)
ORDER BY
    WorkoutYear,
    WorkoutMonth;
GO

/*============================================================
Business Insights

1. Workout activity is significantly lower in August because
   the dataset begins on 31-Aug-2025, while subsequent months
   represent complete monthly records.

2. From September onwards, the platform consistently maintains
   around 500 active users per month, indicating stable user
   engagement throughout the year.

============================================================*/

/*============================================================
Business Recommendation

• Maintain consistent engagement campaigns throughout the year
  and monitor monthly workout trends to quickly identify any
  decline in user activity and take proactive retention actions.

============================================================*/

/*============================================================
Case Study 2 - Task 10
Executive KPI Summary
Difficulty : ⭐⭐⭐
Concept    : Aggregate Functions
============================================================*/

SELECT
    (SELECT COUNT(*) FROM Users) AS TotalUsers,
    COUNT(*) AS TotalWorkoutSessions,
    SUM(DurationMinutes) AS TotalWorkoutMinutes,
    ROUND(AVG(DurationMinutes),2) AS AvgWorkoutDuration,
    COUNT(DISTINCT WorkoutType) AS WorkoutCategories
FROM Workouts;
GO

/*======================================================================
📋 Executive Summary

This case study analyzed user engagement and workout behavior across the AI Fitness Intelligence Platform. The objective was to identify the most active users, evaluate workout consistency, analyze workout duration trends, and generate actionable business recommendations.

The analysis shows that the platform has 500 active users who completed 78,718 workout sessions, contributing to over 3.5 million workout minutes. A small group of highly engaged users consistently leads platform activity, while monthly engagement remains stable across the dataset.

📈 KPI Summary
KPI	Value
Total Users	500
Total Workout Sessions	78,718
Total Workout Minutes	3,507,930
Average Workout Duration	44 Minutes
Workout Categories	4
💡 Key Business Insights
1. High User Engagement

The platform recorded 78,718 workout sessions from 500 users, indicating strong user participation and consistent platform usage.

2. Strong Core User Base

Users such as Stanley Suarez completed over 240 workout sessions, demonstrating exceptional commitment and making them ideal candidates for loyalty and ambassador programs.

3. Stable Monthly Activity

From September onward, approximately 500 users remained active every month, reflecting strong user retention and consistent engagement.

4. Consistent Workout Duration

The average workout duration is 44 minutes, suggesting users follow a structured exercise routine that aligns with recommended fitness session lengths.

5. Data Quality Observation

The CaloriesBurned column contains only NULL values, preventing calorie-based analytics and affecting future machine learning models. This issue should be resolved by improving the synthetic data generation and ETL process.

🎯 Business Recommendations
1.

Launch a loyalty and rewards program for highly active users to improve long-term retention.

2.

Introduce monthly leaderboards, badges, and workout streaks to motivate consistent participation.

3.

Use personalized workout recommendations based on users' workout duration and engagement history.

4.

Monitor monthly workout trends to detect early signs of declining engagement and launch targeted retention campaigns.

5.

Improve the synthetic data generator to include realistic values for CaloriesBurned, varied workout preferences, and richer behavioral patterns before moving to machine learning and dashboard development.

⚠️ Data Quality Observations
Issue	Impact
CaloriesBurned = NULL	Calorie analytics unavailable
Uniform workout distribution	Less realistic business insights
One workout per day for each user	Limits advanced engagement analysis
🚀 Future Improvements
Add realistic calorie burn calculations.
Simulate different user workout preferences (Cardio, Strength, etc.).
Allow multiple workouts per day for some users.
Include heart rate, steps, and workout intensity.
Build predictive analytics using richer behavioral data.
⭐ Overall Business Conclusion

The platform demonstrates excellent user engagement and consistent workout activity, making it a strong foundation for advanced analytics. Before proceeding to machine learning and Power BI, improving the quality and realism of the synthetic dataset will significantly enhance business insights and predictive model performance.
======================================================================================================================================================================================================================================================================================================================================================*/

/*====================================================================

Project     : AI Fitness Intelligence Platform

Module      : Business Case Studies

Case Study  : 03 - Diet & Nutrition Analytics

Author      : Harsh

Database    : AI_Fitness_DB

Description :

Analyze users' dietary habits to identify high calorie intake,
nutrition patterns, meal trends, and opportunities for
personalized diet recommendations.

====================================================================*/

/*============================================================
Case Study 3 - Task 1

Title       : Top 10 Users by Total Calorie Intake

Difficulty  : ⭐⭐⭐

Concept     : JOIN + SUM + AVG + GROUP BY

Business Requirement:

The nutrition team wants to identify users with the highest
total calorie intake to understand eating habits and design
personalized diet plans.

============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    SUM(D.CaloriesConsumed) AS TotalCaloriesConsumed,
    ROUND(AVG(CAST(D.CaloriesConsumed AS DECIMAL(10,2))),2)
        AS AvgCaloriesPerMeal
FROM Users U
INNER JOIN Diet D
    ON U.UserID = D.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY TotalCaloriesConsumed DESC;
GO

/*============================================================

Case Study 3 - Task 2

Title       : Meal Type Analysis

Difficulty  : ⭐⭐⭐

Concept     : GROUP BY + SUM + AVG

Business Requirement:

The nutrition team wants to identify which meal type
(Breakfast, Lunch, Dinner, Snack) contributes the highest
calorie intake. This analysis helps understand eating
patterns and optimize meal recommendations.

============================================================*/

SELECT
    MealType,
    COUNT(*) AS TotalMeals,
    SUM(CaloriesConsumed) AS TotalCalories,
    ROUND(AVG(CAST(CaloriesConsumed AS DECIMAL(10,2))),2) AS AvgCaloriesPerMeal
FROM Diet
GROUP BY MealType
ORDER BY TotalCalories DESC;
GO

/*============================================================

Business Insights

1. Dinner contributes the highest total calorie intake
   (65,060,571 calories) with an average of 689.47 calories
   per meal, making it the most calorie-dense meal type.

2. Lunch is the second-largest contributor to calorie intake,
   while Breakfast has the lowest average calorie consumption,
   indicating that users consume significantly more calories
   during later meals of the day.

============================================================*/

/*============================================================

Business Recommendation

• Introduce personalized dinner meal plans with healthier
  calorie distribution and encourage users to consume a
  balanced proportion of calories across Breakfast, Lunch,
  and Dinner to improve overall nutrition.

============================================================*/

/*============================================================

Case Study 3 - Task 3

Title       : Macronutrient Analysis

Difficulty  : ⭐⭐⭐

Concept     : SUM + AVG + ROUND

Business Requirement:

The nutrition team wants to analyze the overall consumption
of Protein, Carbohydrates, and Fat to understand users'
nutrition balance and identify dietary patterns.

============================================================*/

SELECT
    SUM(ProteinG) AS TotalProteinG,
    ROUND(AVG(CAST(ProteinG AS DECIMAL(10,2))),2) AS AvgProteinPerMeal,

    SUM(CarbsG) AS TotalCarbsG,
    ROUND(AVG(CAST(CarbsG AS DECIMAL(10,2))),2) AS AvgCarbsPerMeal,

    SUM(FatG) AS TotalFatG,
    ROUND(AVG(CAST(FatG AS DECIMAL(10,2))),2) AS AvgFatPerMeal

FROM Diet;
GO

/*============================================================

Business Insights

1. Carbohydrates are the most consumed macronutrient, with
   a total intake of 2,000,576.6 grams and an average of
   53.04 grams per meal, indicating that users primarily
   rely on carbohydrates as their main energy source.

2. Protein intake averages 26.52 grams per meal, while fat
   intake averages 14.40 grams per meal, suggesting that
   users maintain a moderate protein intake with relatively
   lower fat consumption across their meals.

============================================================*/

/*============================================================

Business Recommendation

• Encourage users to maintain a balanced macronutrient
  distribution by increasing high-quality protein sources
  where needed and promoting healthy fats while avoiding
  excessive carbohydrate intake for better overall nutrition.

============================================================*/

/*============================================================

Case Study 3 - Task 4

Title       : Top Healthy Users by Protein Intake

Difficulty  : ⭐⭐⭐⭐

Concept     : JOIN + SUM + HAVING + GROUP BY + ORDER BY

Business Requirement:

The nutrition team wants to identify users with the highest
protein intake while maintaining a moderate calorie intake.
These users can be considered as following a balanced diet
and may serve as benchmarks for personalized nutrition plans.

============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    SUM(D.ProteinG) AS TotalProteinG,
    SUM(D.CaloriesConsumed) AS TotalCaloriesConsumed
FROM Users U
INNER JOIN Diet D
    ON U.UserID = D.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
HAVING
    SUM(D.CaloriesConsumed) < 250000
ORDER BY
    TotalProteinG DESC;
GO

/*============================================================

Case Study 3 - Task 5

Title       : Executive Nutrition KPI Dashboard

Difficulty  : ⭐⭐⭐⭐

Concept     : Aggregate Functions + COUNT(DISTINCT)

Business Requirement:

The management team requires a nutrition dashboard that
summarizes key performance indicators (KPIs) including total
users, total meals, calorie consumption, macronutrient intake,
and average nutrition metrics to support business decisions.

============================================================*/

SELECT

    COUNT(DISTINCT UserID) AS TotalUsers,

    COUNT(*) AS TotalMeals,

    SUM(CaloriesConsumed) AS TotalCaloriesConsumed,

    ROUND(AVG(CAST(CaloriesConsumed AS DECIMAL(10,2))),2)
        AS AvgCaloriesPerMeal,

    SUM(ProteinG) AS TotalProteinG,

    ROUND(AVG(CAST(ProteinG AS DECIMAL(10,2))),2)
        AS AvgProteinPerMeal,

    SUM(CarbsG) AS TotalCarbsG,

    ROUND(AVG(CAST(CarbsG AS DECIMAL(10,2))),2)
        AS AvgCarbsPerMeal,

    SUM(FatG) AS TotalFatG,

    ROUND(AVG(CAST(FatG AS DECIMAL(10,2))),2)
        AS AvgFatPerMeal

FROM Diet;
GO

/*============================================================

Business Insights

1. The platform recorded 377,070 meals with a total calorie
   consumption of 177,677,023 calories, averaging 471.20
   calories per meal. This indicates a consistent meal size
   across the user base.

2. Users consumed 9,998,968.5g of protein, 20,000,576.6g of
   carbohydrates, and 5,428,084.6g of fat. Carbohydrates
   represent the largest share of macronutrient intake,
   highlighting users' dependence on carbohydrates as their
   primary energy source.

============================================================*/

/*============================================================

Business Recommendation

• Introduce personalized nutrition plans that encourage a
  more balanced macronutrient distribution by increasing
  high-quality protein sources and healthy fats while
  maintaining appropriate carbohydrate intake according to
  users' fitness goals.

============================================================*/


/*====================================================================

Executive Summary

The Diet & Nutrition Analytics module evaluated users'
dietary habits using calorie intake, meal distribution,
and macronutrient consumption. The analysis provides
valuable insights into users' eating patterns and helps
support personalized nutrition planning.

----------------------------------------------------------------------
KPI Summary

• Total Users                  : 500
• Total Meals                  : 377,070
• Total Calories Consumed      : 177,677,023
• Average Calories Per Meal    : 471.20
• Total Protein Intake         : 9,998,968.5 g
• Total Carbohydrate Intake    : 20,000,576.6 g
• Total Fat Intake             : 5,428,084.6 g

----------------------------------------------------------------------
Key Business Insights

1. Dinner contributes the highest calorie intake among all
   meal types, indicating that users consume most of their
   daily calories during evening meals.

2. Carbohydrates are the dominant macronutrient in users'
   diets, while protein and fat intake remain comparatively
   lower.

3. The average meal contains approximately 471 calories,
   suggesting a relatively consistent meal size across the
   platform.

----------------------------------------------------------------------
Business Recommendations

• Promote balanced meal plans with higher-quality protein
  sources and healthy fats.

• Encourage users to distribute calorie intake more evenly
  across Breakfast, Lunch, and Dinner.

• Build personalized nutrition recommendations based on
  users' fitness goals such as weight loss, muscle gain,
  or maintenance.

----------------------------------------------------------------------
Business Impact

This analysis enables nutrition coaches and fitness experts
to identify dietary trends, personalize meal plans, improve
user engagement, and support healthier eating habits across
the platform.

====================================================================*/



/*====================================================================

Project     : AI Fitness Intelligence Platform

Module      : Business Case Studies

Case Study  : 04 - Sleep Analytics

Author      : Harsh

Database    : AI_Fitness_DB

Description :

Analyze users' sleeping patterns to identify sleep quality,
sleep duration trends, and opportunities to improve recovery
and overall fitness performance.

====================================================================*/

/*============================================================

Case Study 4 - Task 1

Title       : Sleep Quality Distribution

Difficulty  : ⭐⭐⭐

Concept     : GROUP BY + COUNT + AVG

Business Requirement:

The management team wants to analyze the distribution of
sleep quality levels across all recorded sleep sessions.
This helps identify the most common sleep quality and
evaluate overall user recovery patterns.

============================================================*/

SELECT
    SleepQuality,
    COUNT(*) AS TotalSleepSessions,
    ROUND(AVG(CAST(DurationMinutes AS DECIMAL(10,2))),2)
        AS AvgSleepDurationMinutes
FROM Sleep
GROUP BY SleepQuality
ORDER BY TotalSleepSessions DESC;
GO

/*============================================================

Business Insights

1. Sleep Quality 8 is the most common rating with 28,050
   recorded sleep sessions, followed closely by Quality 10
   and Quality 9, indicating that most users experience
   good to excellent sleep quality.

2. Higher sleep quality is generally associated with longer
   average sleep duration. Users with Sleep Quality 10
   average 488.93 minutes of sleep, whereas Sleep Quality 1
   averages only 366.00 minutes, suggesting a positive
   relationship between sleep duration and sleep quality.

============================================================*/

/*============================================================

Business Recommendation

• Encourage users with lower sleep quality scores to improve
  their sleep duration through personalized sleep reminders,
  recovery plans, and bedtime recommendations to enhance
  overall health and fitness performance.

============================================================*/

/*============================================================

Case Study 4 - Task 2

Title       : Top 10 Users by Average Sleep Duration

Difficulty  : ⭐⭐⭐

Concept     : JOIN + AVG + GROUP BY + ORDER BY

Business Requirement:

The wellness team wants to identify users with the highest
average sleep duration to recognize healthy sleeping habits
and use them as benchmarks for personalized recovery plans.

============================================================*/

SELECT TOP (10)
    U.UserID,
    U.FirstName,
    U.LastName,
    ROUND(AVG(CAST(S.DurationMinutes AS DECIMAL(10,2))),2)
        AS AvgSleepDurationMinutes,
    COUNT(*) AS TotalSleepSessions
FROM Users U
INNER JOIN Sleep S
    ON U.UserID = S.UserID
GROUP BY
    U.UserID,
    U.FirstName,
    U.LastName
ORDER BY AvgSleepDurationMinutes DESC;
GO

/*============================================================

Business Insights

1. Ashley Richardson has the highest average sleep duration
   at 476.95 minutes across 165 sleep sessions, indicating
   consistent and healthy sleep habits over the recorded
   period.

2. The top 10 users maintain an average sleep duration
   between 470 and 477 minutes while recording more than
   160 sleep sessions each, suggesting long-term consistency
   rather than occasional longer sleep durations.

============================================================*/

/*============================================================

Business Recommendation

• Identify the daily routines and lifestyle patterns of
  high-performing sleepers and use these insights to create
  personalized sleep improvement plans and recovery
  recommendations for users with lower average sleep
  durations.

============================================================*/

/*============================================================

Case Study 4 - Task 3

Title       : Sleep Duration vs Sleep Quality Analysis

Difficulty  : ⭐⭐⭐⭐

Concept     : GROUP BY + AVG + COUNT + ORDER BY

Business Requirement:

The wellness team wants to analyze whether longer sleep
duration is associated with better sleep quality. This
analysis helps validate recovery patterns and improve
personalized sleep recommendations.

============================================================*/

SELECT
    SleepQuality,
    COUNT(*) AS TotalSleepSessions,
    ROUND(AVG(CAST(DurationMinutes AS DECIMAL(10,2))),2)
        AS AvgSleepDurationMinutes,
    MIN(DurationMinutes) AS MinSleepDuration,
    MAX(DurationMinutes) AS MaxSleepDuration
FROM Sleep
GROUP BY SleepQuality
ORDER BY SleepQuality DESC;
GO

/*============================================================

Business Insights

1. Users with Sleep Quality 10 recorded the highest average
   sleep duration of 488.93 minutes, while users with Sleep
   Quality 1 averaged only 366.00 minutes. This indicates a
   strong positive relationship between longer sleep duration
   and better sleep quality.

2. Most sleep sessions are concentrated within Sleep Quality
   scores of 7 to 10, accounting for the majority of recorded
   data. This suggests that most users maintain good sleep
   habits, while very poor sleep quality (Levels 1–3) is
   relatively uncommon.

============================================================*/

/*============================================================

Business Recommendation

• Implement personalized sleep coaching for users with
  Sleep Quality below 7 by providing bedtime reminders,
  recovery tips, and sleep hygiene recommendations to
  improve both sleep duration and overall sleep quality.

============================================================*/

/*============================================================

Case Study 4 - Task 5

Title       : Executive Sleep KPI Dashboard

Difficulty  : ⭐⭐⭐⭐

Concept     : Aggregate Functions + COUNT(DISTINCT)

Business Requirement:

The management team requires an executive dashboard to
summarize overall sleep performance, including total users,
sleep sessions, average sleep duration, average sleep quality,
and sleep duration range to support wellness initiatives.

============================================================*/

SELECT

    COUNT(DISTINCT UserID) AS TotalUsers,

    COUNT(*) AS TotalSleepSessions,

    ROUND(AVG(CAST(DurationMinutes AS DECIMAL(10,2))),2)
        AS AvgSleepDurationMinutes,

    ROUND(AVG(CAST(SleepQuality AS DECIMAL(10,2))),2)
        AS AvgSleepQuality,

    MIN(DurationMinutes) AS MinSleepDuration,

    MAX(DurationMinutes) AS MaxSleepDuration,

    SUM(DurationMinutes) AS TotalSleepMinutes

FROM Sleep;
GO

/*============================================================

Business Insights

1. The platform recorded 116,335 sleep sessions across
   500 users, with an average sleep duration of 461.75
   minutes (approximately 7.7 hours), indicating that
   most users achieve the recommended amount of sleep.

2. The average sleep quality is 8.08 out of 10, while
   sleep duration ranges from 210 to 660 minutes. This
   suggests that although overall sleep quality is good,
   there are users with extremely short and very long
   sleep durations who may require personalized guidance.

============================================================*/

/*============================================================

Business Recommendation

• Continue promoting healthy sleep habits while providing
  personalized sleep improvement plans for users with
  below-average sleep quality or unusually short sleep
  durations to improve recovery and overall fitness.

============================================================*/

/*====================================================================

Executive Summary

The Sleep Analytics module evaluated users' sleeping
patterns to understand sleep duration, sleep quality,
and recovery trends. The analysis helps identify healthy
sleep behaviors and supports personalized wellness
recommendations.

----------------------------------------------------------------------
KPI Summary

• Total Users                : 500
• Total Sleep Sessions       : 116,335
• Average Sleep Duration     : 461.75 Minutes
• Average Sleep Quality      : 8.08 / 10
• Minimum Sleep Duration     : 210 Minutes
• Maximum Sleep Duration     : 660 Minutes
• Total Sleep Minutes        : 53,716,765

----------------------------------------------------------------------
Key Business Insights

1. Most users maintain healthy sleep habits, with an
   average sleep duration of approximately 7.7 hours.

2. Sleep quality improves as average sleep duration
   increases, indicating a positive relationship between
   adequate sleep and recovery.

3. Sleep Quality scores between 8 and 10 account for the
   majority of recorded sleep sessions, reflecting overall
   strong recovery patterns across the platform.

----------------------------------------------------------------------
Business Recommendations

• Encourage users with below-average sleep duration to
  follow personalized bedtime schedules and recovery plans.

• Send smart sleep reminders and recovery notifications
  to improve sleep consistency.

• Use sleep analytics to personalize workout intensity
  and recovery recommendations.

----------------------------------------------------------------------
Business Impact

This analysis enables fitness coaches and wellness teams
to monitor recovery trends, improve user engagement, and
deliver personalized sleep recommendations that enhance
overall health and fitness performance.

====================================================================*/

/*====================================================================

Project     : AI Fitness Intelligence Platform

Module      : Business Case Studies

Case Study  : 05 - User Progress & Goal Achievement Analytics

Author      : Harsh

Database    : AI_Fitness_DB

Description :

Analyze users' daily weight progress to monitor fitness
improvement, identify successful users, and evaluate
overall progress trends. This analysis helps fitness
coaches track user performance and improve engagement.

====================================================================*/

/*============================================================

Case Study 5 - Task 1

Title       : Top 10 Users with Highest Weight Progress Records

Difficulty  : ⭐⭐⭐

Concept     : JOIN + COUNT + GROUP BY + ORDER BY

Business Requirement:

The fitness team wants to identify users who consistently
track their weight progress. Frequent progress tracking
indicates higher engagement and commitment towards
fitness goals.

============================================================*/

SELECT TOP (10)

    U.UserID,
    U.FirstName,
    U.LastName,

    COUNT(DP.ProgressID) AS TotalProgressRecords

FROM Users U

INNER JOIN DailyProgress DP
ON U.UserID = DP.UserID

GROUP BY

    U.UserID,
    U.FirstName,
    U.LastName

ORDER BY TotalProgressRecords DESC;
GO

/*============================================================

Business Insights

1. Lori Winters recorded the highest number of weight
   progress entries (301), demonstrating exceptional
   consistency in tracking fitness progress over time.

2. The top 10 users have between 282 and 301 progress
   records, indicating that highly engaged users regularly
   monitor their fitness journey and are more committed to
   achieving their health goals.

============================================================*/

/*============================================================

Business Recommendation

• Encourage all users to log their daily progress
  consistently by introducing streak rewards, progress
  badges, and reminder notifications to improve long-term
  engagement and goal achievement.

============================================================*/

/*============================================================

Case Study 5 - Task 2

Title       : Average Weight Trend Analysis

Difficulty  : ⭐⭐⭐

Concept     : GROUP BY + AVG + ORDER BY

Business Requirement:

The fitness management team wants to analyze the average
weight trend over time to understand whether users are
making consistent progress in their fitness journey. This
analysis helps evaluate overall platform effectiveness and
supports long-term health improvement strategies.

============================================================*/

SELECT

    ProgressDate,

    ROUND(AVG(CAST(WeightKG AS DECIMAL(10,2))),2)
        AS AvgWeightKG,

    COUNT(DISTINCT UserID) AS ActiveUsers

FROM DailyProgress

GROUP BY ProgressDate

ORDER BY ProgressDate;
GO

/*============================================================

Case Study 5 - Task 3

Title       : Top 10 Users with Highest Weight Improvement

Difficulty  : ⭐⭐⭐⭐

Concept     : CTE + MIN + MAX + JOIN + GROUP BY + ORDER BY

Business Requirement:

The fitness management team wants to identify users who
have achieved the highest weight reduction during their
fitness journey. This analysis helps recognize successful
transformations and evaluate the effectiveness of fitness
programs.

============================================================*/

WITH UserWeightProgress AS
(
    SELECT
        UserID,
        MIN(WeightKG) AS LowestWeight,
        MAX(WeightKG) AS HighestWeight
    FROM DailyProgress
    GROUP BY UserID
)

SELECT TOP (10)

    U.UserID,
    U.FirstName,
    U.LastName,

    HighestWeight,
    LowestWeight,

    ROUND(HighestWeight - LowestWeight,2)
        AS WeightLossKG

FROM UserWeightProgress P

INNER JOIN Users U
ON P.UserID = U.UserID

ORDER BY WeightLossKG DESC;
GO

/*============================================================

Business Insights

1. Emily Garcia achieved the highest recorded weight loss
   of 11.10 KG, demonstrating outstanding progress in her
   fitness journey and consistent commitment to her goals.

2. The top 10 users achieved weight reductions ranging
   from 10.30 KG to 11.10 KG, indicating that the platform's
   fitness programs are capable of supporting significant
   and measurable health improvements.

============================================================*/

/*============================================================

Business Recommendation

• Recognize users with significant weight improvement
  through achievement badges and transformation stories.
  Use their success patterns to build personalized coaching
  programs and motivate other users to remain consistent
  with their fitness journey.

============================================================*/

/*============================================================

Case Study 5 - Task 4

Title       : Monthly Weight Progress Analysis

Difficulty  : ⭐⭐⭐⭐

Concept     : YEAR() + MONTH() + AVG() + COUNT(DISTINCT)

Business Requirement:

The fitness management team wants to analyze monthly
weight trends and user participation to monitor overall
fitness progress. This analysis helps identify seasonal
patterns and measure user engagement over time.

============================================================*/

SELECT

    YEAR(ProgressDate) AS ProgressYear,

    MONTH(ProgressDate) AS ProgressMonth,

    COUNT(DISTINCT UserID) AS ActiveUsers,

    COUNT(*) AS TotalProgressRecords,

    ROUND(AVG(CAST(WeightKG AS DECIMAL(10,2))),2)
        AS AvgWeightKG

FROM DailyProgress

GROUP BY

    YEAR(ProgressDate),
    MONTH(ProgressDate)

ORDER BY

    ProgressYear,
    ProgressMonth;
GO

/*============================================================

Case Study 5 - Task 5

Title       : Executive Progress KPI Dashboard

Difficulty  : ⭐⭐⭐⭐

Concept     : Aggregate Functions + COUNT(DISTINCT)

Business Requirement:

The management team requires an executive dashboard to
summarize user progress tracking, weight statistics, and
overall platform engagement. These KPIs help evaluate the
effectiveness of the fitness tracking program.

============================================================*/

SELECT

    COUNT(DISTINCT UserID) AS TotalUsers,

    COUNT(*) AS TotalProgressRecords,

    ROUND(AVG(CAST(WeightKG AS DECIMAL(10,2))),2)
        AS AvgWeightKG,

    MIN(WeightKG) AS LowestRecordedWeight,

    MAX(WeightKG) AS HighestRecordedWeight,

    SUM(WeightKG) AS TotalWeightRecorded

FROM DailyProgress;
GO

/*============================================================

Business Insights

1. The platform recorded 97,981 weight progress records
   from 500 users, with an average recorded weight of
   73.90 KG. This indicates strong user participation in
   tracking fitness progress.

2. Recorded weights range from 40.00 KG to 119.40 KG,
   covering users with diverse fitness profiles. This
   highlights the need for personalized fitness plans
   instead of a one-size-fits-all approach.

============================================================*/

/*============================================================

Business Recommendation

• Continue encouraging users to log their weight regularly
  through reminders, progress dashboards, and milestone
  rewards. Use historical weight trends to provide
  personalized coaching and improve long-term engagement.

============================================================*/

/*====================================================================

Executive Summary

The User Progress Analytics module evaluated daily weight
tracking records to measure user engagement, monitor
fitness improvements, and identify overall progress
trends. The analysis supports data-driven coaching and
personalized fitness recommendations.

----------------------------------------------------------------------
KPI Summary

• Total Users               : 500
• Total Progress Records    : 97,981
• Average Weight            : 73.90 KG
• Lowest Recorded Weight    : 40.00 KG
• Highest Recorded Weight   : 119.40 KG
• Total Weight Recorded     : 7,240,512.00 KG

----------------------------------------------------------------------
Key Business Insights

1. Users actively track their fitness progress, with nearly
   98,000 progress records collected across the platform.

2. The average recorded weight of 73.90 KG provides a
   useful benchmark for monitoring overall user progress.

3. The wide weight range (40.00–119.40 KG) indicates that
   users have diverse fitness goals and require personalized
   recommendations.

----------------------------------------------------------------------
Business Recommendations

• Encourage consistent progress tracking through reminder
  notifications and achievement badges.

• Build personalized weight-loss and weight-gain programs
  based on historical progress data.

• Integrate progress analytics with workout and nutrition
  recommendations to improve overall fitness outcomes.

----------------------------------------------------------------------
Business Impact

Daily progress analytics helps fitness coaches measure
user engagement, evaluate program effectiveness, and
deliver personalized recommendations that improve user
retention and long-term fitness success.

====================================================================*/