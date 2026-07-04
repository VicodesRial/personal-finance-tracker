import os

def clear_console():
    if os.name == "nt":      # Windows
        os.system("cls")
    else:                    # macOS/Linux
        os.system("clear")

def pause():
    input("\nPress Enter to continue...")