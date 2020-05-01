# muscle_groups.py
"""Build a workout routine for a specified muscle group.
    Available groups: Chest, Back, Biceps, Triceps, Shoulders, legs
    Written by Kaleb Levicky"""
import random


class Workout:
    def __init__(self, muscle_group, total_exercises):
        """Build a workout for a specified muscle group using parameters muscle_group (string) and
        total_exercises (int)"""

        self.muscle_group = muscle_group
        self.total_exercises = total_exercises

        # chest exercises
        self.chest_exercises = [('bench press', 'Definition'), ('incline press', 'Defininition'),
                                ('decline press', 'Definition'), ('dumbbell squeeze press', 'Definition')]

        # shoulder exercises
        self.anterior_delts = [('military press', 'Definition'), ('arnold press', 'Definition'),
                          ('front raise', 'Definition')]  # front delts
        self.medial_delts = [('military press', 'Definition'), ('arnold press', 'Definition'),
                        ('lateral raises', 'Definition')]  # lateral/mid delts
        self.posterior_delts = [('reverse pec dec', 'Definition'), ('face pulls', 'Definition'),
                           ('arnold press', 'Definition')]  # rear delts

        # form a unique list of shoulder exercises
        self.shoulder_exercises = self.anterior_delts
        self.shoulder_exercises += self.medial_delts
        self.shoulder_exercises += self.posterior_delts
        self.compound_shoulder_exercises = self.compound(self.shoulder_exercises)
        self.shoulder_exercises = self.unique(self.shoulder_exercises)

        # back exercises
        lats = {'lat pulldowns': 'Definition', 'barbell row': 'Definition', 'landmine row': 'Definition',
                'seated row': 'Definition'}
        traps = {'barbell row': 'Definition', 'landmine row': 'Definition', 'seated row': 'Definition'}
        rhomboids = {'barbell row': 'Definition', 'seated row': 'Definition'}
        self.back_exercises = (lats, traps, rhomboids)

        # bicep exercises
        self.bicep_exercises = {'bicep curls': 'Definition', 'hammer curls': 'Definition',
                                'preacher curls': 'Definition',
                                'reverse barbell curls': 'Definition', 'concentration curls': 'Definition'}

        # tricep exercises
        self.tricep_exercises = {'tricep extensions': 'Definition', 'skullcrushers': 'Definition',
                                 'overhead tricep extensions': 'Definition', 'tricep pushdown': 'Definition'}

        # leg exercises
        quads = {'squats': 'Definition', 'front squats': 'Definition', 'deadlift': 'Definition',
                 'barbell lunge': 'Definition'}
        glutes = {'squats': 'Definition', 'front squats': 'Definition', 'deadlift': 'Definition',
                  'barbell lunge': 'Definition'}
        hamstrings = {'squats': 'Definition', 'front squats': 'Definition', 'deadlift': 'Definition',
                      'barbell lunge': 'Definition'}
        calves = {'calf raises': 'Definition'}
        self.leg_exercises = (quads, glutes, hamstrings, calves)

    def build_workout(self):
        """Build the workout routine"""
        print('Building workout...')
        switcher = {  # simulate a switch statement
            'chest': self.build_chest_workout(),
            'shoulder': self.build_shoulder_workout(),
            'back': self.build_back_workout(),
            'bicep': self.build_bicep_workout(),
            'tricep': self.build_tricep_workout(),
            'leg': self.build_leg_workout()
        }
        return switcher.get(self.muscle_group, 'Invalid muscle group')  # build workout

    def build_chest_workout(self):
        """Build a chest workout with the requested number of total exercises"""
        if self.total_exercises > len(self.chest_exercises):  # Ensure enough chest workouts exist
            return f'{self.total_exercises} chest exercises are not available, choose a number lower than ' \
                   f'{len(self.chest_exercises) + 1}'
        else:
            exercise_routine = []

            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.chest_exercises))  # choose an exercise
                if self.chest_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.chest_exercises[index][0])  # append the exercise
            return exercise_routine

    def build_shoulder_workout(self):
        """Build a shoulder workout with the requested number of total exercises"""
        if self.total_exercises > len(self.shoulder_exercises):  # Ensure enough chest workouts exist
            return f'{self.total_exercises} shoulder exercises are not available, choose a number lower than ' \
                   f'{len(self.shoulder_exercises) + 1}.'
        else:
            exercise_routine = []

            # add exercise from anterior delts
            index = random.randrange(0, len(self.anterior_delts))
            exercise_routine.append(self.anterior_delts[index][0])

            # add exercise from posterior delts
            if self.total_exercises > 1:
                index = random.randrange(0, len(self.posterior_delts))
                exercise = self.posterior_delts[index][0]
                while exercise in exercise_routine:  # ensure exercise is not already added
                    index = random.randrange(0, len(self.posterior_delts))
                    exercise = self.posterior_delts[index][0]
                exercise_routine.append(self.posterior_delts[index][0])

            # add exercise from medial delts
            if self.total_exercises > 2:
                index = random.randrange(0, len(self.medial_delts))
                exercise = self.medial_delts[index][0]
                while exercise in exercise_routine:  # ensure exercise is not already added
                    index = random.randrange(0, len(self.medial_delts))
                    exercise = self.medial_delts[index][0]
                exercise_routine.append(self.medial_delts[index][0])

            # fill remaining exercises
            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.shoulder_exercises))  # choose an exercise
                if self.shoulder_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.shoulder_exercises[index][0])  # append the exercise

            return self.arrange_workout(exercise_routine)

    def build_back_workout(self):
        pass

    def build_bicep_workout(self):
        pass

    def build_tricep_workout(self):
        pass

    def build_leg_workout(self):
        pass

    def unique(self, list):
        """Return a list of unique values given a list of repeated values"""
        unique_list = []
        for value in list:
            if value not in unique_list:
                unique_list.append(value)
        return unique_list

    def compound(self, list):
        """Return a list of compound exercises"""
        compound_exercises = []

        # build list of compound exercises
        index = 0
        for value in list:
            if (value in list[:index]) and (
                    value[0] not in compound_exercises):  # if the exercise occurs more than once
                compound_exercises.append(value[0])
            index += 1
        return compound_exercises

    def arrange_workout(self, routine):
        """Arrange a workout to ensure that compound exercises come first"""

        # rearrange exercise routine with compound exercises first
        for exercise in routine:
            if exercise in self.compound_shoulder_exercises:
                routine.remove(exercise)
                routine.insert(0, exercise)

        return routine
