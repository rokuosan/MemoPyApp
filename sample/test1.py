import tkinter as tk
# from tkinter import messagebox as mbox
import pyautogui


# Process
def submit_action():
    pyautogui.alert("Test")


# Make Window
window = tk.Tk()
window.geometry("500x100")
window.title("YouTube-DL GUI")

# Make Label
label_Link = tk.Label(window, text="YouTubeのリンク")
label_Link.pack()

url_Link = tk.Entry(window)
url_Link.pack()

# Make button
submit_btn = tk.Button(window, text="開始")
submit_btn["command"] = submit_action
submit_btn.pack()

# Show
window.mainloop()
