import tkinter as tk
from main import load_materials
from tkinter import ttk

import _mysql_connector


def connect():
    return _mysql_connector.connect(
        host="localhost",
        user="root",
        password="12",
        database="marupov"
    )
def load():
    for i in tree.get_children():
        tree.delete(i)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        select * from marupov"
                       """)

    for row in cur:
        tree.insert('', 'end', values=row)

        conn.close()


root = tk.Tk()
root.title("экзамен")

columns = ("ID", "Название", "Тип", "Количество","Цена")
tree = ttk.Treeview(root, columns = columns, show = "headings")

for column in columns:
    tree.heading(column, text=column)
    tree.column(column, width=100)

tree.pack(fill="both", expand=True)
tk.button(root, text="Обновить", command=load_materials).pack()
load(); root.mainloop()
root.mainloop()
