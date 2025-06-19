from tkinter import *
from button_class import My_Button

root = Tk()
root.title("Калькулятор")
root["bg"] = 'white'
root.geometry('280x490')
root.resizable(False, False)
root.bind('q', quit)

res = ''

def on_click(sym):
    global res
    if sym == '=':
        print(res)
        res = ''
    else:
        res += sym

def create_buttons(button_dict, y, root: type[Tk] | None = root):
    return [My_Button(symbol, x, y, root).create_button(on_click) for x, symbol in button_dict.items()]

dict_row_420 = {210: '=', 140: ',', 70: '00', 0: '0'}
dict_row_350 = {210: '+', 140: '3', 70: '2', 0: '1'}
dict_row_280 = {210: '-', 140: '6', 70: '5', 0: '4'}
dict_row_210 = {210: '*', 140: '9', 70: '8', 0: '7'}
dict_row_140 = {210: '/', 140: '%', 70: '()', 0: 'C'}

for i in range(1, 6):
    create_buttons(globals()[f'dict_row_{(i+1)*70}'], (i+1)*70)


#  C ()  %  /
#  7  8  9  *
#  4  5  6  -
#  1  2  3  +
#  0 00  ,  =

if __name__ == "__main__":
    root.mainloop()
