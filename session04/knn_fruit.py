import numpy as np
import matplotlib.pyplot as plt

# ویژگی‌های سیب (عرض و طول)
apple_width = np.random.randint(4, 9, 50)
apple_height = np.random.randint(5, 10, 50)

# ویژگی‌های موز (عرض و طول)
banana_width = np.random.randint(2, 5, 50)
banana_height = np.random.randint(8, 15, 50)

X_train = []

# سیب‌ها
for i in range(50):
    X_train.append([apple_width[i], apple_height[i]])

# موز‌ها
for i in range(50):
    X_train.append([banana_width[i], banana_height[i]])

X_train = np.array(X_train)

y_train = []

# 0 = سیب
for i in range(50):
    y_train.append(0)

# 1 = موز
for i in range(50):
    y_train.append(1)

y_train = np.array(y_train)

# میوه جدید
new_fruit = [5, 6]

# رسم نمودار
plt.scatter(X_train[:50, 0], X_train[:50, 1], color='red', label='Apple')
plt.scatter(X_train[50:, 0], X_train[50:, 1], color='orange', label='Banana')
plt.scatter(new_fruit[0], new_fruit[1], color='blue', marker='x', s=100, label='New Fruit')

plt.xlabel('Width')
plt.ylabel('Height')
plt.legend()
plt.show()

# محاسبه فاصله اقلیدسی تا تمام میوه‌ها
distances = []
for fruit in X_train:
    d = np.sqrt((fruit[0] - new_fruit[0])**2 + (fruit[1] - new_fruit[1])**2)
    distances.append(d)

distances = np.array(distances)
print("Distances:", distances)
print("Shape:", distances.shape)
