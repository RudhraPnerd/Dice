import random
import time
import configs
import configs as c


print(c.GREETING_MESSAGE)

dice = input('How many sides do you want to equip you dice with')

if dice.isalpha():
    print('Invalid')

else:
    pass

def roll_dice(min_val_str, max_val_str):

    min_val = int(min_val_str)
    max_val = int(max_val_str)

    return random.randint(min_val, max_val)

#roll

number_rolled = roll_dice(1, dice)

print(f'You got {number_rolled}!')

try:
    with open(c.ROLLS_SAVE_FILE, 'a') as f:
        f.write(f"Rolled: {number_rolled} on {time.ctime()}")
    print(f"Roll saved to {c.ROLLS_SAVE_FILE}")
except IOError as e:
    print(f"Error saving roll to file: {e}")
