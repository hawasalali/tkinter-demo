import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def combo_selected():
    print("Selected:", combo.get())


def add_car(car):
    if car not in val_lst:
        val_lst.append(car)
    combo["values"] = val_lst
    combo.set(car)


def open_file():
    file = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:
        with open(file, "r", encoding="utf-8") as f:
            txt.delete("1.0", tk.END)
            txt.insert("1.0", f.read())


def save_file():
    file = filedialog.asksaveasfilename(
        title="Save File",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )

    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(txt.get("1.0", tk.END))


root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("800x600")

# Menüleiste
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(
    label="New",
    command=lambda: txt.delete("1.0", tk.END)
)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Tkinter Demo"
    )
)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Combobox
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

val_lst = ["BMW", "VW", "Audi", "Ford"]

combo = ttk.Combobox(
    top_frame,
    values=val_lst,
    state="readonly",
    width=20
)

combo.current(0)
combo.grid(row=0, column=0, padx=5)

ttk.Button(
    top_frame,
    text="Selected",
    command=combo_selected
).grid(row=0, column=1, padx=5)

ttk.Button(
    top_frame,
    text="Add Ferrari",
    command=lambda: add_car("Ferrari")
).grid(row=0, column=2, padx=5)

ttk.Button(
    top_frame,
    text="Add List",
    command=lambda: [
        add_car(car)
        for car in ["Maserati", "Tesla", "BYD"]
    ]
).grid(row=0, column=3, padx=5)

# Scale
tk.Scale(
    root,
    from_=0,
    to=10,
    orient="horizontal",
    label="Scale"
).pack(fill="x", padx=10, pady=10)

# Listbox mit Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=False, padx=10, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

mylist = tk.Listbox(
    list_frame,
    height=10,
    yscrollcommand=scrollbar.set
)

for i in range(100):
    mylist.insert(tk.END, f"Number {i}")

mylist.pack(side="left", fill="both", expand=True)

scrollbar.config(command=mylist.yview)

# Textfeld
txt = tk.Text(root, height=12)
txt.pack(fill="both", expand=True, padx=10, pady=10)

# Tastaturkürzel
root.bind("<Control-x>", lambda e: root.destroy())

root.mainloop()