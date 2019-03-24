import random


print(''' Welcome to the DnD dice generator. We are going to roll up six stats
    to use for our characters. We roll 4 dice and add the three highest values
    to create the stats. We will save those 6 numbers for later to put in our
    character sheets. In our house we re-roll if the number is less than 2.
    You don't have to worry about that as this generator will not give you a
    2 or 1.''')

rolled_nums = []

        
def roll_dice(rolled_nums):
    
    rolled_nums = []

    for i in range(0, 4):

        dice = 0
        while dice <= 2:

            dice = random.randint(1, 6)

        rolled_nums.append(dice)

    return rolled_nums


print('''Add the three highest values from each roll and you have the scores
      for your stats''')
print(roll_dice(rolled_nums))
print(roll_dice(rolled_nums))
print(roll_dice(rolled_nums))
print(roll_dice(rolled_nums))
print(roll_dice(rolled_nums))
print(roll_dice(rolled_nums))

