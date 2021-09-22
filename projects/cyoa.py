"""A program to determine what number I'm thinking of."""

__author__ = "730350912"


from random import randint


def main() -> None:
    """A introduction to the game."""
    print(greet(x))
    where_to_go: str = input("What do you want to do next? Press '1' to end the experience. Press '2' to continue playing. Press '3' to change the game. ")
    if where_to_go == "1":
        print(end(x))
    if where_to_go == "2":
        print(keep_going(x))
    if where_to_go == "3":
        print(change(x))


def greet(x: str) -> None:
    """A function to greet the player."""
    player == player
    print(f"Welcome, {player}!")
    print("In this game, I'm thinking of a number between 1-10. Every time you guess it correctly, you win 5 adventure points. Every time you guess it incorrectly, you get nothing.")


def end(x: str) -> str:
    """A function end the game."""
    print(f"Alright, {player}, GAME OVER. Through this experience, you accumulated {points} adventure points. Better luck next time!")
    return x


def keep_going(x: str) -> str:
    """A function to continue the game."""
    global points
    global answer_right
    global answer_wrong
    print(f"Alright, {player}, let's play!")
    i = 0
    random = (randint(1, 10))
    number: int = int(input("What number am I thinking of? "))
    while i == 0:
        if number == random:
            points = points + answer_right
            print(f"You have {points} adventure point(s), {player}. Great job!")
            decision: str = input(f"{player}, what do you want to do now? Press '1' to keep playing. Press '2' to quit while you're ahead. ")
            if decision == "1":
                print("Okay. Here we go again \U0001F642")
                points == points + answer_right
                return str(go_on(0))
            if decision == "2":
                print(f"Your loss, {player}. I guess you don't like to have fun. Bye! \U0000270C")
        else:
            points = points + answer_wrong
            print(f"I was feeling generous (even though you suck). You have {points} adventure point(s), {player}. Do better.")
            decision: str = input(f"{player}, what do you want to do now? Press '1' to keep playing. Press '2' to quit while you're ahead. ")
            if decision == "1":
                print("Okay. Here we go again \U0001F642")
                points == points + answer_right
                return str(go_on(0))
            if decision == "2":
                print(f"Your loss, {player}. I guess you don't like to have fun. Bye! \U0000270C ")
        i = i + 1
    return x


def go_on(x: int) -> int:
    """A function if the player still wants to continue the game."""
    global points
    global answer_right
    global answer_wrong
    i = 0
    random = (randint(1, 10))
    number: int = int(input("What number am I thinking of? "))
    while i == 0:
        if number == random: 
            points = points + answer_right
            print(f"You now have {points} adventure points, {player}.")
            decision: str = input(f"Do you still want to play, {player}? Press '1' for yes and '2' for no. ")
            if decision == "1":
                print("Okay. Here we go again.")
                return go_on(x)
            if decision == "2":
                print(f"Your loss, {player}. I guess you don't like to have fun. Bye! \U0000270C{EMOJI}")
        else:
            points = points + answer_wrong
            print(f"You still suck, {player}. You only have {points} adventure points. Do better.")
            decision: str = input(f"Do you still want to play, {player}? Press '1' for yes and '2' for no. ")
            if decision == "1":
                print("Okay. Here we go again.")
                return go_on(x)
            if decision == "2":
                print(f"Your loss, {player}. I guess you don't like to have fun. Bye! \U0000270C{EMOJI}")
        i = i + 1
    return x


def change(x: str) -> str:
    global points
    global answer_right
    global answer_wrong
    """A function to change how the game is played."""
    direction: str = input(f"Are you sure you want to do that, {player}? I promise it's really fun! Press '1' for 'Yes, I'm sure' and '2' for 'No, I'm not sure.' ")
    if direction == "1":
        print(f"Alright, if you say so, {player}. Your loss, though. Now I'm going to make the game even harder. I was going to be nice, but you doubt my game. Now, you can suffer. Instead of having to guess a number between 1 and 10, now it's a number between 1 and 100. Good luck!!!")
        i = 0
        random = (randint(1, 100))
        number: int = int(input("What number am I thinking of? "))
        while i == 0:
            if number == random:
                points = points + answer_right
                print(f"You have {points} adventure points, {player}. Great job!")
            else:
                points = points + answer_wrong
                print(f"I was feeling generous (even though you suck). You have {points} adventure points, {player}. Do better.")
            decision: str = input(f"{player}, what do you want to do now? Press '1' to keep playing. Press '2' to quit while you're ahead. ")
            if decision == "1":
                print("Okay.")
                return str(go_on(0))
            if decision == "2":
                print(f"Your loss, {player}. I guess you don't like to have fun. Bye! \U0000270C{EMOJI}")
            i = i + 1
    if direction == "2":
        print(f"You made the right decision, {player}. You get to have an easier time than the other guys. Good luck with the rest of the game; I'll be here for moral support.")
        return str(keep_going(x))
    return x


player: str = input("Who are you? ")
x: str = ""
answer_right: int = 5
answer_wrong: int = 1
points: int = 0
EMOJI: str = "\U00000000"


if __name__ == "__main__":
    main()