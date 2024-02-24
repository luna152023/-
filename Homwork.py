from tkinter import *
import tkinter.messagebox
import random

attempt_count = 0
generated_number = None

def generate():
    global attempt_count, generated_number
    try:
        start_range = int(ent_start.get())
        end_range = int(ent_end.get())
        generated_number = random.randint(start_range, end_range)
        attempt_count = 0
        ent_vgadai['state'] = 'normal'
        but_start['state'] = 'normal'
        ent_start['state'] = 'disabled'
        ent_end['state'] = 'disabled'
        but_gener['state'] = 'disabled'
        root.title("Спроба {}".format(attempt_count + 1))
    except ValueError:
        tkinter.messagebox.showerror("Помилка", "Потрібно вводити числа")

def guess_number():
    global attempt_count
    try:
        guessed_number = int(ent_vgadai.get())
        if guessed_number == generated_number:
            tkinter.messagebox.showinfo("Вітання", "Ви вгадали число!")
            ent_vgadai.delete(0, END)
            retry()
        elif guessed_number < generated_number:
            tkinter.messagebox.showinfo("Підказка", "Загадане число більше")
        else:
            tkinter.messagebox.showinfo("Підказка", "Загадане число менше")
        attempt_count += 1
        root.title("Спроба {}".format(attempt_count + 1))
        if attempt_count >= 5:
            ent_vgadai['state'] = 'disabled'
            but_start['state'] = 'disabled'
    except ValueError:
        tkinter.messagebox.showerror("Помилка", "Потрібно вводити числа")
def retry():
    global attempt_count, generated_number
    ent_start['state'] = 'normal'
    ent_end['state'] = 'normal'
    but_gener['state'] = 'normal'
    ent_vgadai.delete(0, END)
    root.title('')
    attempt_count = 0
    generated_number = None
root = Tk()
root.geometry('600x450')
lab_poch = Label(root, text='Ліва межа', font=(None, 16),bg='black',fg='orange')
lab_poch.place(x=40, y=50)
lab_end = Label(root, text='Права межа', font=(None, 16),bg='orange',fg='black')
lab_end.place(x=40, y=90)
ent_start = Entry(root, font=(None, 16),fg='darkmagenta')
ent_start.place(x=180, y=50)
ent_end = Entry(root, font=(None, 16),fg='darkmagenta')
ent_end.place(x=180, y=90)
but_gener = Button(root, text='Генерувати', font=(None, 16), command=generate,bg='black',fg='orange')
but_gener.place(x=180, y=140)
lab_vgadai = Label(root, text='Введіть число', font=(None, 16),bg='orange',fg='black')
lab_vgadai.place(x=40, y=190)
ent_vgadai = Entry(root, font=(None, 16), state='disabled',fg='darkmagenta')
ent_vgadai.place(x=180, y=190)
but_start = Button(root, text='Вгадати', font=(None, 16), command=guess_number, state='disabled',bg='black',fg='orange')
but_start.place(x=180, y=230)
start_the_beginning = Label(root, text='Почати гру знову? ', font=(None, 20),bg='orange',fg='black')
start_the_beginning.place(x=40, y=280)
but_start1 = Button(root, text='Так', font=(None, 16), command=retry,fg='red',bg='black')
but_start1.place(x=300, y=280)
but_start2 = Button(root, text='Ні', font=(None, 16), command=root.destroy,bg='black',fg='yellowgreen')
but_start2.place(x=350, y=280)

root.mainloop()