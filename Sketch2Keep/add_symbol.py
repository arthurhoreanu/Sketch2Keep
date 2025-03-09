from turtle import *
import functools

from symbols_dict import write_to_file
from turtle_move import *

inst_dic = {
    "w": move_forward,
    "s": move_back,
    "d": rotate_right,
    "a": rotate_left,
    "f": move_up,
    "g": move_down,
    ".": draw_dot
}
def define_symbol():
    sym = input("Enter the symbol: \n")
    t = turtle.Turtle()
    print("W - Move forward 10 pixels")
    print("S - Move backward 10 pixels")
    print("D - Turn right 45 degrees")
    print("A - Turn left 45 degrees")
    print("F - Pen up")
    print("G - Pen down")

    clear_sym()
    listen()
    for k in 'wasdfg.':
        onkey(functools.partial(event_handler, k, t), k)
    onkey(bye, 'Return')
    mainloop()
    sym_instr = get_sym()
    write_to_file(sym, sym_instr)

def event_handler(key, tur):
    inst_dic[key](tur)