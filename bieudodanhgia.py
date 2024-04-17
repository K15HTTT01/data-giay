# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:06:03 2024

@author: thanh
"""

import csv
import matplotlib.pyplot as plt

def filter_ratings(csv_file, min_rating=3.0, max_rating=5.0):
    filtered_ratings = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                rating = float(row['rating'].split()[0])  # Chuyển đổi đánh giá từ chuỗi sang số
                if min_rating <= rating <= max_rating:
                    filtered_ratings.append(row)
            except ValueError:
                pass  # Bỏ qua nếu giá trị không hợp lệ

    return filtered_ratings

def plot_ratings_histogram(filtered_data):
    ratings = [float(data['rating'].split()[0]) for data in filtered_data]
    plt.hist(ratings, bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Đánh giá')
    plt.ylabel('Số lượng sản phẩm')
    plt.title('Phân phối đánh giá từ 3.0 đến 5.0 sao (Tháng 12, 2023)')
    plt.grid(True)
    plt.text(4.2, 100, 'Tháng 12, 2023', fontsize=12, color='red')  # Thêm văn bản vào biểu đồ
    plt.show()

# Đường dẫn tới tệp CSV chứa dữ liệu sản phẩm
csv_file_path = 'Shoes_Data.csv'

# Lấy ra các dữ liệu từ 4.0 out of 5 stars đến 5.0 out of 5 stars từ cột rating
filtered_data = filter_ratings(csv_file_path)

# Vẽ biểu đồ cột dựa trên dữ liệu đã lọc
plot_ratings_histogram(filtered_data)