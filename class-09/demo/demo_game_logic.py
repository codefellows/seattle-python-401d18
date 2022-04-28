from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(roll):
        return 0  # DANGER: use your calculate_score logic here

    @staticmethod
    def validate_keepers(roll, keepers):

        counted_roll = Counter(roll)

        counted_keepers = Counter(keepers)

        # if you're curious, nice stretch goal
        # print("counter math", counted_keepers - counted_roll)

        for num in counted_keepers:
            if counted_keepers[num] > counted_roll[num]:
                return False

        return True

    @staticmethod
    def get_scorers(roll):
        """
        Turn (1,2,3,1,5)
        Into (1,1,5)



        2,2,2,1,5 == 350 Original score
        2,2,1,5 == 150 # first element counts
        2,2,1,5 == 150 # 2nd element counts
        2,2,1,5 == 150 # 3 element counts
        2,2,2,5 == 250 # 4th element counts

        - iterate through roll values
        - removing one at a time and see if score affected
        - if so add to scorers
        - something like code below
        """

        orig_score = GameLogic.calculate_score(roll)

        scorers = []
        for i in range(roll):
            sub_roll = list(roll)
            sub_roll.pop(i)
            current_score = GameLogic.calculate_score(sub_roll)
            if current_score != orig_score:
                scorers.append(roll[i])

        return scorers


# actual = GameLogic.get_scorers((1,2,3,1,5))
# expected = (1,1,5)
# assert sorted(actual) == sorted(expected)

# actual = GameLogic.get_scorers((2,2,2,3,5))
# expected = (2,2,2,5)
# assert sorted(actual) == sorted(expected)


assert GameLogic.validate_keepers((1, 2, 3, 4), (1, 1, 1, 1, 1, 1)) == False

print("TESTS PASSED")
