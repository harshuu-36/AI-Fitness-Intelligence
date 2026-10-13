USE AI_Fitness_DB;
GO

/*--------------------------------------------------------------
INDEX 1 - WORKOUTS
--------------------------------------------------------------*/

CREATE NONCLUSTERED INDEX IX_Workouts_User_Date_Covering
ON Workouts (UserID, WorkoutDate)
INCLUDE (WorkoutType, DurationMinutes);
GO

/*--------------------------------------------------------------
INDEX 2 - DIET
--------------------------------------------------------------*/

CREATE NONCLUSTERED INDEX IX_Diet_User_Date
ON Diet (UserID, MealDate)
INCLUDE (CaloriesConsumed, ProteinG, CarbsG, FatG);
GO

/*--------------------------------------------------------------
INDEX 3 - SLEEP
--------------------------------------------------------------*/

CREATE NONCLUSTERED INDEX IX_Sleep_User_Date
ON Sleep (UserID, SleepDate)
INCLUDE (DurationMinutes, SleepQuality);
GO

/*--------------------------------------------------------------
INDEX 4 - DAILY PROGRESS
--------------------------------------------------------------*/

CREATE NONCLUSTERED INDEX IX_DailyProgress_User_Date
ON DailyProgress (UserID, ProgressDate)
INCLUDE (WeightKG);
GO