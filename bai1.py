#Thêm thanh cuộn khi phương trình có nhiều ẩn màn hình không hiện hết được
import tkinter as tk
from tkinter import messagebox
import numpy as np

heso=[]
coso=[]
def math():
    try:
        main_frame.pack_forget()
        second_frame.pack_forget()
        third_frame.pack()
        global heso, coso
        n=int(entry1.get())
        array_heso = np.empty((n,n))
        array_coso = np.empty((n,1))
        for i in range(n*n):
            heso_value=float(heso[i].get())
            array_heso[i//n, i%n]=heso_value
        for i in range(n):
            coso_value=float(coso[i].get())
            array_coso[i,0]=coso_value
        x=np.linalg.solve(array_heso,array_coso)
        for i in x:
            label=tk.Label(third_frame,text=f"{i}")
            label.pack()
    except np.linalg.LinAlgError as e:
        if np.linalg.matrix_rank(array_heso)==np.linalg.matrix_rank(np.column_stack((array_heso,array_coso))):
            label_ketqua.config(text="Hệ có vô số nghiệm")
        else:
            label_ketqua.config(text="Hệ vô nghiệm")
    except ValueError:
        main_frame.pack_forget()
        second_frame.pack()
        third_frame.pack_forget()
        mes="Nhập số nguyên hoặc số thực"
        messagebox.showwarning("Cảnh báo",mes )

def bt1():
    try:
        n=int(entry1.get())
        main_frame.pack_forget()
        second_frame.pack()
        third_frame.pack_forget()

        canvas = tk.Canvas(second_frame)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(second_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame_inside_canvas = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

        global heso
        for i in range (n*n):
            label=tk.Label(frame_inside_canvas, text=f"Nhập hệ số {i+1}" )
            label.pack()
            entry=tk.Entry(frame_inside_canvas)
            entry.pack()
            heso.append(entry)
        global coso
        for i in range (n):
            label=tk.Label(frame_inside_canvas, text=f"Nhập cơ số {i+1}" )
            label.pack()
            entry=tk.Entry(frame_inside_canvas)
            entry.pack()
            coso.append(entry)
        button2=tk.Button(frame_inside_canvas,text=f"Giải",command=math)
        button2.pack()

        frame_inside_canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    except ValueError:
        mes="Số ẩn của hệ là số nguyên.\n\nVui lòng nhập lại"
        messagebox.showwarning("Cảnh báo", mes)



cs=tk.Tk()
cs.title("GIẢI PHƯƠNG TRÌNH N ẨN")
cs.geometry("400x400")
cs.resizable(False, False)

main_frame=tk.Frame(cs)
main_frame.pack()

label1=tk.Label(main_frame, text="Số ẩn của hệ phương trình")
label1.pack()
entry1 = tk.Entry(main_frame)
entry1.pack()
button1=tk.Button(main_frame, text="Giải hệ phương trình", command=bt1)
button1.pack()

second_frame=tk.Frame(cs)
second_frame.pack_forget()

third_frame=tk.Frame(cs)
label_ketqua=tk.Label(third_frame, text=f"Các nghiệm của hệ phương trình lần lượt là:")
label_ketqua.pack()
third_frame.pack_forget()


cs.mainloop()