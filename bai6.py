import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd

# Hàm sigmoid cho mạng neural
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Đạo hàm của sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Hàm để tính toán và hiển thị số sinh viên đạt và không đạt
def evaluate_predictions(predictions, ground_truth, threshold=0.5):
    predictions_binary = np.where(predictions >= threshold, 1, 0)

    students_passed = np.sum(predictions_binary == ground_truth)
    students_failed = len(ground_truth) - students_passed

    print(f"Số sinh viên đạt: {students_passed}")
    print(f"Số sinh viên không đạt: {students_failed}")

    # Vẽ biểu đồ cột thể hiện kết quả
    labels = ['Đạt', 'Không đạt']
    values = [students_passed, students_failed]

    plt.bar(labels, values, color=['green', 'red'])
    plt.title('Biểu đồ số lượng sinh viên đạt và không đạt')
    plt.xlabel('Kết quả')
    plt.ylabel('Số lượng sinh viên')
    plt.show()

# Đọc file CSV
df = pd.read_csv('Student_Performance.csv')

# Trích xuất cột cần thiết cho dữ liệu x và y
x1 = df['Hours Studied']
x2 = df['Previous Scores']
x3 = df['Extracurricular Activities']
x4 = df['Sleep Hours']
x5 = df['Sample Question Papers Practiced']
y = df['Performance Index']

# Tạo model cho tập dữ liệu
X = np.column_stack((x1, x2, x3, x4, x5))
Y = np.array(y).reshape(-1, 1)

# Khởi tạo biến
W = tf.Variable(tf.random.normal([5, 1], dtype=tf.float32), name="W")
b = tf.Variable(tf.random.normal([1], dtype=tf.float32), name="b")

# Thiết lập tốc độ học và số vòng lặp
learning_rate = 0.01
training_epochs = 100

# Hàm dự đoán của mô hình
def linear_regression(X):
    return tf.matmul(tf.cast(X, tf.float32), W) + b

# Hàm mất mát Mean Squared Error
def mean_squared_error(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))

# Tối ưu hóa bằng Gradient Descent
optimizer = tf.optimizers.SGD(learning_rate)

# Huấn luyện mô hình
for epoch in range(training_epochs):
    with tf.GradientTape() as tape:
        y_pred = linear_regression(X)
        loss = mean_squared_error(y_pred, Y)

    gradients = tape.gradient(loss, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))

    if (epoch + 1) % 10 == 0:
        print("Epoch", (epoch + 1), ": loss =", loss.numpy())

# Tính toán dự đoán cho tất cả 5 biến
predictions = np.dot(X, W.numpy()) + b.numpy()

# Vẽ biểu đồ kết quả cho tất cả 5 biến
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs[0, 0].scatter(x1, y)
axs[0, 0].plot(x1, predictions, 'r', label='Dự đoán')
axs[0, 0].set_xlabel('Số giờ học')
axs[0, 0].set_ylabel('Chỉ số thành tích')
axs[0, 0].legend()
axs[0, 1].scatter(x2, y)
axs[0, 1].plot(x2, predictions, 'r', label='Dự đoán')
axs[0, 1].set_xlabel('Điểm trước đó')
axs[0, 1].set_ylabel('Chỉ số thành tích')
axs[0, 1].legend()
axs[0, 2].scatter(x3, y)
axs[0, 2].plot(x3, predictions, 'r', label='Dự đoán')
axs[0, 2].set_xlabel('Hoạt động ngoại khóa')
axs[0, 2].set_ylabel('Chỉ số thành tích')
axs[0, 2].legend()
axs[1, 0].scatter(x4, y)
axs[1, 0].plot(x4, predictions, 'r', label='Dự đoán')
axs[1, 0].set_xlabel('Giờ ngủ')
axs[1, 0].set_ylabel('Chỉ số thành tích')
axs[1, 0].legend()
axs[1, 1].scatter(x5, y)
axs[1, 1].plot(x5, predictions, 'r', label='Dự đoán')
axs[1, 1].set_xlabel('Lượng đề luyện tập')
axs[1, 1].set_ylabel('Chỉ số thành tích')
axs[1, 1].legend()
plt.tight_layout()
plt.show()

# Áp dụng hàm đánh giá
evaluate_predictions(predictions, y)
