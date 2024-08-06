try:
    import os
    import json
    import requests
    import zipfile
    import colorama
    import sys
    import time
    
    print("HI")

except ImportError:
    import os
    import sys
    
    def rest():
        os.system('cls')
        script_name = os.getcwd()
        os.system(script_name)
    
    os.system("pip install json --quiet")
    os.system("cls || clear")
    os.system("pip install requests --quiet")
    os.system("cls || clear")
    os.system("pip install zipfile --quiet")
    os.system("cls || clear")
    os.system("pip install colorama --quiet")
    os.system("cls || clear")
    
    print("Please restart the script")