from main import display_menu

def get_category_choice(intro_message, valid_categories):
    """
    Prompts the user to input a category choice and validates the input. Will keep asking until a category is
    chosen or the user exits.

    :param intro_message: Quick introduction to explain to the user what they are choosing these options for
    :param valid_categories: A set of valid category names.
    :return: The user's valid category choice.
    """
    while True:
        print("\n" + intro_message + " - these are the categories to choose from:")
        print(" - " + "\n - ".join(valid_categories) + "\n - exit (exit the application)")
        category_choice = input("\nInput the category of statistics you want to search for: ").strip().lower()

        if category_choice == "exit":
            print("\n\n -------------------------EXIT path chosen-------------------------")
            break
        elif category_choice in valid_categories:
            return category_choice
        else:
            print("Invalid choice. Please select one of the following categories:")
            print(" - " + "\n - ".join(valid_categories))

def display_return_to_menu_message():
    key = str(
        input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        display_menu()