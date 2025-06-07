import random

affirmations = [
    "You are exactly where you need to be.",
    "You are doing better than you think.",
    "You are deeply loved and cherished.",
    "You have the power to make today great.",
    "You are safe and everything is unfolding as it should.",
    "You radiate confidence and calm.",
    "You are enough, exactly as you are.",
    "You are not alone. You are supported."
]

def show_affirmation():
    affirmation = random.choice(affirmations)
    print("\n🌟 Affirmation of the Day:\n")
    print(f'"{affirmation}"\n')

if __name__ == "__main__":
    show_affirmation()