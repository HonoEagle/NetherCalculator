from tkinter import *
from tkinter import messagebox

RATIO = 8


def calculate():
    try:
        x = float(x_entry.get().strip())
        y = float(y_entry.get().strip())
        z = float(z_entry.get().strip())
    except ValueError:
        messagebox.showerror("Erreur", "Entre des nombres valides pour X, Y et Z.")
        return

    direction = direction_var.get()
    if direction == "Overworld -> Nether":
        new_x = x / RATIO
        new_z = z / RATIO
    else:
        new_x = x * RATIO
        new_z = z * RATIO

    # Y ne change pas entre les dimensions
    new_y = y

    result_x_value.config(text=f"X = {round(new_x, 2)}")
    result_y_value.config(text=f"Y = {round(new_y, 2)}")
    result_z_value.config(text=f"Z = {round(new_z, 2)}")


window = Tk()
window.title("Convertisseur Nether / Overworld")
window.geometry("420x360")

Label(window, text="Dimension source -> cible :").pack(pady=(10, 2))
direction_var = StringVar(value="Overworld -> Nether")
OptionMenu(window, direction_var, "Overworld -> Nether", "Nether -> Overworld").pack()

Label(window, text="X :").pack(pady=(12, 0))
x_entry = Entry(window)
x_entry.pack()

Label(window, text="Y :").pack(pady=(8, 0))
y_entry = Entry(window)
y_entry.pack()

Label(window, text="Z :").pack(pady=(8, 0))
z_entry = Entry(window)
z_entry.pack()

Button(window, text="Calculer", command=calculate).pack(pady=14)

Label(window, text="Coordonnées converties :").pack()
result_x_value = Label(window, text="X =")
result_x_value.pack()
result_y_value = Label(window, text="Y =")
result_y_value.pack()
result_z_value = Label(window, text="Z =")
result_z_value.pack()

window.mainloop()
