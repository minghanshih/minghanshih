# Name: Ming Han SHIH

# 1. What goes in?
#    The file scenarios_A.csv. It uses commas to separate the values.
#    The first line is the header with 14 columns: ID, Scenario, the 3 options,
#    the budget change for A B C, the reputation change for A B C, and the feedback for A B C.
#    When a text has a comma inside, it is put between quotes.
#    The numbers are normal whole numbers like -800, but Python reads them as text,
#    so I need int() before I can add them.
#    For option B, I look at BudgetB and ReputationB.
#
# 2. What happens in one day?
#    Show the day and the two gauges.
#    Show the problem of the day and the 3 options.
#    Ask A, B or C. If the player types something else, ask again.
#    Change the budget and the reputation (reputation stops at 100).
#    Show the feedback.
#    Keep the day in my history list.
#    If budget or reputation is 0 or less, the player is fired and the game stops.
#
# 3. What comes out?
#    At the end the player sees if he is fired and why, or his score and his title.
#    He also sees his best move and his worst move.
#    One line of results.csv looks like: MingHan,6350,100,CMO Material,2026-11-03
#
#4. What could go wrong?
#    - The player types something else than A, B or C: I ask again until it is valid.
#    - A gauge goes below zero: the game stops at once and says the player is fired.
#    - The scenario file is missing: I show a message and stop instead of crashing.
#    - The player types a wrong difficulty: I ask again.
#    - The player types an empty name: I use "Player".
# Feature chosen: d, Difficulty (easy 15,000 EUR or hard 6,000 EUR).
# Why: in finance, the starting capital changes the whole strategy. With less money,
# every spending decision matters more, which makes the game replayable.

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS= 10

# Read every scenario of my file and store each option as a tuple
def read_scenarios(filename):
    scenarios = []
    with open(filename, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            options= {}
            for letter in ["A", "B", "C"]:
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
            scenarios.append((row["Scenario"], options))
    return scenarios


# Ask the player for the difficulty: this decides the starting budget
def choose_difficulty():
    answer = input("Difficulty: easy (15,000 EUR) or hard (6,000 EUR)? ").strip().lower()
    while answer not in ["easy", "hard"]:
        answer = input("Please type easy or hard: ").strip().lower()
    if answer == "easy":
        return 15000
    return 6000


# Ask A, B or C until the player gives a valid answer
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ["A", "B", "C"]:
        answer = input("Please type A, B or C: ").strip().upper()
    return answer


# Apply the impact of the chosen option, reputation can never go above 100
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation


# Turn the final score into a title
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    return "Viral Legend"


# Add one line per game to results.csv, with a header if the file is new
def save_result(name, budget, reputation, title):
    try:
        with open(RESULTS_FILE, encoding="utf-8") as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False
    with open(RESULTS_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# The whole game: setup, ten days, then the end screen
def play_game():
    name = input("What is your name? ").strip()
    if name == "":
        name = "Player"

    # Stop politely if the scenario file is missing
    try:
        scenarios = read_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("The file", SCENARIO_FILE, "is missing. Put it next to this program.")
        return

    budget = choose_difficulty()
    reputation = START_REPUTATION

    # Shuffle the scenarios and keep ten days
    random.shuffle(scenarios)
    days = scenarios[:DAYS]

    # History: one tuple per day (reputation change, day, option text)
    history = []
    fired_reason = ""

    for day, (situation, options) in enumerate(days, start=1):
        print()
        print(f"--- Day {day} ---")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(situation)
        for letter in ["A", "B", "C"]:
            print(f"   {letter}: {options[letter][0]}")

        choice = ask_choice()
        option = options[choice]
        budget, reputation = apply_choice(budget, reputation, option)

        # Show what the choice did
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print(f"Budget {budget_change:+} EUR, Reputation {reputation_change:+}")
        history.append((reputation_change, day, text))

        # Fired as soon as one gauge is at 0 or less
        if budget <= 0:
            fired_reason = "the budget is empty"
            break
        if reputation <= 0:
            fired_reason = "the reputation hit zero"
            break

    # End of the game: fired or survived
    print()
    print("==============================")
    if fired_reason != "":
        title = "Fired"
        print(f"You are fired, {name}: {fired_reason}.")
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")

    # Best and worst move: tuples compare their first element, the reputation change
    best = max(history)
    worst = min(history)
    print(f'Best move:  day {best[1]}, "{best[2]}" ({best[0]:+})')
    print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+})')

    save_result(name, budget, reputation, title)
    print("Saved in", RESULTS_FILE)


play_game()