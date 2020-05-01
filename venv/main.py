# main.py
"""Program to automatically generate a workout schedule
    Written by Kaleb Levicky"""
import muscle_groups

Chest_Workout = muscle_groups.Workout('chest', 4)
print(Chest_Workout.build_workout())



