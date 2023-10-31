############## I DID NOT MAKE THIS ################


import random

def roll_dice(num_dice, num_sides):
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

def main():
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        results = roll_dice(num_dice, num_sides)
        print("You rolled:", results)
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()