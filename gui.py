import tkinter as tk
from tkinter import ttk
from subprocess import Popen
import threading

pyprog = 'hand_gesture_detection.py'

def callpy():
    global process
    process = Popen(['python', pyprog])

def quitpy():
    if process:
        process.terminate()

# Initialize main window
root = tk.Tk()
root.title("Hand Gesture Recognition")

# Get screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set window size
root.geometry(f"{int(width / 2)}x{int(height / 1.5)}")

# Create main frame
main_frame = tk.Frame(root, bg="#f0f8ff")
main_frame.pack(expand=True, fill=tk.BOTH)

# Title label
title_label = tk.Label(main_frame, text="REAL-TIME HAND GESTURE RECOGNITION", font=("Arial", 22), bg="#f0f8ff")
title_label.pack(pady=20)

# Buttons frame
button_frame = tk.Frame(main_frame, bg="#f0f8ff")
button_frame.pack(pady=10)

# Start button
start_button = ttk.Button(button_frame, text='Start', command=lambda: threading.Thread(target=callpy).start())
start_button.grid(row=0, column=0, padx=10, pady=10)

# Close button
close_button = ttk.Button(button_frame, text="Close Window", command=root.destroy)
close_button.grid(row=0, column=1, padx=10, pady=10)

# Terminate button
terminate_button = ttk.Button(button_frame, text="Terminate Recogniser", command=quitpy)
terminate_button.grid(row=0, column=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
