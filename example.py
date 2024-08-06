from colorama import Fore, Back, Style
import time
import os

PHRASES = "tbc"


def intro():
    print("#######################################")
    print(f"{Fore.RED}NihonGO! {Fore.WHITE}- Learn the REAL Japanese way!\n")
    print(f"Welcome to {Fore.RED}NihonGO! {Fore.WHITE}The best way to learn Japanese!\n")
    print(f"{Fore.LIGHTBLACK_EX}Product Version: 0.0 (Development Access)\n")
    print(f"Loading Modules...\n{Fore.WHITE}")
    print("#######################################")


if __name__ == "__main__":
    intro()