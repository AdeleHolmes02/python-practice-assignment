"""
Work Requirement 1 - Python Practice Assignment
Solutions in one file.
"""


# -----------------------------
# Exercise 1: Greeting and Age Check
# -----------------------------
def exercise_1():
    name = input("Enter your name: ").strip()
    age_str = input("Enter your age: ").strip()

    try:
        age = int(age_str)
    except ValueError:
        print("Age must be a whole number (integer).")
        return

    if age >= 18:
        print(f"Hello, {name}! You can enter.")
    else:
        print(f"Hello, {name}! Sorry, you're too young.")


# -----------------------------
# Exercise 3: Sum of User Inputs
# -----------------------------
def exercise_3():
    a_str = input("Enter number 1: ").strip()
    b_str = input("Enter number 2: ").strip()
    c_str = input("Enter number 3: ").strip()

    try:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    except ValueError:
        print("All inputs must be integers.")
        return

    nums = [a, b, c]
    total = a + b + c

    print("Numbers list:", nums)
    print("Total:", total)

    if total % 2 == 0:
        print("Your sum is even!")
    else:
        print("Your sum is odd!")


# -----------------------------
# Exercise 5: Temperature Converter
# -----------------------------
def exercise_5():
    c_str = input("Enter temperature in Celsius: ").strip()

    try:
        celsius = float(c_str)
    except ValueError:
        print("Temperature must be a number (e.g., 21 or 21.5).")
        return

    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is {fahrenheit:.1f}°F")

    if fahrenheit > 80:
        print("It's hot!")
    else:
        print("It's not too hot.")

    temps = [celsius, fahrenheit]
    print("Temperature list:", temps)


# -----------------------------
# Exercise 8: Letter Counter
# -----------------------------
def exercise_8():
    word = input("Enter a word: ").strip().lower()

    if not word:
        print("You entered an empty word.")
        return

    counts = {}
    for ch in word:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    print("Letter counts:", counts)

    if len(word) > 5:
        print("That's a long word!")


# -----------------------------
# Exercise 10: Shopping List Manager
# -----------------------------
def exercise_10():
    shopping_list = []

    while True:
        item = input('Enter an item to add (or type "done" to finish): ').strip()

        if item.lower() == "done":
            break

        if item == "":
            print("Empty item ignored.")
            continue

        shopping_list.append(item)

    print("Shopping list:", shopping_list)

    if len(shopping_list) > 3:
        print("You have a lot of items!")
    else:
        print("You have a short list.")


def main():
    while True:
        print("\n--- Python Practice Assignment ---")
        print("Choose an exercise to run:")
        print("1 - Greeting and Age Check")
        print("3 - Sum of User Inputs")
        print("5 - Temperature Converter")
        print("8 - Letter Counter")
        print("10 - Shopping List Manager")
        print("q - Quit")

        choice = input("Your choice: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break
        elif choice == "1":
            exercise_1()
        elif choice == "3":
            exercise_3()
        elif choice == "5":
            exercise_5()
        elif choice == "8":
            exercise_8()
        elif choice == "10":
            exercise_10()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
