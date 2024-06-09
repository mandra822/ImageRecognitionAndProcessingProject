import tkinter as tk
from tkinter import Toplevel, colorchooser
from tkinter import ttk
import default_settings

lines_displayed = default_settings.lines_displayed
lines_color = default_settings.lines_color
detect_cars = default_settings.detect_cars
detect_pedestrians = default_settings.detect_pedestrians
detect_trucks = default_settings.detect_trucks
cars_color = default_settings.cars_color
pedestrians_color = default_settings.pedestrians_color
trucks_color = default_settings.trucks_color
lines_color_alert = default_settings.lines_color_alert

def open_config_window(root):
    config_window = Toplevel(root)
    config_window.title("Configuration")
    config_window.geometry("400x550")

    config_title = tk.Label(config_window, text="Configuration", font=('Arial', 24))
    config_title.pack(pady=10)

    separator0 = ttk.Separator(config_window, orient='horizontal')
    separator0.pack(fill='x', pady=5)

    display_lines_label = tk.Label(config_window, text="Display lines?", font=('Arial', 12))
    display_lines_label.pack(pady=5)

    display_lines_var = tk.BooleanVar()
    display_lines_var.set(lines_displayed)

    radio_frame = tk.Frame(config_window)
    radio_frame.pack(pady=5)

    display_lines_yes = tk.Radiobutton(radio_frame, text="Yes", variable=display_lines_var, value=True)
    display_lines_yes.pack(side=tk.LEFT, padx=10)

    display_lines_no = tk.Radiobutton(radio_frame, text="No", variable=display_lines_var, value=False)
    display_lines_no.pack(side=tk.LEFT, padx=10)

    temp_lines_color = [lines_color]
    def choose_line_color():
        lines_color_code = colorchooser.askcolor(title="Choose line color")[1]
        if lines_color_code:
            temp_lines_color[0] = tuple(int(lines_color_code[i:i+2], 16) for i in (1, 3, 5))
            lines_color_show.config(bg=lines_color_code)

    lines_color_frame = tk.Frame(config_window)
    lines_color_frame.pack(pady=5)

    lines_color_button = tk.Button(lines_color_frame, text="Choose Lines Color", command=choose_line_color)
    lines_color_button.pack(side=tk.LEFT, padx=10)

    lines_color_show = tk.Button(lines_color_frame, bg='#%02x%02x%02x' % lines_color, width=5)
    lines_color_show.pack(side=tk.LEFT, padx=10)

    separator1 = ttk.Separator(config_window, orient='horizontal')
    separator1.pack(fill='x', pady=10)

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

    temp_cars_color = [cars_color]
    def choose_cars_color():
        cars_color_code = colorchooser.askcolor(title="Choose cars frames color")[1]
        if cars_color_code:
            temp_cars_color[0] = tuple(int(cars_color_code[i:i+2], 16) for i in (1, 3, 5))
            cars_color_show.config(bg=cars_color_code)

    temp_pedestrians_color = [pedestrians_color]
    def choose_pedestrians_color():
        pedestrians_color_code = colorchooser.askcolor(title="Choose pedestrians frames color")[1]
        if pedestrians_color_code:
            temp_pedestrians_color[0] = tuple(int(pedestrians_color_code[i:i+2], 16) for i in (1, 3, 5))
            pedestrians_color_show.config(bg=pedestrians_color_code)

    temp_trucks_color = [trucks_color]
    def choose_trucks_color():
        trucks_color_code = colorchooser.askcolor(title="Choose trucks frames color")[1]
        if trucks_color_code:
            temp_trucks_color[0] = tuple(int(trucks_color_code[i:i+2], 16) for i in (1, 3, 5))
            trucks_color_show.config(bg=trucks_color_code)

    cars_frame = tk.Frame(config_window)
    cars_frame.pack(pady=5)

    pedestrians_frame = tk.Frame(config_window)
    pedestrians_frame.pack(pady=5)

    trucks_frame = tk.Frame(config_window)
    trucks_frame.pack(pady=5)

    cars_color_button = tk.Button(cars_frame, text="Choose Cars Frames Color", command=choose_cars_color)
    cars_color_button.pack(side=tk.LEFT, padx=10)

    cars_color_show = tk.Button(cars_frame, bg='#%02x%02x%02x' % cars_color, width=5)
    cars_color_show.pack(side=tk.LEFT, padx=10)

    pedestrians_color_button = tk.Button(pedestrians_frame, text="Choose Pedestrians Frames Color", command=choose_pedestrians_color)
    pedestrians_color_button.pack(side=tk.LEFT, padx=10)

    pedestrians_color_show = tk.Button(pedestrians_frame, bg='#%02x%02x%02x' % pedestrians_color, width=5)
    pedestrians_color_show.pack(side=tk.LEFT, padx=10)

    trucks_color_button = tk.Button(trucks_frame, text="Choose Trucks Frames Color", command=choose_trucks_color)
    trucks_color_button.pack(side=tk.LEFT, padx=10)

    trucks_color_show = tk.Button(trucks_frame, bg='#%02x%02x%02x' % trucks_color, width=5)
    trucks_color_show.pack(side=tk.LEFT, padx=10)

    separator2 = ttk.Separator(config_window, orient='horizontal')
    separator2.pack(fill='x', pady=10)

    safety_alerts_label = tk.Label(config_window, text="Safety Alerts", font=('Arial', 12))
    safety_alerts_label.pack(pady=5)

    temp_lines_color_alert = [lines_color_alert]
    def choose_line_color_alert():
        lines_color_alert_code = colorchooser.askcolor(title="Choose line color")[1]
        if lines_color_alert_code:
            temp_lines_color_alert[0] = tuple(int(lines_color_alert_code[i:i+2], 16) for i in (1, 3, 5))
            lines_color_alert_show.config(bg=lines_color_alert_code)

    lines_color_alert_frame = tk.Frame(config_window)
    lines_color_alert_frame.pack(pady=5)

    lines_color_alert_button = tk.Button(lines_color_alert_frame, text="Choose Lines Color", command=choose_line_color_alert)
    lines_color_alert_button.pack(side=tk.LEFT, padx=10)

    lines_color_alert_show = tk.Button(lines_color_alert_frame, bg='#%02x%02x%02x' % lines_color_alert, width=5)
    lines_color_alert_show.pack(side=tk.LEFT, padx=10)

    separator3 = ttk.Separator(config_window, orient='horizontal')
    separator3.pack(fill='x', pady=10)

    def apply_settings():
        global lines_displayed, detect_cars, detect_pedestrians, detect_trucks, lines_color, cars_color, pedestrians_color, trucks_color, lines_color_alert
        lines_displayed = display_lines_var.get()
        detect_cars = detect_cars_var.get()
        detect_pedestrians = detect_pedestrians_var.get()
        detect_trucks = detect_trucks_var.get()
        lines_color = temp_lines_color[0]
        cars_color = temp_cars_color[0]
        pedestrians_color = temp_pedestrians_color[0]
        trucks_color = temp_trucks_color[0]
        lines_color_alert = temp_lines_color_alert[0]
        config_window.destroy()

    apply_button = tk.Button(config_window, text="Apply", command=apply_settings)
    apply_button.pack(pady=12)




