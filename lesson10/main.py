'''
__¶¶¶¶¶¶__¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶_
___¶¶¶¶¶___¶¶¶¶¶¶___¶¶¶¶¶¶_¶¶¶¶¶____¶¶¶¶¶¶¶__¶¶¶¶¶¶¶_
_____¶¶¶____¶¶¶____¶¶¶¶_______¶¶¶____¶¶¶_______¶¶¶___
______¶¶¶__¶¶¶_____¶¶¶_________¶¶¶___¶¶¶_______¶¶¶___
_______¶¶¶¶¶¶_____¶¶¶__________¶¶¶___¶¶¶_______¶¶¶___
________¶¶¶¶______¶¶¶__________¶¶¶___¶¶¶_______¶¶¶___
________¶¶¶_______¶¶¶¶_________¶¶¶___¶¶¶_______¶¶¶___
________¶¶¶________¶¶¶________¶¶¶¶___¶¶¶_______¶¶¶___
________¶¶¶_________¶¶¶¶____¶¶¶¶¶_____¶¶¶_____¶¶¶____
____¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶¶¶¶_____
_____¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶____________¶¶¶¶¶_______
'''
import time
from functools import reduce

CAN_DRAW = {
    "Y" :'''__¶¶¶¶¶¶__¶¶¶¶¶¶¶¶_
___¶¶¶¶¶___¶¶¶¶¶¶__
_____¶¶¶____¶¶¶____
______¶¶¶__¶¶¶_____
_______¶¶¶¶¶¶______
________¶¶¶¶_______
________¶¶¶________
________¶¶¶________
________¶¶¶________
____¶¶¶¶¶¶¶¶¶¶¶____
_____¶¶¶¶¶¶¶¶¶_____
''', "O": '''____¶¶¶¶¶¶¶¶¶_____
__¶¶¶¶¶¶_¶¶¶¶¶____
__¶¶¶¶_______¶¶¶__
__¶¶¶_________¶¶¶_
__¶¶¶__________¶¶¶
__¶¶¶__________¶¶¶
_¶¶¶¶_________¶¶¶_
__¶¶¶________¶¶¶¶_
_¶¶¶_____¶¶¶______
__¶¶¶¶¶¶¶¶¶¶______
_____¶¶¶¶¶¶_______
'''
}

class Char():

    def __init__(self, symb="y"):
        if symb.upper() in CAN_DRAW:
            self.all_rows = CAN_DRAW[symb.upper()].split("\n")
        else:
            raise ValueError

    @property
    def width(self):
        return (len(self.all_rows[0]))

    def get_line(self, i):
        try:
            return self.all_rows[i]
        except:
            return '_' * self.width

class Display():

    def __init__(self, width=20):
        self.width = width
        self.symbols = []

    def add(self, symb):
        if isinstance(symb, Char):
            self.symbols.append(symb)

    @property
    def symbols_width(self):
        total = 0
        for s in self.symbols:
            total += s.width
        return total

    def display(self, shift_val=0):
        for i in range(15):
            str_line = ""
            for s in self.symbols:
                str_line += s.get_line(i)

            print(str_line[shift_val:self.width + shift_val])

d = Display(45)
d.add(Char("y"))
d.add(Char("o"))
d.add(Char("y"))
print(d.symbols_width)

if d.symbols_width > d.width:
    for i in range(d.symbols_width - d.width):
        d.display(i)
        time.sleep(1)
else:
    d.display()
