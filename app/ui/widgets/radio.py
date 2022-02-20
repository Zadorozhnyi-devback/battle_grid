from tkinter import StringVar, Tk, Radiobutton, Frame

from settings.ui.const import (
    GRID_SIZE_RADIO_FRAME_COORDS, SEX_RADIO_FRAME_COORDS,
    CATEGORY_TYPE_RADIO_FRAME_COORDS
)


def get_default_radio(window: Tk, value: str) -> StringVar:
    return StringVar(master=window, value=value)


def create_grid_size_radio(
    main_window: Tk, selected_size: StringVar
) -> None:
    radio_frame = Frame(master=main_window)
    radio_frame.grid(**GRID_SIZE_RADIO_FRAME_COORDS, sticky='W')
    radiobutton_8 = Radiobutton(
        master=radio_frame, text='8', value='8',
        variable=selected_size
    )
    radiobutton_16 = Radiobutton(
        master=radio_frame, text='16', value='16',
        variable=selected_size
    )
    radiobutton_32 = Radiobutton(
        master=radio_frame, text='32', value='32',
        variable=selected_size
    )
    radiobutton_4_angles = Radiobutton(
        master=radio_frame, text='4 angles', value='4_angles',
        variable=selected_size
    )
    radiobutton_selection = Radiobutton(
        master=radio_frame, text='selection', value='selection',
        variable=selected_size
    )
    radiobutton_8.grid(column=0, row=0, sticky='W')
    radiobutton_16.grid(column=0, row=0, sticky='E')
    radiobutton_32.grid(column=1, row=0, sticky='W')
    radiobutton_selection.grid(column=0, row=1)
    radiobutton_4_angles.grid(column=1, row=1)


def create_sex_radio(
    main_window: Tk, selected_sex: StringVar
) -> None:
    radio_frame = Frame(master=main_window)
    radio_frame.grid(**SEX_RADIO_FRAME_COORDS, sticky='W')
    radiobutton_male = Radiobutton(
        master=radio_frame, text='male', value='male',
        variable=selected_sex
    )
    radiobutton_female = Radiobutton(
        master=radio_frame, text='female', value='female',
        variable=selected_sex
    )
    radiobutton_male.grid(column=0, row=0)
    radiobutton_female.grid(column=1, row=0)


def create_category_type_radio(window, selected_type: StringVar) -> None:
    radio_frame = Frame(master=window)
    radio_frame.grid(**CATEGORY_TYPE_RADIO_FRAME_COORDS, sticky='W')
    radiobutton_single = Radiobutton(
        master=radio_frame, text='single', value='single',
        variable=selected_type
    )
    radiobutton_crew = Radiobutton(
        master=radio_frame, text='crew', value='crew',
        variable=selected_type
    )
    radiobutton_single.grid(column=0, row=0)
    radiobutton_crew.grid(column=1, row=0)
