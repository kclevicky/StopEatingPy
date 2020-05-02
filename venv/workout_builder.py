# muscle_groups.py
"""Build a workout routine for a specified muscle group.
    Available groups: Chest, Back, Biceps, Triceps, Shoulders, Legs.
    A workout will contain at least one exercise from each area of a muscle group.
    Ex: Shoulders will contain at least one of anterior delts, medial delts, and posterior delts.
    Compound lifts will be listed first in the exercise routine.
    Written by Kaleb Levicky"""
import random


class Workout:
    def __init__(self, muscle_group, total_exercises):
        """Build a workout for a specified muscle group using parameters muscle_group (string) and
        total_exercises (int)"""

        self.muscle_group = muscle_group
        self.total_exercises = total_exercises

        # TODO: Move lists outside of initializer to improve memory management
        # chest exercises
        self.chest_exercises = [('bench press', 'Definition'), ('incline press', 'Definition'),
                                ('decline press', 'Definition'), ('dumbbell squeeze press', 'Definition')]

        # shoulder exercises
        self.anterior_delts = [('military press', 'Definition'), ('arnold press', 'Definition'),
                               ('front raise', 'Definition')]  # front delts
        self.medial_delts = [('military press', 'Definition'), ('arnold press', 'Definition'),
                             ('lateral raises', 'Definition')]  # lateral/mid delts
        self.posterior_delts = [('reverse pec dec', 'Definition'), ('face pulls', 'Definition'),
                                ('arnold press', 'Definition')]  # rear delts

        # form a unique list of shoulder exercises
        self.shoulder_exercises = []
        self.shoulder_exercises += self.anterior_delts
        self.shoulder_exercises += self.medial_delts
        self.shoulder_exercises += self.posterior_delts
        self.compound_shoulder_exercises = self.compound(self.shoulder_exercises)
        self.shoulder_exercises = self.unique(self.shoulder_exercises)

        # back exercises
        self.lats = [('lat pulldowns', 'Definition'), ('barbell row', 'Definition'), ('landmine row', 'Definition'),
                     ('seated row', 'Definition')]
        self.traps = [('barbell row', 'Definition'), ('landmine row', 'Definition'), ('seated row', 'Definition')]
        self.rhomboids = [('barbell row', 'Definition'), ('seated row', 'Definition')]
        self.back_exercises = []
        self.back_exercises += self.lats
        self.back_exercises += self.traps
        self.back_exercises += self.rhomboids
        self.compound_back_exercises = self.compound(self.back_exercises)
        self.back_exercises = self.unique(self.back_exercises)

        # bicep exercises
        self.bicep_exercises = [('bicep curls', 'Definition'), ('hammer curls', 'Definition'),
                                ('preacher curls', 'Definition'), ('reverse barbell curls', 'Definition'),
                                ('concentration curls', 'Definition')]

        # tricep exercises
        self.tricep_exercises = [('tricep extensions', 'Definition'), ('skullcrushers', 'Definition'),
                                 ('overhead tricep extensions', 'Definition'), ('tricep pushdown', 'Definition')]

        # leg exercises
        self.quads = [('squats', 'Definition'), ('front squats', 'Definition'), ('deadlift', 'Definition'),
                 ('barbell lunge', 'Definition')]
        self.glutes = [('squats', 'Definition'), ('front squats', 'Definition'), ('deadlift', 'Definition'),
                  ('barbell lunge', 'Definition')]
        self.hamstrings = [('squats', 'Definition'), ('front squats', 'Definition'), ('deadlift', 'Definition'),
                      ('barbell lunge', 'Definition')]
        self.calves = [('calf raises', 'Definition')]
        self.leg_exercises = []
        self.leg_exercises += self.quads
        self.leg_exercises += self.glutes
        self.leg_exercises += self.hamstrings
        self.leg_exercises += self.calves
        self.compound_leg_exercises = self.compound(self.leg_exercises)
        self.leg_exercises = self.unique(self.leg_exercises)

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
        if self.total_exercises > len(self.shoulder_exercises):  # Ensure enough shoulder workouts exist
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
        """Build a back workout with the requested number of total exercises"""
        if self.total_exercises > len(self.back_exercises):  # Ensure enough back workouts exist
            return f'{self.total_exercises} back exercises are not available, choose a number lower than ' \
                   f'{len(self.back_exercises) + 1}.'
        else:
            exercise_routine = []

            # add exercise from lats
            index = random.randrange(0, len(self.lats))
            exercise_routine.append(self.lats[index][0])

            # add exercise from traps
            if self.total_exercises > 1:
                index = random.randrange(0, len(self.traps))
                exercise = self.traps[index][0]
                while exercise in exercise_routine:  # ensure exercise is not already added
                    index = random.randrange(0, len(self.traps))
                    exercise = self.traps[index][0]
                exercise_routine.append(self.traps[index][0])

            # fill remaining exercises
            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.back_exercises))  # choose an exercise
                if self.back_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.back_exercises[index][0])  # append the exercise

            return self.arrange_workout(exercise_routine)

    def build_bicep_workout(self):
        """Build a bicep workout with the requested number of total exercises"""
        if self.total_exercises > len(self.bicep_exercises):  # Ensure enough bicep workouts exist
            return f'{self.total_exercises} bicep exercises are not available, choose a number lower than ' \
                   f'{len(self.bicep_exercises) + 1}'
        else:
            exercise_routine = []

            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.bicep_exercises))  # choose an exercise
                if self.bicep_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.bicep_exercises[index][0])  # append the exercise
            return exercise_routine

    def build_tricep_workout(self):
        """Build a tricep workout with the requested number of total exercises"""
        if self.total_exercises > len(self.tricep_exercises):  # Ensure enough tricep workouts exist
            return f'{self.total_exercises} tricep exercises are not available, choose a number lower than ' \
                   f'{len(self.tricep_exercises) + 1}'
        else:
            exercise_routine = []

            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.tricep_exercises))  # choose an exercise
                if self.tricep_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.tricep_exercises[index][0])  # append the exercise
            return exercise_routine

    def build_leg_workout(self):
        """Build a leg workout with the requested number of total exercises"""
        if self.total_exercises > len(self.leg_exercises):  # Ensure enough leg workouts exist
            return f'{self.total_exercises} leg exercises are not available, choose a number lower than ' \
                   f'{len(self.leg_exercises) + 1}.'
        else:
            exercise_routine = []

            # add exercise from quads
            index = random.randrange(0, len(self.quads))
            exercise_routine.append(self.quads[index][0])

            # add exercise from glutes
            if self.total_exercises > 1:
                index = random.randrange(0, len(self.glutes))
                exercise = self.glutes[index][0]
                while exercise in exercise_routine:  # ensure exercise is not already added
                    index = random.randrange(0, len(self.glutes))
                    exercise = self.glutes[index][0]
                exercise_routine.append(self.glutes[index][0])

            # add exercise from calves
            if self.total_exercises > 2:
                index = random.randrange(0, len(self.calves))
                exercise = self.calves[index][0]
                while exercise in exercise_routine:  # ensure exercise is not already added
                    index = random.randrange(0, len(self.calves))
                    exercise = self.calves[index][0]
                exercise_routine.append(self.calves[index][0])

            # fill remaining exercises
            while len(exercise_routine) < self.total_exercises:  # while the exercise routine is not full
                index = random.randrange(0, len(self.leg_exercises))  # choose an exercise
                if self.leg_exercises[index][0] not in exercise_routine:  # if the exercise is not in the routine
                    exercise_routine.append(self.leg_exercises[index][0])  # append the exercise

            return self.arrange_workout(exercise_routine)

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
        """Arrange a workout ensuring that compound exercises come first"""

        compound_exercises = self.compound_shoulder_exercises + self.compound_back_exercises + \
                             self.compound_leg_exercises
        # rearrange exercise routine with compound exercises first
        for exercise in routine:
            if exercise in compound_exercises:
                routine.remove(exercise)
                routine.insert(0, exercise)
        return routine
