import tkinter as tk

def on_click(key):
    current_text = entry.get()
    if key == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "Del":
        entry.delete(len(current_text) - 1)
    else:
        entry.insert(tk.END, key)

app = tk.Tk()
app.title("Simple Calculator")

entry = tk.Entry(app, font=("Arial", 20), bd=5, width=20, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("Del", 5, 0), ("C", 5, 1)
]

for (text, row, col) in buttons:
    btn = tk.Button(app, text=text, font=("Arial", 18), bd=3, width=5, height=2,
                    command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

app.mainloop()

