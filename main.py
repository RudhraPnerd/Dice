import random
import configs as c


class Dice:
    six_sided_dice = {
        1: """
        . . .
        . • .
        . . .
        """,
        2: """
        • . .
        . . .
        . . •
        """,
        3: """
        • . .
        . • .
        . . •
        """,
        4: """
        • . •
        . . .
        • . •
        """,
        5: """
        • . •
        . • .
        • . •
        """,
        6: """
        • . •
        • . •
        • . •
        """
    }

    twelve_sided_dice = {
        1: """
        . . .
        . • .
        . . .
        """,
        2: """
        • . .
        . . .
        . . •
        """,
        3: """
        • . .
        . • .
        . . •
        """,
        4: """
        • . •
        . . .
        • . •
        """,
        5: """
        • . •
        . • .
        • . •
        """,
        6: """
        • . •
        • . •
        • . •
        """,
        7: """
        • • •
        . • .
        • • •
        """,
        8: """
        • • •
        • . •
        • • •
        """,
        9: """
        • • •
        • • •
        • . •
        """,
        10: """
        • • •
        • • •
        • • •
        """,
        11: """
        • • •
        • • •
        • • •
        """,
        12: """
        • • •
        • • •
        • • •
        """
    }


print(c.GREETING_MESSAGE)

while True:
    dice = input('Which dice do you want to roll? [6/12] ')
    if dice == '6':
        dice_faces = Dice.six_sided_dice
        sides = 6
    elif dice == '12':
        dice_faces = Dice.twelve_sided_dice
        sides = 12
    else:
        print('Invalid input')
        continue  # Skip to the next iteration if input is invalid

    # Roll the dice (random number between 1 and the number of sides)
    roll = random.randint(1, sides)

    # Display the rolled number and the corresponding dice face
    print(f'You rolled a {roll}!')
    content = roll

    with open(c.ROLLS_SAVE_FILE, "w") as file:
        file.write(f"{content}\n")

    print(dice_faces[roll])
