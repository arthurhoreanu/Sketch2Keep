from draw_symbols import draw_str
from add_symbol import define_symbol

def menu():
    print("1. Draw symbol")
    print("2. Add symbol")

    opt = int(input())

    match opt:
        case 1:
            draw_str()
        case 2:
            define_symbol()

menu()