import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox
import logging
import keyboard 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

class AutoPressApp:
    def __init__(self, master): 
        self.master = master
        self.master.title("Auto Press F")
        
        self.is_running = False
        
        self.start_button = tk.Button(master, text="Старт", command=self.start_pressing)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Стоп", command=self.stop_pressing)
        self.stop_button.pack(pady=10)
        
        self.info_button = tk.Button(master, text="Информация", command=self.show_info)
        self.info_button.pack(pady=10)

        self.keyboard_thread = threading.Thread(target=self.listen_keys)
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()

    def start_pressing(self):
        if not self.is_running:
            self.is_running = True
            logger.info("Программа запущена.")
            self.thread = threading.Thread(target=self.press_f)
            self.thread.start()

    def stop_pressing(self):
        self.is_running = False
        if hasattr(self, 'thread'):
            self.thread.join()
            logger.info("Программа остановлена.")

    def press_f(self):
        while self.is_running:
            time.sleep(2)
            pyautogui.press('f') 

    def show_info(self):
        info_message = (
            "ДО ЗАПУСКА ПРОГРАММЫ РАСКЛАДКА ДОЛЖНА СТОЯТЬ ENG!!!\n"
            "Данный скрипт создан для прохождения задания сезонного пропуска Majestic RP, "
            "где нужно 15 раз выиграть в игровой автомат.\n\n"
            "Функционал:\n"
            "1) Кнопка Старт (или же клавиша + на клавиатуре)\n"
            "2) Кнопка Стоп (или же клавиша - на клавиатуре)\n"
            "3) Кнопка Информация\n\n"
            "Версия: V1"
        )
        messagebox.showinfo("Информация", info_message)

    def listen_keys(self):
        while True:
            if keyboard.is_pressed('+'):
                self.start_pressing()
                time.sleep(0.5)  
            elif keyboard.is_pressed('-'):
                self.stop_pressing()
                time.sleep(0.5)  

if __name__ == "__main__": 
    root = tk.Tk()
    app = AutoPressApp(root)
    root.mainloop()
