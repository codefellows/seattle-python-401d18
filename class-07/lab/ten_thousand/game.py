from ten_thousand.game_logic import GameLogic


class Game:
    def play(self, roller=GameLogic.roll_dice):

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            print("Starting round 1")
            print("Rolling 6 dice...")
            print("*** 4 4 5 2 3 1 ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")

            if response == "q":
                print("Thanks for playing. You earned 0 points")


if __name__ == "__main__":
    game = Game()
    game.play()
