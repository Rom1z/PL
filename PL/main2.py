import tkinter as tk
from tkinter import ttk
import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12",   # укажи свой пароль
        database="marupov"
    )
    return connection




def load_materials():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT 
    m.id,
    m.name,
    mt.name,
    m.stock_quantity,
    m.min_quantity
    FROM materials m
    JOIN material_types mt
    ON mt.id = m.type_id
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    conn.close()

root = tk.Tk()
root.title("Материалы на складе")
root.geometry("800x500")
root.configure(bg="#FFFFFF")

# Заголовок

title = tk.Label(
    root,
    text="Склад материалов",
    font=("Constantia", 18),
    bg="#FFFFFF",
    fg="#405C73"
)
title.pack(pady=10)



columns = ("ID", "Название", "Тип", "Количество", "Минимум")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(expand=True, fill="both", padx=20, pady=20)



btn_frame = tk.Frame(root, bg="#FFFFFF")
btn_frame.pack()

refresh_btn = tk.Button(
    btn_frame,
    text="Обновить список",
    font=("Constantia", 12),
    bg="#405C73",
    fg="white",
    command=load_materials
)

refresh_btn.pack(pady=10)



load_materials()

root.mainloop()
