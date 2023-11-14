import tkinter as tk
from tkinter import ttk
import sympy as sp

def tinh_dien_tich_chu_vi():
    ban_kinh = float(entry_ban_kinh.get())
    canh = float(entry_canh.get())

    dien_tich_tron = sp.pi * ban_kinh**2
    chu_vi_tron = 2 * sp.pi * ban_kinh

    dien_tich_vuong = canh**2
    chu_vi_vuong = 4 * canh

    result_text.set(f'Dien tich hinh tron: {dien_tich_tron.evalf()}, Chu vi hinh tron: {chu_vi_tron.evalf()}\nDien tich hinh vuong: {dien_tich_vuong}, Chu vi hinh vuong: {chu_vi_vuong}')

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")

# Tạo các widget
label_ban_kinh = ttk.Label(root, text="Ban kinh hinh tron:")
entry_ban_kinh = ttk.Entry(root)

label_canh = ttk.Label(root, text="Canh hinh vuong:")
entry_canh = ttk.Entry(root)

button_tinh = ttk.Button(root, text="Tinh", command=tinh_dien_tich_chu_vi)

result_text = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_text)

# Sắp xếp các widget trên cửa sổ
label_ban_kinh.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ban_kinh.grid(row=0, column=1, padx=10, pady=10)

label_canh.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_canh.grid(row=1, column=1, padx=10, pady=10)

button_tinh.grid(row=2, column=0, columnspan=2, pady=10)

label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Bắt đầu vòng lặp chạy chương trình
root.mainloop()
