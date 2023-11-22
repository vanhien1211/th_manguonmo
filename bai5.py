import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
import tkinter as tk
from tkinter import ttk

class UngDungThietKeBoLoc:
    def __init__(self, master):
        self.master = master
        master.title("Ứng Dụng Thiết Kế Bộ Lọc FIR")

        self.dang_loc_label = ttk.Label(master, text="Chọn Dạng Bộ Lọc:")
        self.dang_loc_combobox = ttk.Combobox(master, values=["Thông Cao", "Thông Thấp"])
        self.dang_loc_combobox.set("Thông Cao")

        self.tan_so_cat_label = ttk.Label(master, text="Tần Số Cắt:")
        self.tan_so_cat_nhap = ttk.Entry(master)

        self.chieu_dai_label = ttk.Label(master, text="Chiều Dài Bộ Lọc:")
        self.chieu_dai_nhap = ttk.Entry(master)

        self.xac_dinh_dap_ung_button = ttk.Button(master, text="Xác Định Đáp Ứng h(n)", command=self.xac_dinh_dap_ung)
        self.ve_do_thi_button = ttk.Button(master, text="Vẽ Đồ Thị Bộ Lọc", command=self.ve_do_thi)
        self.bieu_dien_sodo_button = ttk.Button(master, text="Biểu Diễn Sơ Đồ Bộ Lọc", command=self.bieu_dien_sodo)

        # Label để hiển thị kết quả h(n)
        self.ket_qua_label = ttk.Label(master, text="Kết Quả h(n):")

        # Bố cục
        self.dang_loc_label.grid(row=0, column=0, padx=10, pady=10)
        self.dang_loc_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.tan_so_cat_label.grid(row=1, column=0, padx=10, pady=10)
        self.tan_so_cat_nhap.grid(row=1, column=1, padx=10, pady=10)

        self.chieu_dai_label.grid(row=2, column=0, padx=10, pady=10)
        self.chieu_dai_nhap.grid(row=2, column=1, padx=10, pady=10)

        self.xac_dinh_dap_ung_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.ve_do_thi_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.bieu_dien_sodo_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Label kết quả
        self.ket_qua_label.grid(row=6, column=0, columnspan=2, pady=10)

    def xac_dinh_dap_ung(self):
        try:
            dang_loc = self.dang_loc_combobox.get()
            tan_so_cat = float(self.tan_so_cat_nhap.get())
            chieu_dai = int(self.chieu_dai_nhap.get())

            if tan_so_cat <= 0 or chieu_dai <= 0:
                self.ket_qua_label.config(text="Vui lòng nhập giá trị hợp lệ cho Tần Số Cắt và Chiều Dài Bộ Lọc.")
                return

            # Thiết kế bộ lọc FIR dựa trên yêu cầu của người dùng
            if dang_loc == "Thông Cao":
                h = firwin(chieu_dai, tan_so_cat/2, pass_zero=False, window='hamming')
            elif dang_loc == "Thông Thấp":
                h = firwin(chieu_dai, tan_so_cat/2, pass_zero=True, window='hamming')

            # Lưu trữ hệ số bộ lọc để sử dụng sau này nếu cần
            self.h = h

            # Hiển thị kết quả h(n) trên Label
            self.ket_qua_label.config(text=f"Kết Quả h(n): {h}")

        except ValueError:
            self.ket_qua_label.config(text="Vui lòng nhập giá trị số cho Tần Số Cắt và Chiều Dài Bộ Lọc.")

    def ve_do_thi(self):
        if hasattr(self, 'h'):
            w, h = freqz(self.h, worN=8000)
            plt.figure()
            plt.plot(0.5 * w / np.pi, np.abs(h), 'b')
            plt.title('Đáp ứng tần số của Bộ Lọc FIR')
            plt.xlabel('Tần số (Hz)')
            plt.ylabel('Độ Cao')
            plt.grid(True)
            plt.show()

    def bieu_dien_sodo(self):
        if hasattr(self, 'h'):
            # Biểu diễn sơ đồ của bộ lọc FIR
            plt.figure()
            plt.stem(range(len(self.h)), self.h)
            plt.title('Sơ Đồ Bộ Lọc FIR')
            plt.xlabel('Chỉ số n')
            plt.ylabel('Hệ số h(n)')
            plt.grid(True)
            plt.show(block=False)  # Thêm tham số block=False để đảm bảo hiển thị đồ thị ngay lập tức

if __name__ == "__main__":
    root = tk.Tk()
    app = UngDungThietKeBoLoc(root)
    root.mainloop()
