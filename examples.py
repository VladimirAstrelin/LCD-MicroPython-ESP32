# Примеры использования LCD 2004 с ESP32 на MicroPython
# SCL = Pin(22), SDA = Pin(21)

from machine import Pin, I2C
from i2c_lcd import I2cLcd
import time
import random

# Инициализация I2C и LCD
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)  # Адрес 0x27, 4 строки, 20 столбцов

# =============================================================================
# ПРИМЕР 1: Базовый вывод текста
# =============================================================================
def example_1_basic_text():
    print("Пример 1: Базовый вывод текста")
    lcd.clear()
    lcd.putstr("Hello, World!")
    lcd.move_to(0, 1)
    lcd.putstr("ESP32 + LCD 2004")
    lcd.move_to(0, 2)
    lcd.putstr("MicroPython rocks!")
    lcd.move_to(0, 3)
    lcd.putstr("Line 4: Amazing!")
    time.sleep(3)

# =============================================================================
# ПРИМЕР 2: Управление курсором
# =============================================================================
def example_2_cursor_control():
    print("Пример 2: Управление курсором")
    lcd.clear()
    lcd.putstr("Cursor Demo:")
    
    # Показать курсор
    lcd.move_to(0, 1)
    lcd.putstr("Show cursor")
    lcd.show_cursor()
    time.sleep(2)
    
    # Мигающий курсор
    lcd.move_to(0, 2)
    lcd.putstr("Blinking cursor")
    lcd.blink_cursor_on()
    time.sleep(2)
    
    # Выключить мигание
    lcd.blink_cursor_off()
    time.sleep(1)
    
    # Спрятать курсор
    lcd.hide_cursor()
    time.sleep(1)

# =============================================================================
# ПРИМЕР 3: Управление подсветкой
# =============================================================================
def example_3_backlight_control():
    print("Пример 3: Управление подсветкой")
    lcd.clear()
    lcd.putstr("Backlight Demo")
    
    for i in range(5):
        lcd.move_to(0, 1)
        lcd.putstr(f"Cycle: {i+1}/5")
        
        # Выключить подсветку
        lcd.backlight_off()
        time.sleep(1)
        
        # Включить подсветку
        lcd.backlight_on()
        time.sleep(1)

# =============================================================================
# ПРИМЕР 4: Управление дисплеем
# =============================================================================
def example_4_display_control():
    print("Пример 4: Управление дисплеем")
    lcd.clear()
    lcd.putstr("Display Control")
    lcd.move_to(0, 1)
    lcd.putstr("Text will blink")
    
    for i in range(5):
        lcd.display_off()
        time.sleep(0.5)
        lcd.display_on()
        time.sleep(0.5)

# =============================================================================
# ПРИМЕР 5: Позиционирование текста
# =============================================================================
def example_5_positioning():
    print("Пример 5: Позиционирование текста")
    lcd.clear()
    
    # Заполнить все 4 строки в разных позициях
    positions = [
        (0, 0, "Top-Left"),
        (10, 0, "Top-Right"),
        (0, 1, "Line 2 Start"),
        (12, 1, "Line 2 End"),
        (5, 2, "Center Line 3"),
        (0, 3, "Bottom: "),
        (8, 3, "Full!")
    ]
    
    for x, y, text in positions:
        lcd.move_to(x, y)
        lcd.putstr(text)
        time.sleep(0.5)
    
    time.sleep(2)

# =============================================================================
# ПРИМЕР 6: Прокрутка текста
# =============================================================================
def example_6_scrolling_text():
    print("Пример 6: Прокрутка текста")
    lcd.clear()
    
    long_text = "This is a very long text that will scroll across the LCD display!"
    
    for i in range(len(long_text) - 19):
        lcd.move_to(0, 0)
        lcd.putstr("Scrolling Demo:")
        lcd.move_to(0, 1)
        lcd.putstr(long_text[i:i+20])
        time.sleep(0.2)

# =============================================================================
# ПРИМЕР 7: Счетчик с форматированием
# =============================================================================
def example_7_counter():
    print("Пример 7: Счетчик")
    lcd.clear()
    lcd.putstr("Counter Demo:")
    
    for i in range(100):
        lcd.move_to(0, 1)
        lcd.putstr(f"Count: {i:3d}")
        lcd.move_to(0, 2)
        lcd.putstr(f"Hex: 0x{i:02X}")
        lcd.move_to(0, 3)
        lcd.putstr(f"Binary: {i:08b}")
        time.sleep(0.1)

# =============================================================================
# ПРИМЕР 8: Часы реального времени (симуляция)
# =============================================================================
def example_8_clock():
    print("Пример 8: Часы")
    lcd.clear()
    lcd.putstr("Digital Clock:")
    
    start_time = time.ticks_ms()
    
    for _ in range(30):  # 30 секунд демо
        elapsed = time.ticks_diff(time.ticks_ms(), start_time) // 1000
        hours = (elapsed // 3600) % 24
        minutes = (elapsed // 60) % 60
        seconds = elapsed % 60
        
        lcd.move_to(0, 1)
        lcd.putstr(f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
        # Показать дату (фиктивную)
        lcd.move_to(0, 2)
        lcd.putstr("Date: 09.06.2025")
        
        # Показать день недели
        lcd.move_to(0, 3)
        lcd.putstr("Monday")
        
        time.sleep(1)

# =============================================================================
# ПРИМЕР 9: Температурный монитор (симуляция)
# =============================================================================
def example_9_temperature_monitor():
    print("Пример 9: Монитор температуры")
    lcd.clear()
    lcd.putstr("Temperature Monitor")
    
    for i in range(20):
        # Симуляция температуры
        temp_c = 20 + random.randint(-5, 15)
        temp_f = temp_c * 9 // 5 + 32
        humidity = 45 + random.randint(-10, 20)
        
        lcd.move_to(0, 1)
        lcd.putstr(f"Temp: {temp_c}C / {temp_f}F")
        lcd.move_to(0, 2)
        lcd.putstr(f"Humidity: {humidity}%")
        lcd.move_to(0, 3)
        lcd.putstr(f"Reading #{i+1}")
        
        time.sleep(1)

# =============================================================================
# ПРИМЕР 10: Индикатор прогресса
# =============================================================================
def example_10_progress_bar():
    print("Пример 10: Индикатор прогресса")
    lcd.clear()
    lcd.putstr("Progress Bar Demo:")
    
    for progress in range(101):
        lcd.move_to(0, 1)
        lcd.putstr(f"Progress: {progress:3d}%")
        
        # Создать визуальную полосу прогресса
        bar_length = (progress * 20) // 100
        bar = "#" * bar_length + "-" * (20 - bar_length)
        lcd.move_to(0, 2)
        lcd.putstr(bar)
        
        # Статус
        lcd.move_to(0, 3)
        if progress < 33:
            lcd.putstr("Status: Starting... ")
        elif progress < 66:
            lcd.putstr("Status: Processing..")
        elif progress < 100:
            lcd.putstr("Status: Finishing.. ")
        else:
            lcd.putstr("Status: Complete!   ")
        
        time.sleep(0.1)

# =============================================================================
# ПРИМЕР 11: Меню навигации
# =============================================================================
def example_11_menu():
    print("Пример 11: Меню навигации")
    menu_items = [
        "1. Settings",
        "2. Display",
        "3. Network",
        "4. System Info",
        "5. Reboot",
        "6. Exit"
    ]
    
    selected = 0
    
    for demo_step in range(len(menu_items) * 2):  # Демо навигации
        lcd.clear()
        lcd.putstr("Main Menu:")
        
        # Показать 3 пункта меню
        for i in range(3):
            menu_index = (selected + i) % len(menu_items)
            lcd.move_to(0, i + 1)
            prefix = ">" if i == 0 else " "
            lcd.putstr(f"{prefix} {menu_items[menu_index]}")
        
        selected = (selected + 1) % len(menu_items)
        time.sleep(1)

# =============================================================================
# ПРИМЕР 12: Системная информация
# =============================================================================
def example_12_system_info():
    print("Пример 12: Системная информация")
    import gc
    import micropython
    
    lcd.clear()
    lcd.putstr("System Information:")
    
    # Показать разную системную информацию
    info_screens = [
        ("Memory Info:", f"Free: {gc.mem_free()}", f"Alloc: {gc.mem_alloc()}", "Bytes"),
        ("Platform:", "ESP32", "MicroPython", f"Freq: {machine.freq()//1000000}MHz"),
        ("I2C Info:", "SCL: Pin 22", "SDA: Pin 21", "Freq: 400kHz"),
        ("LCD Info:", "Model: 2004", "Size: 20x4", "I2C Address: 0x27")
    ]
    
    for title, line1, line2, line3 in info_screens:
        lcd.clear()
        lcd.putstr(title)
        lcd.move_to(0, 1)
        lcd.putstr(line1)
        lcd.move_to(0, 2)
        lcd.putstr(line2)
        lcd.move_to(0, 3)
        lcd.putstr(line3)
        time.sleep(3)

# =============================================================================
# ПРИМЕР 13: Создание пользовательских символов
# =============================================================================
def example_13_custom_characters():
    print("Пример 13: Пользовательские символы")
    
    # Определить пользовательские символы
    # Сердце
    heart = [
        0b00000,
        0b01010,
        0b11111,
        0b11111,
        0b11111,
        0b01110,
        0b00100,
        0b00000
    ]
    
    # Смайлик
    smiley = [
        0b00000,
        0b01010,
        0b00000,
        0b00000,
        0b10001,
        0b01110,
        0b00000,
        0b00000
    ]
    
    # Стрелка вверх
    arrow_up = [
        0b00100,
        0b01110,
        0b11111,
        0b00100,
        0b00100,
        0b00100,
        0b00100,
        0b00000
    ]
    
    # Стрелка вниз
    arrow_down = [
        0b00100,
        0b00100,
        0b00100,
        0b00100,
        0b11111,
        0b01110,
        0b00100,
        0b00000
    ]
    
    # Загрузить пользовательские символы
    lcd.custom_char(0, heart)
    lcd.custom_char(1, smiley)
    lcd.custom_char(2, arrow_up)
    lcd.custom_char(3, arrow_down)
    
    lcd.clear()
    lcd.putstr("Custom Characters:")
    lcd.move_to(0, 1)
    lcd.putstr("Heart: " + chr(0) + " Love!")
    lcd.move_to(0, 2)
    lcd.putstr("Happy: " + chr(1) + " Face!")
    lcd.move_to(0, 3)
    lcd.putstr("Arrows: " + chr(2) + " " + chr(3) + " Move!")
    
    time.sleep(3)

# =============================================================================
# ПРИМЕР 14: Анимация с пользовательскими символами
# =============================================================================
def example_14_animation():
    print("Пример 14: Анимация")
    
    # Создать символы для анимации (фазы луны)
    moon_phases = [
        [0b01110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110, 0b00000],  # Новолуние
        [0b01110, 0b10001, 0b10011, 0b10111, 0b10111, 0b10011, 0b01110, 0b00000],  # Растущая
        [0b01110, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b01110, 0b00000],  # Полнолуние
        [0b01110, 0b11001, 0b11101, 0b11101, 0b11101, 0b11001, 0b01110, 0b00000],  # Убывающая
    ]
    
    lcd.clear()
    lcd.putstr("Moon Phase Animation")
    
    for cycle in range(3):  # 3 полных цикла
        for phase, pattern in enumerate(moon_phases):
            lcd.custom_char(0, pattern)
            lcd.move_to(0, 2)
            lcd.putstr(f"Phase {phase+1}: " + chr(0))
            time.sleep(1)

# =============================================================================
# ПРИМЕР 15: Игра "Змейка" (упрощенная версия)
# =============================================================================
def example_15_snake_game():
    print("Пример 15: Игра Змейка")
    
    # Создать символы для игры
    snake_body = [0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b00000]
    food = [0b00100, 0b01110, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000]
    
    lcd.custom_char(0, snake_body)
    lcd.custom_char(1, food)
    
    lcd.clear()
    lcd.putstr("Snake Game Demo:")
    
    # Простая демонстрация движения змейки
    snake_positions = [(5, 2), (6, 2), (7, 2)]
    food_pos = (10, 2)
    
    for step in range(15):
        lcd.move_to(0, 1)
        lcd.putstr("Score: " + str(step))
        
        # Очистить предыдущие позиции
        for x in range(20):
            lcd.move_to(x, 2)
            lcd.putchar(' ')
        
        # Отобразить еду
        lcd.move_to(food_pos[0], food_pos[1])
        lcd.putchar(chr(1))
        
        # Отобразить змейку
        for pos in snake_positions:
            lcd.move_to(pos[0], pos[1])
            lcd.putchar(chr(0))
        
        # Переместить змейку
        new_head = ((snake_positions[-1][0] + 1) % 15, snake_positions[-1][1])
        snake_positions.append(new_head)
        snake_positions.pop(0)
        
        time.sleep(0.5)

# =============================================================================
# ПРИМЕР 16: Многоязычный текст
# =============================================================================
def example_16_multilingual():
    print("Пример 16: Многоязычный текст")
    
    texts = [
        ("English:", "Hello World!", "Welcome!", "Good day!"),
        ("Numbers:", "123456789", "Pi = 3.14159", "E = 2.71828"),
        ("Symbols:", "!@#$%^&*()", "[]{}()<>", "+-*/=~`"),
        ("Mixed:", "ABC123!@#", "ESP32 + LCD", "2004 Display")
    ]
    
    for title, line1, line2, line3 in texts:
        lcd.clear()
        lcd.putstr(title)
        lcd.move_to(0, 1)
        lcd.putstr(line1)
        lcd.move_to(0, 2)
        lcd.putstr(line2)
        lcd.move_to(0, 3)
        lcd.putstr(line3)
        time.sleep(3)

# =============================================================================
# ПРИМЕР 17: Тестирование всех позиций экрана
# =============================================================================
def example_17_position_test():
    print("Пример 17: Тест позиций")
    
    # Заполнить весь экран символами для проверки
    lcd.clear()
    lcd.putstr("Position Test:")
    
    # Показать координаты в каждой позиции
    for row in range(4):
        for col in range(20):
            if row == 0 and col < 14:  # Пропустить заголовок
                continue
            lcd.move_to(col, row)
            if col < 10:
                lcd.putchar(str(col))
            else:
                lcd.putchar(chr(ord('A') + col - 10))
    
    time.sleep(3)
    
    # Тест границ
    lcd.clear()
    lcd.putstr("Border Test:")
    
    # Верхняя и нижняя границы
    for col in range(20):
        lcd.move_to(col, 1)
        lcd.putchar('-')
        lcd.move_to(col, 3)
        lcd.putchar('-')
    
    # Левая и правая границы  
    for row in range(1, 4):
        lcd.move_to(0, row)
        lcd.putchar('|')
        lcd.move_to(19, row)
        lcd.putchar('|')
    
    # Углы
    lcd.move_to(0, 1)
    lcd.putchar('+')
    lcd.move_to(19, 1)
    lcd.putchar('+')
    lcd.move_to(0, 3)
    lcd.putchar('+')
    lcd.move_to(19, 3)
    lcd.putchar('+')
    
    time.sleep(3)

# =============================================================================
# ПРИМЕР 18: Стресс-тест производительности
# =============================================================================
def example_18_performance_test():
    print("Пример 18: Тест производительности")
    
    lcd.clear()
    lcd.putstr("Performance Test:")
    
    start_time = time.ticks_ms()
    
    # Быстрая запись большого количества символов
    for i in range(100):
        lcd.move_to(0, 1)
        lcd.putstr(f"Iteration: {i:3d}")
        lcd.move_to(0, 2)
        lcd.putstr("X" * (i % 21))
        lcd.move_to(0, 3)
        lcd.putstr("=" * ((i * 2) % 21))
    
    end_time = time.ticks_ms()
    duration = time.ticks_diff(end_time, start_time)
    
    lcd.clear()
    lcd.putstr("Performance Result:")
    lcd.move_to(0, 1)
    lcd.putstr(f"100 iterations")
    lcd.move_to(0, 2)
    lcd.putstr(f"Time: {duration}ms")
    lcd.move_to(0, 3)
    lcd.putstr(f"Avg: {duration/100:.1f}ms/op")
    
    time.sleep(3)

# =============================================================================
# ПРИМЕР 19: Демонстрация обработки переноса строк
# =============================================================================
def example_19_line_wrapping():
    print("Пример 19: Перенос строк")
    
    lcd.clear()
    
    # Длинный текст, который будет автоматически переноситься
    long_text = "This is a very long text that will automatically wrap to the next line and demonstrate the line wrapping functionality of the LCD display!"
    
    lcd.putstr("Auto Line Wrap:")
    lcd.move_to(0, 1)
    
    # Вывести длинный текст - он должен автоматически переноситься
    for char in long_text:
        lcd.putchar(char)
        time.sleep(0.05)  # Медленный вывод для демонстрации
    
    time.sleep(3)

# =============================================================================
# ПРИМЕР 20: Финальная демонстрация всех возможностей
# =============================================================================
def example_20_grand_finale():
    print("Пример 20: Финальная демонстрация")
    
    # Создать специальные символы для финала
    star = [0b00100, 0b01110, 0b11111, 0b01110, 0b01010, 0b10001, 0b00000, 0b00000]
    lcd.custom_char(0, star)
    
    # Заставка
    lcd.clear()
    lcd.backlight_off()
    time.sleep(0.5)
    lcd.backlight_on()
    
    # Анимированная заставка
    for i in range(3):
        lcd.clear()
        lcd.move_to(8, 1)
        lcd.putstr("DEMO")
        lcd.move_to(6, 2)
        lcd.putstr("COMPLETE!")
        
        # Добавить звездочки
        positions = [(2, 1), (15, 1), (2, 2), (15, 2)]
        for pos in positions:
            lcd.move_to(pos[0], pos[1])
            lcd.putchar(chr(0))
        
        time.sleep(0.5)
        lcd.display_off()
        time.sleep(0.2)
        lcd.display_on()
    
    # Финальное сообщение
    lcd.clear()
    lcd.putstr("All 20 examples done!")
    lcd.move_to(0, 1)
    lcd.putstr("ESP32 + LCD = " + chr(0))
    lcd.move_to(0, 2)
    lcd.putstr("MicroPython rocks!")
    lcd.move_to(0, 3)
    lcd.putstr("Thank you!")

# =============================================================================
# ГЛАВНАЯ ФУНКЦИЯ ДЛЯ ЗАПУСКА ВСЕХ ПРИМЕРОВ
# =============================================================================
def run_all_examples():
    """Запустить все примеры по очереди"""
    examples = [
        example_1_basic_text,
        example_2_cursor_control,
        example_3_backlight_control,
        example_4_display_control,
        example_5_positioning,
        example_6_scrolling_text,
        example_7_counter,
        example_8_clock,
        example_9_temperature_monitor,
        example_10_progress_bar,
        example_11_menu,
        example_12_system_info,
        example_13_custom_characters,
        example_14_animation,
        example_15_snake_game,
        example_16_multilingual,
        example_17_position_test,
        example_18_performance_test,
        example_19_line_wrapping,
        example_20_grand_finale
    ]
    
    print("Запуск всех 20 примеров для LCD 2004...")
    print("Используется I2C: SCL=Pin(22), SDA=Pin(21)")
    print("LCD адрес: 0x27, размер: 20x4")
    print("=" * 50)
    
    for i, example in enumerate(examples, 1):
        print(f"Запуск примера {i}/20...")
        try:
            example()
            print(f"Пример {i} завершен успешно")
        except Exception as e:
            print(f"Ошибка в примере {i}: {e}")
        
        # Пауза между примерами
        time.sleep(2)
    
    print("=" * 50)
    print("Все примеры завершены!")

# =============================================================================
# ФУНКЦИЯ ДЛЯ ЗАПУСКА ОТДЕЛЬНОГО ПРИМЕРА
# =============================================================================
def run_example(example_number):
    """Запустить конкретный пример по номеру"""
    examples = {
        1: example_1_basic_text,
        2: example_2_cursor_control,
        3: example_3_backlight_control,
        4: example_4_display_control,
        5: example_5_positioning,
        6: example_6_scrolling_text,
        7: example_7_counter,
        8: example_8_clock,
        9: example_9_temperature_monitor,
        10: example_10_progress_bar,
        11: example_11_menu,
        12: example_12_system_info,
        13: example_13_custom_characters,
        14: example_14_animation,
        15: example_15_snake_game,
        16: example_16_multilingual,
        17: example_17_position_test,
        18: example_18_performance_test,
        19: example_19_line_wrapping,
        20: example_20_grand_finale
    }
    
    if example_number in examples:
        print(f"Запуск примера {example_number}...")
        examples[example_number]()
        print(f"Пример {example_number} завершен")
    else:
        print(f"Пример {example_number} не найден. Доступны примеры 1-20")

# =============================================================================
# ИСПОЛЬЗОВАНИЕ:
# =============================================================================
# Для запуска всех примеров:
# run_all_examples()

# Для запуска конкретного примера:
# run_example(1)  # Запустить пример 1
# run_example(13) # Запустить пример 13 (пользовательские символы)

# Для быстрого теста подключения:
# example_1_basic_text()