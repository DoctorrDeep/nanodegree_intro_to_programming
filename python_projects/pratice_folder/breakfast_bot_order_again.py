import time



def print_pause(text_to_print, pause_time=2):
    print(text_to_print)
    time.sleep(pause_time)

def intro():
    intro_text = ["Hello! I am Bob, the Breakfast Bot.",
                  "Today we have two breakfasts available.",
                  "The first is waffles with strawberries and whipped cream.",
                  "The second is sweet potato pancakes with butter and syrup.",
                ]
    for a_line in intro_text:
        print_pause(a_line, 2)


def validate_input(prompt, list_of_exepcted_responses, list_of_prints):

    found_valid_response = False
    while True:
        response = input(prompt).lower()
        index = 0
        while index < len(list_of_exepcted_responses):
            if list_of_exepcted_responses[index] in response:
                print_pause(list_of_prints[index], 2)
                found_valid_response = True
                break
            index += 1
        if found_valid_response:
            break
        else:
            print_pause("Sorry, I don't understand.",1)

    return response


def get_order():
    validate_input("\nPlease place your order. Would you like waffles or pancakes?\n", ["waffles", "pancakes"], ["Waffles it is!", "Pancakes it is!"])
    print_pause("Your order will be ready shortly.",1)


def order_again():
    while True:
        response = validate_input("\nWould you like to place another order? \nPlease say 'yes' or 'no'.\n", ["no", "yes"], ["OK,goodbye!", "Very good, I'm happy to take another order."])
        if "no" in response:
            return
        elif "yes" in response:
            get_order()


def order_breakfast():
    intro()
    get_order()
    order_again()


if __name__ == "__main__":
    order_breakfast()
