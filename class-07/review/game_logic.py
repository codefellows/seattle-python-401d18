from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent
        the user's selected dice pulled out from current roll
        """
        score = 0

        counts = Counter(dice)

        # TODO: handle the special cases of:
        # 1,2,3,4,5,6 (in any order) = 1500
        # 3 pairs = 1500
        # HINT: all the info you need is in counts

        fives_used = False

        ones_used = False

        for num in range(1, 6 + 1):

            occurance_count = counts[num]

            if occurance_count >= 3:

                value_to_add = num * 100
                score = value_to_add
                bonus_occurances = occurance_count - 3
                score += bonus_occurances * value_to_add

                if num == 1:
                    ones_used = True
                    score *= 10

                if num == 5:
                    fives_used = True

        if not ones_used:
            score += counts[1] * 100

        if not fives_used:
            score += counts[5] * 50

        return score


print(GameLogic.calculate_score((1, 1, 3, 1, 3, 4)))

assert GameLogic.calculate_score((1, 2, 3, 2, 3, 4)) == 100
assert GameLogic.calculate_score((1, 1, 3, 2, 3, 4)) == 200
assert GameLogic.calculate_score((4, 6, 5, 2, 3, 4)) == 50
assert GameLogic.calculate_score((4, 6, 5, 2, 3, 1)) == 150

# 4s
assert GameLogic.calculate_score((4, 4, 4, 2, 3, 2)) == 400
assert GameLogic.calculate_score((4, 4, 4, 4, 3, 2)) == 800
assert GameLogic.calculate_score((4, 4, 4, 4, 4, 2)) == 1200
assert GameLogic.calculate_score((4, 4, 4, 4, 4, 4)) == 1600

# 3s
assert GameLogic.calculate_score((3, 3, 4, 4, 3, 2)) == 300
assert GameLogic.calculate_score((3, 3, 4, 3, 3, 2)) == 600
assert GameLogic.calculate_score((3, 3, 3, 3, 4, 3)) == 900
assert GameLogic.calculate_score((3, 3, 3, 3, 3, 3)) == 1200

# 5s
assert GameLogic.calculate_score((5, 3, 4, 4, 3, 2)) == 50
assert GameLogic.calculate_score((5, 3, 4, 5, 3, 2)) == 100
assert GameLogic.calculate_score((5, 3, 5, 2, 5, 3)) == 500
assert GameLogic.calculate_score((3, 5, 5, 3, 5, 5)) == 1000
assert GameLogic.calculate_score((5, 5, 5, 5, 5, 3)) == 1500
assert GameLogic.calculate_score((5, 5, 5, 5, 5, 5)) == 2000


assert GameLogic.calculate_score((1, 1, 3, 1, 3, 4)) == 1000
assert GameLogic.calculate_score((1, 1, 3, 1, 1, 4)) == 2000
assert GameLogic.calculate_score((1, 1, 3, 1, 1, 1)) == 3000
assert GameLogic.calculate_score((1, 1, 1, 1, 1, 1)) == 4000

assert GameLogic.calculate_score((1, 2, 3, 4, 5, 6)) == 1500
assert GameLogic.calculate_score((2, 2, 3, 3, 5, 5)) == 1500

print("TESTS PASSED")
