import tkinter as tk  # Импорт модуля tkinter и его псевдонима tk


def clear_task(): # Объявление функции для очистки всего списка задач
    task_listBox.delete(0, tk.END)  # Очистка списка задач

root = tk.Tk()  # Создание главного окна
root.title("Task list")  # Установка заголовка окна
root.config(background="lightgray")  # Установка цвета фона для главного окна

clear_buton = tk.Button(root, text="Очистить список", command=clear_task) # Создание кнопки для очистки списка задач
clear_buton.pack(pady=5)    #Размещение кнопки в главном окне с небольшим отступом

root.mainloop()  # Запуск главного цикла приложения