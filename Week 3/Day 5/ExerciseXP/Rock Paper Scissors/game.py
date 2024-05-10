import random


class Game:

    Win = 1
    Lose = -1
    Draw = 0
    Running = 0

    Game = Running

    def get_user_item(self):
        while True:
            self.user_input = input("Please select an item (rock/paper/scissors): ")
            if self.user_input.lower() in ["rock", "paper", "scissors"]:
                print("You chose", self.user_input)
                break
            else:
                print("Invalid choice. Please select rock, paper, or scissors")

    def get_computer_choice(self):
        self.computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose", self.computer_choice)

    def result_types(self):
        if self.user_input.lower() == self.computer_choice.lower():
            self.Game = self.Draw
        elif (
            (
                self.user_input.lower() == "rock"
                and self.computer_choice.lower() == "scissors"
            )
            or (
                self.user_input.lower() == "paper"
                and self.computer_choice.lower() == "rock"
            )
            or (
                self.user_input.lower() == "scissors"
                and self.computer_choice.lower() == "paper"
            )
        ):
            self.Game = self.Win
        else:
            self.Game = self.Lose
        return

    def get_game_result(self):
        if self.Game == self.Draw:
            return "Draw Game!"
        elif self.Game == self.Win:
            return "You Win!"
        else:
            return "Computer Wins!"

    def play(self):
        self.user_a = self.get_user_item
        self.computer_a = self.get_computer_choice
        self.results = self.get_game_result


play_game = Game()
play_game.get_user_item()
play_game.get_computer_choice()
play_game.result_types()
play_game.get_game_result()
play_game.play()
