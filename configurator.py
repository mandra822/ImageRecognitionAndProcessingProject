import tkinter as tk
from tkinter import Toplevel, colorchooser

lines_displayed = False
lines_color = (255, 255, 0)
detect_cars = True
detect_pedestrians = True
detect_trucks = True

def open_config_window(root):
    config_window = Toplevel(root)
    config_window.title("Configuration")
    config_window.geometry("400x400")

    config_title = tk.Label(config_window, text="Configurator", font=('Arial', 24))
    config_title.pack(pady=12)

    display_lines_label = tk.Label(config_window, text="Display lines?", font=('Arial', 12))
    display_lines_label.pack(pady=5)

    display_lines_var = tk.BooleanVar()
    display_lines_var.set(lines_displayed)

    radio_frame = tk.Frame(config_window)
    radio_frame.pack(pady=5)

    def toggle_line_color_chooser(enable):
        if enable:
            lines_color_button.config(state=tk.NORMAL)
        else:
            lines_color_button.config(state=tk.DISABLED)

    display_lines_yes = tk.Radiobutton(radio_frame, text="Yes", variable=display_lines_var, value=True, command=lambda: toggle_line_color_chooser(True))
    display_lines_yes.pack(side=tk.LEFT, padx=10)

    display_lines_no = tk.Radiobutton(radio_frame, text="No", variable=display_lines_var, value=False, command=lambda: toggle_line_color_chooser(False))
    display_lines_no.pack(side=tk.LEFT, padx=10)

    temp_lines_color = [lines_color]
    def choose_line_color():
        lines_color_code = colorchooser.askcolor(title="Choose line color")[1]
        if lines_color_code:
            temp_lines_color[0] = tuple(int(lines_color_code[i:i+2], 16) for i in (1, 3, 5))
            lines_color_show.config(bg=lines_color_code)

    lines_color_frame = tk.Frame(config_window)
    lines_color_frame.pack()

    lines_color_button = tk.Button(lines_color_frame, text="Choose Lines Color", command=choose_line_color, state=tk.DISABLED)
    lines_color_button.pack(side=tk.LEFT, padx=10)

    lines_color_show = tk.Button(lines_color_frame, bg='#%02x%02x%02x' % lines_color, width=5)
    lines_color_show.pack(side=tk.LEFT, padx=10)

    detect_objects_label = tk.Label(config_window, text="Detect which objects?", font=('Arial', 12))
    detect_objects_label.pack(pady=5)

    objects_frame = tk.Frame(config_window)
    objects_frame.pack(pady=5)

    detect_cars_var = tk.BooleanVar()
    detect_cars_var.set(detect_cars)
    detect_cars_cb = tk.Checkbutton(objects_frame, text="Cars", variable=detect_cars_var)
    detect_cars_cb.pack(side=tk.LEFT, padx=10)

    detect_pedestrians_var = tk.BooleanVar()
    detect_pedestrians_var.set(detect_pedestrians)
    detect_pedestrians_cb = tk.Checkbutton(objects_frame, text="Pedestrians", variable=detect_pedestrians_var)
    detect_pedestrians_cb.pack(side=tk.LEFT, padx=10)

    detect_trucks_var = tk.BooleanVar()
    detect_trucks_var.set(detect_trucks)
    detect_trucks_cb = tk.Checkbutton(objects_frame, text="Trucks", variable=detect_trucks_var)
    detect_trucks_cb.pack(side=tk.LEFT, padx=10)


    def apply_settings():
        global lines_displayed, detect_cars, detect_pedestrians, detect_trucks, lines_color
        lines_displayed = display_lines_var.get()
        detect_cars = detect_cars_var.get()
        detect_pedestrians = detect_pedestrians_var.get()
        detect_trucks = detect_trucks_var.get()
        lines_color = temp_lines_color[0]
        config_window.destroy()

    apply_button = tk.Button(config_window, text="Apply", command=apply_settings)
    apply_button.pack(pady=12)






