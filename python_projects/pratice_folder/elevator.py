# User get intro text
# user is asked to make a choice
# user makes a choice, either known or unknown

# if known choice made then user get text that states wher he end s up.
# Where would he like to go "Next"

# if unknown the user is asked to stick to the script

# There are only 3 floors

import time
import copy


def print_pause(list_of_text_to_print, pause_duration=0):
    for text_to_print in list_of_text_to_print:
        print(text_to_print)
        time.sleep(pause_duration)


def intro():
    intro_lines = ["You have just arrived at your new job!", "You are in the elevator."]
    print_pause(intro_lines)


def present_choices(floors_dict):
    intro_text = ["Please enter the number for the floor you would like to visit:"]
    print_pause(intro_text)
    floor_levels = []
    for level, level_data in floors_dict.items():
        floor_levels.append(f"{level}. {level_data['name_u']}")
    print_pause(floor_levels, 0)


# Lets resolve the state upon entry to a level
def level_resolver(floor_index, initial_state, current_state, floors_dict):
    print(initial_state)
    print(current_state)

    current_level = list(floors_dict.keys())[floor_index]
    level_data = floors_dict[current_level]

    # Upon re-entering when a level. This HAS to either True True.
    # False False is not possible since level_resolver for the would not be called if
    # the current level was not visited (i.e. true)
    if initial_state[floor_index] == current_state[floor_index]:
        print_pause(level_data["repeat_text"])
        return current_state

    # Upon entering a level for the first time
    # This is a success ONLY if ALL previous levels have also been visited
    if not initial_state[floor_index] and current_state[floor_index]:
        previous_levels_visited = True
        index = floor_index
        while index > 0:
            print(current_state[index - 1])
            print(index - 1)
            if current_state[index - 1] != True:
                previous_levels_visited = False
                break
            else:
                index -= 1
        if previous_levels_visited:
            print_pause(level_data["success_text"])
            return current_state
        else:
            print_pause(level_data["fail_text"])
            return initial_state

    return current_state


def choice_realization(floors_visited_states_list, floors_dict):
    print("Current visited state list ", floors_visited_states_list)
    new_visited_list = copy.deepcopy(floors_visited_states_list)
    present_choices(floors_dict)
    choice_floor = input().lower()

    if choice_floor not in floors_dict.keys():
        return

    index = 0
    for level, level_data in floors_dict.items():
        if level == choice_floor:
            new_visited_list[index] = True
            user_journey_text = [
                f"You push the button for the {level_data['text']} floor.",
                f"After a few moments, you find yourself in the {level_data['name_l']}.",
                # f"Where would you like to go next?",
            ]
            print_pause(user_journey_text)
            new_visited_list = level_resolver(
                index, floors_visited_states_list, new_visited_list, floors_dict
            )
        index += 1
    if False in new_visited_list:
        choice_realization(new_visited_list, floors_dict)
    else:
        return


if __name__ == "__main__":
    intro()
    floors = {
        "1": {
            "text": "first",
            "name_u": "Lobby",
            "name_l": "lobby",
            "repeat_text": [
                "The clerk greets you, but she has already given you your ID card, so there is nothing more to do here now."
            ],
            "success_text": ["The clerk greets you and gives you your ID card."],
            "fail_text": [],
        },
        "2": {
            "text": "second",
            "name_u": "Human resources",
            "name_l": "human resources department",
            "success_text": [
                "The head of HR greets you.",
                "He looks at your ID card and then gives you a copy of the employee handbook.",
                "You head back to the elevator.",
            ],
            "repeat_text": [
                "The HR folks are busy at their desks.",
                "There doesn't seem to be much to do here.",
                "You head back to the elevator.",
            ],
            "fail_text": [
                "The head of HR greets you.",
                "He has something for you, but says he can't give it to you until you go get your ID card.",
                "You head back to the elevator.",
            ],
        },
        "3": {
            "text": "third",
            "name_u": "Engineering department",
            "name_l": "engineering department",
            "repeat_text": [],
            "success_text": [
                "This is where you work!",
                "You use your ID card to open the door.",
                "Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.",
                "Fortunately, you got that from HR!",
                "Congratulatons! You are ready to start your new job as vice president of engineering!",
            ],
            "fail_text": [
                "This is where you work!",
                "Unfortunately, the door is locked and you can't get in.",
                "It looks like you need some kind of key card to open the door.",
                "You head back to the elevator.",
                "This is where you work!",
                "You use your ID card to open the door.",
                "Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.",
                "They scowl when they see that you don't have it, and send you back to the elevator.",
            ],
        },
    }
    floors_visited_states_list = [False, False, False]
    choice_realization(floors_visited_states_list, floors)
