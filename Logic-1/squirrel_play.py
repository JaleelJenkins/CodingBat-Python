'''
squirrel_play - The squirrels in Palo Alto spend most of the day playing. In particular,
the play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then
the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer,
return True if the squirrels play and False otherwise.

Expected Output:
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

'''
def squirrel_play(temp, is_summer):
    if is_summer == True:
        if temp >= 60 and temp <= 100:
            return True
    elif temp >= 60 and temp <= 90:
        return True

    return False
