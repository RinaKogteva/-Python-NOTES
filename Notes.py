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
    
# Функция для сохранения заметок в файл
def save_notes():
    global data
    out = asksaveasfile(mode="w", defaultextension=".json")
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ошибка", "Не получилось сохранить файл!")
    data2 = text.get('1.0', '1.15')
    new_button = Button(frame_base, text=data2, command=open_name_file)
    new_button.pack(side=TOP, pady=5, padx=5)

# Функция для чтения всех заметок
def read_notes():
    for note in notes:
        print(f"{note['id']}.({note['timestamp']})")
    if not notes:
        print("Нет заметок")
        
# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note['id'] == note_id:
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

# Функция открытия файлов
def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
    note_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

# Функция перезапуска
def restart_font():
    global font
    font = str(entry.get())
    if font == "":
        messagebox.showerror("Ошибка", "Поле ввода шрифта пусто")
    else:
        text.config(font=font)
        
#Функция автосохранения файла