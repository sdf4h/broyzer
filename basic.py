import tkinter as tk
import webbrowser
from pynput import keyboard

def open_browser(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

def on_activate():
    root = tk.Tk()

    def handle_close():
        root.destroy()

    def submit_query():
        query = entry.get()
        open_browser(query)

    def submit_enter(event):
        submit_query()

    root.protocol("WM_DELETE_WINDOW", handle_close)
    root.title("писькин дрищь")
    root.configure(bg='gray')

    entry = tk.Entry(root)
    entry.bind("<Return>", submit_enter)
    entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_query)
    submit_button.pack()

    root.mainloop()

def on_press(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        global ctrl_pressed
        ctrl_pressed = True
    elif key == keyboard.Key.shift or ctrl_pressed:
        global shift_pressed
        shift_pressed = True

def on_release(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        global ctrl_pressed
        ctrl_pressed = False
    elif key == keyboard.Key.shift:
        global shift_pressed
        if shift_pressed:
            on_activate()
            shift_pressed = False

ctrl_pressed = False
shift_pressed = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()