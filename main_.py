import dearpygui.dearpygui as dpg
import pyperclip
from func import set_accent
from func import open_settings_menu
from func import btn_callback

history = []
max_history = 50
dpg.create_context()

with dpg.font_registry():
    with dpg.font("/home/nigger/Downloads/Fonts/CascadiaCode/CaskaydiaCoveNerdFontMono-SemiBold.ttf", 16) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range(0x0020, 0x00FF)  # Basic Latin + Latin Supplement
        dpg.add_font_range(0x2000, 0x206F)  # General Punctuation
        dpg.add_font_range(0x2190, 0x21FF)  # Arrows
        dpg.add_font_range(0x2600, 0x26FF)  # Miscellaneous Symbols
        dpg.add_font_range(0x2700, 0x27BF)  # Dingbats
        dpg.add_font_range(0xF000, 0xFFFF)  # Private Use Area (main NerdFont range)
        dpg.add_font_range(0xF0000, 0xFFFFD)  # Supplementary Private Use Area-A
        dpg.add_font_range(0x100000, 0x10FFFD)

dpg.bind_font(default_font)

with dpg.theme(tag="bg_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (50, 50, 150, 255), tag="bg_color")

with dpg.theme(tag="button_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 70, 180, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (90, 90, 200, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (110, 110, 220, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 8)

with dpg.theme(tag="settings_button_theme"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (80, 80, 190, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 120, 220, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (140, 140, 240, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 15)

with dpg.theme(tag="settings_window_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 60, 200))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (100, 100, 200, 150))
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 15, 15)
    with dpg.theme_component(dpg.mvCheckbox):
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (100, 100, 200, 150))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (120, 120, 220, 180))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)





with dpg.window(label="Clipboard Manager", no_title_bar=True, tag="id", width=800, height=400):
    settings_btn = dpg.add_button(label="\uf013", width=35, height=35, callback=open_settings_menu)
    dpg.bind_item_theme(settings_btn, "settings_button_theme")

    with dpg.window(label="Settings", width=220, height=200, show=False, tag="settings_menu",
                    no_title_bar=True, no_resize=True, no_move=True, pos=[10, 50]):
        dpg.add_text("Theme Colors", color=(255, 255, 255, 255))
        dpg.add_separator()
        dpg.add_spacer(height=5)

        dpg.add_checkbox(label="Red", callback=set_accent, tag=1025)
        dpg.add_checkbox(label="Green", callback=set_accent, tag=1026)
        dpg.add_checkbox(label="Blue", callback=set_accent, tag=1027)
        dpg.add_checkbox(label="Yellow", callback=set_accent, tag=1028)
        dpg.add_checkbox(label="Plato Purple", callback=set_accent, tag=1029)

dpg.bind_item_theme("id", "bg_theme")
dpg.bind_item_theme("settings_menu", "settings_window_theme")

dpg.create_viewport(title='Clipboard History Manager', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()

prev_clip = None

while dpg.is_dearpygui_running():
    latest_copied_text = pyperclip.paste()
    if len(history) > max_history:
        history.pop(0)

    if latest_copied_text != prev_clip:
        history.append(latest_copied_text)
        new_btn = dpg.add_button(label=latest_copied_text, callback=btn_callback, parent="id", width=-1)
        dpg.bind_item_theme(new_btn, "button_theme")
        prev_clip = latest_copied_text

    dpg.set_primary_window("id", True)
    dpg.render_dearpygui_frame()

dpg.destroy_context()
