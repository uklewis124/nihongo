import time
import os
import json
import keyboard
import requests
from colorama import Fore
import sys

def change_user():
    print("Change User")

def main_menu():
    print("Main Menu")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

def intro():
    os.system("cls || clear")
    # Introduction to the Program
    logo = """                                                                          
 #+     #  ++  -:     =-    =+**:   :#=    :=    .*%*-:+%=    -+#**##+.     #%+     
-@%%   .%  %#  #*     @*  :%.  .@=  *@@+   +=    *%*    :-  :#%-    :#%-   +%+      
+@:##  =#  %*  #*    .@+  @-    +@  %%:@=  #=    %%.        #%+      =%%. :%#       
+@  %* *#  %*  %%=++++@= -@:    +%  %* :@- @-   .%#  .--=== #%:      -%%- +%-       
*#   %*%*  #+  %*     @- :@+   .@=  @-  :@=@:    ##. .:*%-- -%+      #%#         
*:    #@=  #=  %-     @   =@+=+%=   %    :%@     :##+=+##    -##=:.-#%*.  %+        
                                                  :===-.      :=+++=:    +%- """
    print_slow(logo)
    print()
    time.sleep(2)
    
    print(f"{Fore.RED}NihonGO! {Fore.WHITE}- Learn the REAL Japanese way!\n")
    print(f"Welcome to {Fore.RED}NihonGO! {Fore.WHITE}The best way to learn Japanese!\n")
    print(f"{Fore.LIGHTBLACK_EX}Product Version: 0.0 (Development Access)\n")
    time.sleep(1)
    print(f"Checking for Updates...\n{Fore.WHITE}")
    time.sleep(4)
    
    # Checking Product is up to date
    import checkver
    checkver.run()
    
    
    # Prepare user data to see who current user is
    USER_JSON = json.load(open("data/users.json"))
    
    time.sleep(1)
    
    print("Welcome back,")
    print(f"Current User: {Fore.RED}{USER_JSON['current_user']['names']['name']}{Fore.WHITE}\n")
    
    print("Press ENTER to login or press 'c' to change user.")
    
    # Check if user wants to change user
    checking = True
    while checking:
        if keyboard.is_pressed("c"):
            checking = False
            os.system("cls || clear")
            change_user()
        elif keyboard.is_pressed("enter"):
            checking = False
            os.system("cls || clear")
            main_menu()


if __name__ == "__main__":
    intro()