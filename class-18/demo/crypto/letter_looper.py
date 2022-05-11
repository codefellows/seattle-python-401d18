def shift_letter(letter, shift):
    letter_as_num = ord(letter)

    shifted_letter_as_num = letter_as_num + shift

    shifted_letter = chr(shifted_letter_as_num)

    # TODO: not handling "looping back around" at moment. E.g. "z" back to "a"

    return shifted_letter


if __name__ == "__main__":
    actual = shift_letter("z", 1)
    expected = "a"
    assert actual == expected, f"{actual} != {expected}"

    print("TESTS PASSED")
