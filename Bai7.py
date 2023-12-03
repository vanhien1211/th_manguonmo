import cv2
from tkinter import Tk, Button, filedialog, Label, Entry, Scale
from PIL import Image, ImageTk

def apply_filter():
    global image_path
    global image

    # Đọc ảnh từ đường dẫn
    image_path = filedialog.askopenfilename(title="Chọn ảnh")
    if image_path:
        path_entry.delete(0, 'end')  # Xóa nội dung hiện tại trong ô nhập địa chỉ đường dẫn
        path_entry.insert(0, image_path)  # Hiển thị đường dẫn trong ô nhập
        image = cv2.imread(image_path)
        # Hiển thị ảnh gốc khi chọn ảnh
        show_original_image()

def update_images():
    global image
    global smoothed_image

    # Chuyển từ BGR sang RGB để hiển thị bằng PIL
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Lấy giá trị của thanh trượt mức độ làm mịn
    selected_level = kernel_size_scale.get()

    # Chọn mức độ làm mịn tương ứng với giá trị được chọn
    kernel_size = get_kernel_size(selected_level)

    # Áp dụng bộ lọc Gaussian
    smoothed_image = cv2.GaussianBlur(image_rgb, kernel_size, 0)

    # Hiển thị ảnh gốc và ảnh sau khi làm mịn bằng PIL
    show_image(smoothed_image, 'Smoothed Image')

def show_original_image():
    global image

    # Chuyển từ BGR sang RGB để hiển thị bằng PIL
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Hiển thị ảnh gốc bằng PIL
    show_image(image_rgb, 'Original Image')

def show_image(img, title):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    label.config(image=img)
    label.image = img
    label_title.config(text=title)

def get_kernel_size(level):
    # Chọn mức độ làm mịn tương ứng với level
    if level == 1:
        return (5, 5)
    elif level == 2:
        return (7, 7)
    elif level == 3:
        return (13, 13)
    elif level == 4:
        return (15, 15)
    else:
        return (5, 5)  # Giá trị mặc định nếu level không hợp lệ

def save_image():
    global smoothed_image

    if smoothed_image is not None:
        # Chọn nơi lưu ảnh
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

        if save_path:
            # Lưu ảnh kết quả (ảnh đã làm mịn)
            pil_image = Image.fromarray(smoothed_image)
            pil_image.save(save_path)

# Khởi tạo biến toàn cục để lưu ảnh và đường dẫn
image = None
smoothed_image=None
image_path = ""

# Tạo cửa sổ Tkinter
root = Tk()
root.title("Ứng dụng làm mịn ảnh")

# Tạo nhãn và ô nhập để hiển thị và nhập đường dẫn ảnh
path_label = Label(root, text="Đường dẫn ảnh:")
path_label.pack(pady=5)

path_entry = Entry(root, width=50)
path_entry.pack(pady=5)

# Tạo nút để chọn ảnh
load_button = Button(root, text="Chọn ảnh", command=apply_filter)
load_button.pack(pady=10)

# Tạo thanh trượt để chọn mức độ làm mịn
kernel_size_scale = Scale(root, from_=1, to=4, orient="horizontal", label="Chọn mức độ làm mịn")
kernel_size_scale.pack()

# Tạo nhãn để hiển thị ảnh
label = Label(root)
label.pack()

# Tạo nhãn để hiển thị tiêu đề ảnh
label_title = Label(root, text="")
label_title.pack()

# Tạo nút để áp dụng bộ lọc
apply_button = Button(root, text="Áp dụng bộ lọc", command=update_images)
apply_button.pack(pady=10)

# Tạo nút để hiển thị ảnh gốc
original_button = Button(root, text="Hiển thị ảnh gốc", command=show_original_image)
original_button.pack(pady=5)

# Tạo nút để lưu ảnh
save_button = Button(root, text="Lưu ảnh", command=save_image)
save_button.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
