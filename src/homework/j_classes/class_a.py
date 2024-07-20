import random

class Die:
    def __init__(self):
        self._roll_value = None

    def roll(self):
        self._roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self._roll_value
    
    def __str__(self):
        return f"The rolled value is {self._roll_value}"
    

def main():
    die = Die()
    while True:
        die.roll()
        print(die)
        continue_rolling = input("Roll again? (y/n): ").lower()
        if continue_rolling != 'y':
            break

if __name__ == "__main__":
    main()