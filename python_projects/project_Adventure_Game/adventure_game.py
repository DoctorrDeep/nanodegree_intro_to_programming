"Text based adventure game about defeating supernatural villains in village."
import random
import time
from typing import List

DEBUG_MODE = True


def print_pause(text_list_to_print: List[str], pause_time: int = 2):
    """
    Print a list of strings in new lines with pauses.
    Note: The globally scoped DEBUG_MODE setting
          is to be maniuplated for faster testing
    """
    if DEBUG_MODE:
        pause_time = 0.1
    for a_line in text_list_to_print:
        print(a_line)
        time.sleep(pause_time)


def intro(villain: str):
    """
    Introductory text print to set the story and introduce villain.
    """
    print_pause(
        [
            "You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.",
            f"Rumor has it that a {villain} is somewhere "
            "around here, and has been terrifying the nearby village.",
            "In front of you is a house.",
            "To your right is a dark cave.",
            "In your hand you hold your trusty "
            "(but not very effective) dagger.",
        ]
    )


def validate_input(input_prompt: str, known_inputs: List[str]) -> str:
    """
    Get input from user and retry till it is a valid input.
    Pass the valid input back to where the call came from
    """
    while True:
        user_input = input(input_prompt).lower()
        if user_input not in known_inputs:
            print_pause(["Sorry, did not understand."])
        else:
            break

    return user_input


def cave(weapon: str) -> str:
    """
    Things to be done in cave
    - get sword
    - if already have sword then nothing
    """
    print_pause(["You peer cautiously into the cave."])
    if weapon == "dagger":
        print_pause(
            [
                "It turns out to be only a very small cave.",
                "Your eye catches a glint of metal behind a rock.",
                "You have found the magical Sword of Ogoroth!",
                "You discard your silly old dagger "
                "and take the sword with you.",
            ]
        )
        weapon = "sword"
    elif weapon == "sword":
        print_pause(
            [
                "You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now.",
            ]
        )

    print_pause(["You walk back out to the field."])
    return weapon


def house(villain, weapon):
    """
    Things to do in house:
    - knock and fight
        if you have a sword then in the first instance you win
        else you lose
    - knock and run away
        you go back to village always without ending game
    """
    print_pause(
        [
            "You approach the door of the house.",
            "You are about to knock when the door opens "
            f"and out steps a {villain}.",
            f"Eep! This is the {villain}'s house!",
            f"The {villain} attacks you!",
        ]
    )
    if weapon == "dagger":
        print_pause(
            [
                "You feel a bit under-prepared for this, "
                "what with only having a tiny dagger."
            ]
        )

    fight_choice = validate_input(
        input_prompt="Would you like to (1) fight or (2) run away?",
        known_inputs=["1", "2"],
    )

    if fight_choice == "1":
        if weapon == "dagger":
            print_pause(
                [
                    "You do your best...",
                    "but your dagger is no match for the gorgon.",
                    "You have been defeated!",
                ]
            )
        elif weapon == "sword":
            print_pause(
                [
                    f"As the {villain} moves to attack, "
                    "you unsheath your new sword.",
                    "The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.",
                    f"But the {villain} takes one look at "
                    "your shiny new toy and runs away!",
                    f"You have rid the town of the {villain}. "
                    "You are victorious!",
                ]
            )
            return
        else:
            print(
                "Incorrect weapon state reached: weapon =",
                str(weapon),
                type(weapon),
            )
        return
    if fight_choice == "2":
        print_pause(
            [
                "You run back into the field. Luckily, "
                "you don't seem to have been followed."
            ]
        )
        village(villain, weapon)

    # The following else was made obsolete by "validate_input"
    #     function added after code review #1
    # else:
    #     print_pause(["Sorry, did not understand."])


def village(villain, weapon):
    """
    After every turn in house or cave,
    the player end up here where they can make another turn
    as long as the game is in session
    """
    print_pause(
        [
            "\nEnter 1 to knock on the door of the house.",
            "Enter 2 to peer into the cave.",
            "What would you like to do?",
        ]
    )
    next_step = validate_input(
        input_prompt="(Please enter 1 or 2.)\n", known_inputs=["1", "2"]
    )

    if next_step == "1":
        house(villain, weapon)
    elif next_step == "2":
        weapon = cave(weapon)
        village(villain, weapon)
    # The following else was made obsolete by "validate_input"
    #     function added after code review #1
    # else:
    #     print_pause(["Sorry, did not understand."])


def play_game():
    """
    Each game is started/restarted or ended here.
    Hence, the players' initial setup like weapon, villain name
    is done here.
    """
    villains = ["wicked fairie", "ogre", "pirate", "dragon"]
    villain = random.choice(villains)
    intro(villain)
    village(villain, weapon="dagger")

    play_again = validate_input(
        input_prompt="Would you like to play again? (y/n)",
        known_inputs=["y", "n"],
    )

    if "y" in play_again:
        print_pause(["Excellent! Restarting the game ..."])
        play_game()
    elif "n" in play_again:
        print_pause(["Thanks for playing! See you next time."])
        return
    # The following else was made obsolete by "validate_input"
    #     function added after code review #1
    # else:
    #     print_pause(["Sorry, did not understand."])


# Begin your adventure
play_game()
