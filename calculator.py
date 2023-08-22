import tkinter as tk
import math

def calculate(method):
    try:
        angle = float(entry_angle.get())
    except ValueError:
        label_result.config(text="Please enter a valid angle", font=("Times New Roman", 15))
        return

    if angle:
        trig_functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sec": lambda x: 1 / math.cos(x),
            "cosec": lambda x: 1 / math.sin(x),
            "cot": lambda x: 1 / math.tan(x)
        }

        trig_func = trig_functions[method]
        trig_val = round(trig_func(math.radians(angle)), 4)

        label_result.config(text=f"{method.upper()}({angle}°) = {trig_val}", font=("Times New Roman", 15))
    else:
        label_result.config(text="Please enter a valid angle", font=("Times New Roman", 15))

def clear_result():
    label_result.config(text="", font=("Times New Roman", 15))
    entry_angle.delete(0, "end")

#main window
root = tk.Tk()
root.title("Trigonometric Calculator")
root.configure(bg="lightpink")

root.resizable(False, False)

#dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#window position
window_width = 740
window_height = 250
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


label_angle = tk.Label(root, text="Enter Angle (in Degrees):", font=("Times New Roman", 14), bg="lightpink")
entry_angle = tk.Entry(root, font=("Times New Roman", 13), justify="center")
button_frame = tk.Frame(root, bg="lightpink")  # Frame to hold the buttons
label_result = tk.Label(root, text="", justify="left", bg="lightpink")
button_clear = tk.Button(root, text="CLEAR", command=clear_result, font=("Times New Roman", 12), bg="white", width=10, height=1, bd=2, relief="raised")

#button styles
button_style = {
    "font": ("Times New Roman", 12),
    "width": 10,
    "height": 1,
    "bd": 2,
    "relief": "raised",
}

#button colors
button_colors = {
    "sin": "lightblue",
    "cos": "lightgreen",
    "tan": "lightcoral",
    "sec": "lightyellow",
    "cosec": "lightsalmon",
    "cot": "#eb67e0",
}

#buttons
methods = ["sin", "cos", "tan", "sec", "cosec", "cot"]
for method in methods:
    button = tk.Button(button_frame, text=method.upper(), command=lambda m=method: calculate(m), bg=button_colors[method], **button_style)
    button.pack(side="left", padx=5)


label_angle.pack()
entry_angle.pack()
button_frame.pack(pady=10)
label_result.pack()
button_clear.pack(pady=10)

root.mainloop()
