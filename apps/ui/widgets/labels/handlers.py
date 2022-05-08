from tkinter import Canvas


def change_text_canvas(canvas: Canvas, text: str) -> None:
    # first set coords to default
    canvas.coords('1', 5, 5)
    canvas.itemconfig(tagOrId='1', text=text)
