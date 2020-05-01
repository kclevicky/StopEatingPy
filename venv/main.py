# main.py
"""Program to automatically generate a workout schedule
    Written by Kaleb Levicky"""
import workout_builder

Chest_Workout = workout_builder.Workout('shoulder', 4)
print(Chest_Workout.build_workout())



