from tkinter import Tk, Label, Button, ttk


def inital_error_window():
    root = Tk()
    label = Label(root, text='Queue List is Empty')
    label.pack()
    button = Button(root, text='Ok', command=root.destroy)
    button.pack()
    root.mainloop()


def wrong_output_error_window():
    root = Tk()
    label = Label(root, text="You didn't pick output")
    label.pack()
    button = Button(root, text='Ok', command=root.destroy)
    button.pack()
    root.mainloop()


def download_completed():
    root = Tk()
    label = Label(root, text="Download completed")
    label.pack()
    button = Button(root, text='Ok', command=root.destroy)
    button.pack()
    root.mainloop()
