from menu import MENU

def order(item):
    return item.strip().lower() in MENU
