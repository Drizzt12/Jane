from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN,\
    ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW
from lifxlan import LifxLAN
lx = LifxLAN()
import sys
devices = lx.get_lights()

def change_color(color):
    colors = {
        "red": RED,
        "orange": ORANGE,
        "yellow": YELLOW,
        "green": GREEN,
        "cyan": CYAN,
        "blue": BLUE,
        "purple": PURPLE,
        "pink": PINK,
        "white": WHITE,
        "cold_white": COLD_WHITE,
        "warm_white": WARM_WHITE,
        "gold": GOLD
    }
    if color not in colors:
        print("That is not an accepted color")
    else:
        color = colors[color]
        lx.set_color_all_lights(color=color, rapid=True)

def data():
    print("\nFound {} light(s):\n".format(len(devices)))
    for d in devices:
        print(d)

def get_color():
    for d in devices:
        if d.label == None:
            print("Please run 'lights data' first, to get light data.")
            break
        else:
            print(d.label + ":")
            print(d.color)
