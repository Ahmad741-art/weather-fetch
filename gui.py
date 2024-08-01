import tkinter as tk
from tkinter import ttk

def fetch_weather():
    city = city_entry.get()
    weather = get_weather(city)
    result_label.config(text=str(weather))

root = tk.Tk()
root.title('Weather App')

city_label = ttk.Label(root, text='City:')
city_label.pack()

city_entry = ttk.Entry(root)
city_entry.pack()

fetch_button = ttk.Button(root, text='Get Weather', command=fetch_weather)
fetch_button.pack()

result_label = ttk.Label(root, text='')
result_label.pack()

root.mainloop()
