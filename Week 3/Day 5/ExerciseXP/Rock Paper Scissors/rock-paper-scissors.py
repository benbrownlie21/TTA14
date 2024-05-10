from game import Game

results = {}


def get_user_menu_choice():
    while True:
        print("--------MENU--------\nPlay New Game (g)\nShow Scores (s)\nQuit (x)")
        user_input = input("Please choose using (g, s, x): ")
        if user_input == "g":
            main()
        elif user_input == "s":
            print_results(results)
        elif user_input == "x":
            break
        else:
            print("Please input either g, s, or q")


def print_results(results):
    game = Game()
    game_result = game.get_game_result()
    if game_result == "You Win!":
        results["Win"] = results.get("Win", 0) + 1
    elif game_result == "Computer Wins!":
        results["Loss"] = results.get("Loss", 0) + 1
    else:
        results["Draw"] = results.get("Draw", 0) + 1
    print(results)


def main():
    game = Game()
    game.get_user_item()
    game.get_computer_choice()
    game.result_types()
    game_result = game.get_game_result()
    print(game_result)
    return game_result


get_user_menu_choice()
