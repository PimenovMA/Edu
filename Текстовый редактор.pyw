# -*- coding:utf-8 -*-
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox


FILE_NAME = tkinter.NONE


def new_file():
	global FILE_NAME
	FILE_NAME = "Новый"
	text.delete ('1.0', tkinter.END)

def save_file():
	data = text.get ('1.0', tkinter.END)
	out = open (FILE_NAME, 'w')
	out.write (data)
	out.close()
	
def save_as():
	out = asksaveasfile (mode = 'w', defaulttextension = 'txt')
	data = text.get ('1.0', tkinter.END)
	try:
		out.write (data.rstip())
	except Exception:
		showerror (title = 'ОШИБКА', message = 'Ошибка записи файла!')


def open_file():
	global FILE_NAME
	inp = askopenfile (mode = 'r')
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete ('1.0', tkinter.END)
	text.insert ('1.0', data)

def info():
	messagebox.showinfo ("ИНФОРМАЦИЯ", "Автор: Пименов Михаил Александрович\nE-mail: zloadmin@mail.ru\nVK: vk.com/id1908748")



# создаем обьект "ОКНО" с заголовком
root = tkinter.Tk()
root.title ('Простой тектовый редактор. Версия 0.0.4')

# задаем размеры окна
root.minsize (850,600)
root.maxsize (850,600)


# создаем текстовое поле с вертикальной прокруткой
text = tkinter.Text(root, width = 700, height = 500, wrap = "word")
scrolib = Scrollbar (root, orient = VERTICAL, command = text.yview)
scrolib.pack(side = "right", fill = 'y')
text.configure(yscrollcommand = scrolib.set)
text.pack()

menu_bar = tkinter.Menu(root)
file_menu = tkinter.Menu (menu_bar)

file_menu.add_command(label = 'Новый', command = new_file)
file_menu.add_command(label = 'Открыть', command = open_file)
file_menu.add_command(label = 'Сохранить', command = save_file)
file_menu.add_command(label = 'Сохранить как', command = save_as)

menu_bar.add_cascade (label = 'Файл', menu = file_menu)
menu_bar.add_cascade (label = 'Разрабочик', command = info)
menu_bar.add_cascade (label = 'Выход', command = root.quit)

root.config (menu = menu_bar)


root.mainloop()
