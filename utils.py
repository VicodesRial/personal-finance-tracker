import os
from datetime import datetime

def get_current_date():
    auto_date = datetime.now().strftime("%Y-%m-%d")
    return auto_date

def clear_console():
    if os.name == "nt":      
        os.system("cls")
    else:                    
        os.system("clear")

def pause():
    input("\nPress Enter to continue...")