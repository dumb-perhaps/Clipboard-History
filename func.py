import dearpygui.dearpygui as dpg
import pyperclip

def set_accent(sender):
    color_map = {
        1025: (220, 50, 50, 255),
        1026: (50, 220, 100, 255),
        1027: (50, 100, 220, 255),
        1028: (240, 200, 50, 255),
        1029: (180, 100, 200, 255)
    }

    for cb in [1025, 1026, 1027, 1028, 1029]:
        if cb != sender:
            dpg.set_value(cb, False)

    dpg.set_value("bg_color", color_map[sender])


def open_settings_menu(sender, app_data, user_data):
    if dpg.is_item_shown("settings_menu"):
        dpg.hide_item("settings_menu")
    else:
        dpg.show_item("settings_menu")


def btn_callback(sender):
    config = dpg.get_item_configuration(sender)
    btn_label = config['label']
    pyperclip.copy(btn_label)