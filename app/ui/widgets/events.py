from tkinter import Event, Tk, messagebox


def closer(_: Event, main_window: Tk) -> None:
    answer = messagebox.askyesno(message=f"close battle grid?")
    if answer:
        main_window.destroy()
