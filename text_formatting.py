def run(file_add, do_i_print):
    import json
    from colorama import Fore, init
    import time
    import os

    # Initialize colorama
    init(autoreset=True)

    # Load JSON data
    with open(file_add, 'r') as file:
        phrases = json.load(file)

    # Mapping of color codes
    color_mapping = {
        "{Fore.RED}": Fore.RED,
        "{Fore.WHITE}": Fore.WHITE,
        "{Fore.LIGHTBLACK_EX}": Fore.LIGHTBLACK_EX,
        "\\n": "\n"
    }

    # Function to replace placeholders with color codes
    def replace_colors(text, mapping):
        for key, value in mapping.items():
            text = text.replace(key, value)
        return text

    # Access the intro data and replace color placeholders
    intro_data = [replace_colors(line, color_mapping) for line in phrases['intro']['data']]

    if do_i_print:
        # Print the formatted intro
        for line in intro_data:
            print(line)

    return intro_data
