import sys

from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    """Class for Ten Thousand Game application"""

    def __init__(self, num_rounds=20):
        """initialize attributes"""
        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=GameLogic.roll_dice):
        """Entry point for playing the game"""
        self._roller = roller

        self.invite_to_play()

        self.play_rounds()

        self.end_game()

    def invite_to_play(self):
        """give user option to play game or not"""

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == "n":
            print("OK. Maybe another time")
            sys.exit()

    def end_game(self):
        """thank user for playing game and exit the application"""

        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def play_rounds(self):
        """play for set number of rounds"""
        while self.round_num < self.num_rounds:
            self.round_num += 1
            self.play_round()

    def play_round(self):
        """play single round of game"""

        self.start_round()

        self.play_turn()

        self.end_round()

    def start_round(self):
        """announce the current round that is starting"""
        print(f"Starting round {self.round_num}")

    def end_round(self):
        """handle the banking and give status update now that round is complete"""
        round_points = self.banker.bank()
        print(f"You banked {round_points} points in round {self.round_num}")
        print(f"Total score is {self.banker.balance} points")

    def play_turn(self):
        """roll dice then collect user choices until a bank, zilch or quit happens"""
        num_dice = 6

        while True:
            roll = self.roll_dice(num_dice)

            if self.is_zilch(roll):
                self.do_zilch()
                return

            keepers = self.collect_keepers(roll)

            num_dice -= len(keepers)

            print(
                f"You have {self.banker.shelved} unbanked points and {num_dice} dice remaining"
            )

            # refresh in case of "hot dice"
            if num_dice == 0:
                num_dice = 6

            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()
            elif response == "b":
                return

    def roll_dice(self, num_dice):
        """roll given number of dice and display it"""
        print(f"Rolling {num_dice} dice...")
        roll = self._roller(num_dice)
        formatted_roll = self.format_roll(roll)
        print(formatted_roll)
        return roll

    def format_roll(self, roll):
        """convert a sequence of dice values into a formatted string"""
        roll_string = " ".join([str(value) for value in roll])
        return f"*** {roll_string} ***"

    def is_zilch(self, roll):
        """check if a zilch has happened"""
        return GameLogic.calculate_score(roll) == 0

    def do_zilch(self):
        """a zilch happened, let user know and handle the banking"""
        self.banker.clear_shelf()

        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

    def collect_keepers(self, roll):
        """get user's choices for which dice to keep from current roll"""
        keeper_values = self.validate_keepers(roll)
        points_for_current_roll = GameLogic.calculate_score(keeper_values)
        self.banker.shelf(points_for_current_roll)
        return keeper_values

    def validate_keepers(self, roll):
        """ensures that kept dice are valid for the roll. Eventually return valid keepers or quits"""
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(self.format_roll(roll))


if __name__ == "__main__":
    game = Game()
    game.play()
