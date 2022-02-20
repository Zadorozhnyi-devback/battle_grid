from tkinter import Event, Tk


def closer(_: Event, main_window: Tk) -> None:
    main_window.destroy()
