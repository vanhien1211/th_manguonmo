import os
from tkinter import Tk, filedialog, Button, Label, Frame, Scale, IntVar
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import cv2

class ImageEnhancer:
    def __init__(self, master):
        self.master = master
        self.master.title("Enhance Image Brightness")

        self.image_path = ""
        self.brightness_factor = IntVar(value=15)

        # Frame chứa các thành phần giao diện
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Button để chọn ảnh
        self.choose_button = Button(self.frame, text="Chọn ảnh", command=self.choose_image)
        self.choose_button.grid(row=0, column=0, padx=5, pady=5)

        # Label hiển thị đường dẫn ảnh
        self.path_label = Label(self.frame, text="Đường dẫn ảnh: ")
        self.path_label.grid(row=1, column=0, padx=5, pady=5)

        # Thanh trượt để điều chỉnh độ sáng
        self.brightness_slider = Scale(self.frame, from_=1, to=30, orient="horizontal", label="Độ sáng",
                                       variable=self.brightness_factor)
        self.brightness_slider.grid(row=2, column=0, padx=5, pady=5)

        # Button để tăng cường độ sáng
        self.enhance_button = Button(self.frame, text="Tăng cường độ sáng", command=self.enhance_brightness)
        self.enhance_button.grid(row=3, column=0, padx=5, pady=5)

        # Placeholder for displaying the image
        self.image_label = Label(self.frame)
        self.image_label.grid(row=4, column=0, padx=5, pady=5)

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image_path = file_path
            self.path_label.config(text=f"Đường dẫn ảnh: {file_path}")

            # Hiển thị ảnh trên giao diện
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

    def enhance_brightness(self):
        if self.image_path:
            # Đọc ảnh từ đường dẫn
            image = cv2.imread(self.image_path)

            # Tăng cường độ sáng của ảnh dựa trên giá trị của thanh trượt
            brightness_factor = self.brightness_factor.get() / 10
            enhanced_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

            # Hiển thị ảnh tăng cường độ sáng bằng matplotlib
            plt.imshow(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
            plt.title("Enhanced Image")
            plt.axis('off')  # Optional: Turn off axis labels
            plt.show()

if __name__ == "__main__":
    root = Tk()
    app = ImageEnhancer(root)
    root.mainloop()
