import tkinter as tk
from tkinter import filedialog
import video_handler

def choose_file(path_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
    if file_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, file_path)

def confirm_and_start(path_chooser_window, path_entry):
    file_path = path_entry.get()
    if file_path:
        path_chooser_window.destroy()  # Close the file chooser window
        video_handler.frameCapture_with_yolo(file_path)

def open_path_chooser():
    path_chooser_window = tk.Tk()
    path_chooser_window.title("Choose video path")

    path_label = tk.Label(path_chooser_window, text="Selected Video Path:")
    path_label.pack()

    path_entry = tk.Entry(path_chooser_window, width=50)
    path_entry.pack()

    choose_file_button = tk.Button(path_chooser_window, text="Choose Video File", command=lambda: choose_file(path_entry))
    choose_file_button.pack()

    confirm_button = tk.Button(path_chooser_window, text="Confirm", command=lambda: confirm_and_start(path_chooser_window, path_entry))
    confirm_button.pack()

    path_chooser_window.mainloop()