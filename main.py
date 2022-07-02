from tkinter import *

root = Tk()
root.title('calculator')
root.iconbitmap('Calculator-icon.ico')


def clear():
    entry.delete(0, END)


def btn_clk(num):
    cur_num = entry.get()
    clear()
    f_num = cur_num + num
    entry.insert(0, f_num)


first_num = 0
math = ''
math_sign = ''

ms_list = ['+', '-', '*', '/']


def calc(math_type, ms):
    global first_num, math, math_sign
    math_sign = ms
    math = math_type
    first_num = entry.get()
    for x in ms_list:
        if x in first_num:
            first_num = first_num.replace(x, '')

    clear()
    entry.insert(0, first_num + math_sign)


def equal():
    result = ''
    global first_num, math, math_sign
    second_num = entry.get().replace(str(first_num)+math_sign, '')
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
    entry.insert(0, str(result))


# entry box

entry = Entry(root, width=14, font=('Arial', 28), justify=RIGHT)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# buttons

btn_0 = Button(root, text="0", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('0'))
btn_1 = Button(root, text="1", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('1'))
btn_2 = Button(root, text="2", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('2'))
btn_3 = Button(root, text="3", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('3'))
btn_4 = Button(root, text="4", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('4'))
btn_5 = Button(root, text="5", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('5'))
btn_6 = Button(root, text="6", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('6'))
btn_7 = Button(root, text="7", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('7'))
btn_8 = Button(root, text="8", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('8'))
btn_9 = Button(root, text="9", padx=36, pady=10, font=('Arial', 14), bg="#87cefa", command=lambda: btn_clk('9'))
btn_add = Button(root, text="+", padx=36, bg="pink", pady=10, font=('Arial', 14), command=lambda: calc('add', '+'))
btn_sub = Button(root, text="-", padx=36, bg="pink", pady=10, font=('Arial', 14), command=lambda: calc('sub', '-'))
btn_mul = Button(root, text="*", padx=36, bg="pink", pady=10, font=('Arial', 14), command=lambda: calc('mul', '*'))
btn_div = Button(root, text="/", padx=36, bg="pink", pady=10, font=('Arial', 14), command=lambda: calc('div', '/'))
btn_equal = Button(root, text="=", padx=33, pady=47, bg="light green", font=('Arial', 14), command=equal)
btn_clear = Button(root, text="clear", padx=74, bg="orange", fg='black', pady=10, font=('Arial', 14), command=clear)
# buttons place

btn_0.grid(row=4, column=0, padx=2, pady=10)
btn_1.grid(row=3, column=0, padx=2, pady=10)
btn_2.grid(row=3, column=1, padx=2, pady=10)
btn_3.grid(row=3, column=2, padx=2, pady=10)
btn_4.grid(row=2, column=0, padx=2, pady=10)
btn_5.grid(row=2, column=1, padx=2, pady=10)
btn_6.grid(row=2, column=2, padx=2, pady=10)
btn_7.grid(row=1, column=0, padx=2, pady=10)
btn_8.grid(row=1, column=1, padx=2, pady=10)
btn_9.grid(row=1, column=2, padx=2, pady=10)
btn_0.grid(row=4, column=0, padx=2, pady=10)
btn_add.grid(row=4, column=1, padx=2, pady=10)
btn_sub.grid(row=4, column=2, padx=2, pady=10)
btn_mul.grid(row=5, column=1, padx=2, pady=10)
btn_div.grid(row=5, column=2, padx=2, pady=10)
btn_equal.grid(row=5, column=0, padx=2, pady=10, rowspan=2)
btn_clear.grid(row=6, column=1, padx=2, pady=10, columnspan=2)

root.mainloop()

