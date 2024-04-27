"""Prompt user with question to get tne input."""
import random

def main():
    """Prompt user with question to get tne input."""
    guess = random.randint(1, 100)
    min_number = 1
    max_number = 100

    print("Gissa talet")
    print("Du ska nu gissa ett tal")
    print(f"mellan {min_number} och {max_number}.")

    while True:
        try:
            user_guess = int(input("Skriv in ett tal: \n"))
        except ValueError:
            print("Bokstäver accepteras inte.")
            print(f"Gissa på ett tal mellan {min_number} och {max_number}.")
            continue

        if user_guess < min_number or user_guess > max_number:
            print("Din gissning är utanför spelets gränser.")
            print(f"Gissa på ett tal mellan {min_number} och {max_number}.")
            continue

        if user_guess == guess:
            print("Grattis! Du gissade rätt!")
            print("\nProgrammet är slut")
        else:
            if abs(guess - user_guess) <= 3:
                close_hint = "Du är dock nära och det bränns"
            else:
                close_hint = ""

            if user_guess > guess:
                print("Ditt tal är för stort. Gissa på ett mindre")
                print(close_hint)
            else:
                print("Ditt tal är för litet. Gissa på ett större tal.")
                print(close_hint)

if __name__ == "__main__":
    main()
