from tkinter import Canvas


__all__ = (
    'change_text_canvas',
)


def change_text_canvas(canvas: Canvas, text: str) -> None:
    canvas.itemconfig(tagOrId='1', text=text)
