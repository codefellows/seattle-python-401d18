"""
Let's create the classic guessing game I Spy. We'll need...
- A list of things to guess
  - Each thing should be a dictionary with name and hints attributes
  - name is a string
  - hints is a list of strings
"""
things = [
    {
        "solution": "billboard",
        "hints": [
            "bigger than a bread box",
            "rectangular",
            "changes periodically",
            "tells you something",
            "sells you something",
            "often see them in a rush",
        ],
    },
    {
        "solution": "chair",
        "hints": [
            "has multiple legs",
            "has a restful interface",
            "not used in stand up meetings",
            "avoid electric ones",
        ],
    },
    {
        "solution": "mirror",
        "hints": [
            "copies what you do",
            "is always changing color",
            "careful or it will bring you bad luck",
            "never lies to you",
            "fine with mom but not with mama",
        ],
    },
]

# really long line really long line really long line really long line really long line really long line really long line really long line really long line


def guess_a_thing(riddle_index):
    thing = things[riddle_index]

    success = False

    hints = thing["hints"]

    correct_answer = thing["solution"]

    guess = ""

    for hint in hints:

        if guess == correct_answer:
            success = True
            break
        else:
            print(f"Nope, but here's a hint - {hint}")

        guess = input("I spy with my little eye... ")

    if success or guess == correct_answer:
        print("Crushed it")
    else:
        print(f"Too bad. It's a {correct_answer}")


def main():
    riddle_index = 0

    response = ""
    while response != "n":
        guess_a_thing(riddle_index)
        riddle_index += 1
        if riddle_index > 1:
            break
        response = input("Wanna play? ")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
