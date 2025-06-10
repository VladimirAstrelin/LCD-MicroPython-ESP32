import tkinter as tk
from tkinter import ttk

def validate_length(P):
    """Функция проверки длины ввода"""
    return len(P) <= 20

def insert_text():
    # Получаем данные из всех четырех полей
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    text4 = entry4.get()
    
    # Формируем выходной текст
    output_text = f'lcd.move_to(0, 0)\nlcd.putstr("{text1}")\n\n'
    output_text += f'lcd.move_to(0, 1)\nlcd.putstr("{text2}")\n\n'
    output_text += f'lcd.move_to(0, 2)\nlcd.putstr("{text3}")\n\n'
    output_text += f'lcd.move_to(0, 3)\nlcd.putstr("{text4}")\n'
    
    # Очищаем и вставляем текст в выходное поле
    output_entry.delete(1.0, tk.END)
    output_entry.insert(tk.END, output_text)

def copy_to_clipboard():
    # Получаем текст из выходного поля
    text_to_copy = output_entry.get(1.0, tk.END)
    
    # Очищаем буфер обмена и добавляем туда текст
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    root.update()  # Фиксируем изменения в буфере обмена
    
    # Временно меняем текст кнопки для визуального подтверждения
    copy_button.config(text="Скопировано!")
    root.after(2000, lambda: copy_button.config(text="Скопировать в буфер"))

# Создаем главное окно
root = tk.Tk()
root.title("LCD 2004 Text Generator")

# Регистрируем функцию валидации
vcmd = (root.register(validate_length), '%P')

# Создаем и размещаем метки и поля ввода
tk.Label(root, text="Строка 1 (0,0):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry1 = ttk.Entry(root, width=25, validate="key", validatecommand=vcmd)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Строка 2 (0,1):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry2 = ttk.Entry(root, width=25, validate="key", validatecommand=vcmd)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Строка 3 (0,2):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry3 = ttk.Entry(root, width=25, validate="key", validatecommand=vcmd)
entry3.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Строка 4 (0,3):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry4 = ttk.Entry(root, width=25, validate="key", validatecommand=vcmd)
entry4.grid(row=3, column=1, padx=5, pady=5)

# Кнопка для вставки текста
insert_button = ttk.Button(root, text="Вставить", command=insert_text)
insert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Выходное текстовое поле с прокруткой
tk.Label(root, text="Результат для MicroPython:").grid(row=5, column=0, columnspan=2, pady=5, sticky="w")

output_entry = tk.Text(root, width=40, height=15, wrap=tk.NONE)
output_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Добавляем полосу прокрутки
scrollbar = ttk.Scrollbar(root, orient="vertical", command=output_entry.yview)
scrollbar.grid(row=6, column=2, sticky="ns")
output_entry.configure(yscrollcommand=scrollbar.set)

# Кнопка для копирования в буфер обмена
copy_button = ttk.Button(root, text="Скопировать в буфер", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, pady=5)

# Запускаем главный цикл
root.mainloop()