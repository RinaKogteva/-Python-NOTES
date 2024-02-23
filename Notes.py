#Импортируем необходимые библиотеки
import json
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

#Создаем окно менюбара
root = Tk()
root.title("ЗАМЕТКИ")
root.geometry("400x600")
text = Text(root,width=400, height=600)
text.pack()
ont = StringVar()

frame_ent = Frame(root, bg="grey")
frame_ent.place(relheight=0.05)
menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label='Файл', menu = file_menu)

# Функция для создания новой заметки
def create_note():
    global note_name
    text.delete('1.0', END)
    note_id = len(notes) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    note = {"id": note_id, "timestamp": timestamp}
    save_notes()
    
