import sys


nothing = "-"
cross = "x"
circle = "o"
pattern = "[]"

def pattern_update():
    if e1 is None:
        e1 = nothing
    if e2 is None:
        e2 = nothing
    if e3 is None:
        e3 = nothing
    if e4 is None:
        e4 = nothing
    if e5 is None:
        e5 = nothing
    if e6 is None:
        e6 = nothing
    if e7 is None:
        e7 = nothing
    if e8 is None:
        e8 = nothing
    if e9 is None:
        e9 = nothing
    
    p1 = "[" + e1 + "]"
    p2 = "[" + e2 + "]"
    p3 = "[" + e3 + "]"
    p4 = "[" + e4 + "]"
    p5 = "[" + e5 + "]"
    p6 = "[" + e6 + "]"
    p7 = "[" + e7 + "]"
    p8 = "[" + e8 + "]"
    p9 = "[" + e9 + "]"
    
    pattern = p1, p2, p3, "\n", p4, p5, p6, "\n", p7, p8, p9


def screen_update():    
    print(pattern)
    





op = input("Deine Operation: ")
if op is "print screen":
    pattern_update()
    screen_update()
else:
    sys.exit()