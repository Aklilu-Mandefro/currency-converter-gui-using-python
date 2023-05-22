from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

from utils import convert_currency, get_currencies

# Colors
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#333333"
BLUE_COLOR = "#0000FF"


def convert():
    amount = float(amount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    converted_amount = convert_currency(from_currency, to_currency, amount)

    result_label['text'] = f'{to_currency} {converted_amount:.2f}'


# Window Configuration
window = Tk()
window.geometry("300x320")
window.title("Currency Converter")
window.configure(bg=WHITE_COLOR)
window.resizable(height=FALSE, width=FALSE)


# Frames
top_frame = Frame(window, width=300, height=60, bg=BLUE_COLOR)
top_frame.grid(row=0, column=0)

main_frame = Frame(window, width=300, height=260, bg=WHITE_COLOR)
main_frame.grid(row=1, column=0)


# Top Frame Widgets
icon_image = Image.open('icon.png')
icon_image = icon_image.resize((40, 40))
icon_image = ImageTk.PhotoImage(icon_image)
app_name_label = Label(top_frame, image=icon_image, compound=LEFT, text="Currency Converter", height=3, padx=13, pady=30,
                 anchor=CENTER, font=('Arial 16 bold'), bg=BLUE_COLOR, fg=WHITE_COLOR)
app_name_label.place(x=0, y=0)

# Main Frame Widgets
result_label = Label(main_frame, text=" ", width=15, height=2, pady=7, padx=0, anchor=CENTER,
               font=('Ivy 16 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=SOLID)
result_label.place(x=50, y=10)

from_label = Label(main_frame, text="From", width=8, height=1, pady=0, padx=0, anchor=NW,
                   font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
from_label.place(x=48, y=90)
from_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
from_combo['values'] = (get_currencies())
from_combo.current(0)
from_combo.place(x=50, y=115)

to_label = Label(main_frame, text="To", width=8, height=1, pady=0, padx=0, anchor=NW,
                 font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
to_label.place(x=158, y=90)
to_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
to_combo['values'] = (get_currencies())
to_combo.current(1)
to_combo.place(x=160, y=115)

amount_entry = Entry(main_frame, width=22, justify=CENTER,
                    font=('Ivy 12 bold'), relief=SOLID)
amount_entry.place(x=50, y=155)

convert_button = Button(main_frame, text="Convert", width=19, padx=5,
                        height=1, bg=BLUE_COLOR, fg=WHITE_COLOR, font=('Ivy 12 bold'), command=convert)
convert_button.place(x=50, y=210)

# Mainloop
window.mainloop()
