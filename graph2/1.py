import numpy as np
import matplotlib.pyplot as plt

# 示例数据
x = np.array([30, 35, 40, 45, 50])  # 第一组数据
y = np.array([0.98, 1.192, 1.366, 1.572, 1.786])  # 第二组数据

# 进行线性拟合
slope, intercept = np.polyfit(x, y, 1)  # 1表示线性拟合

# 生成拟合的直线
y_fit = slope * x + intercept

# 绘制散点图和拟合直线
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_fit, color='red', label=f'Fit: y = {slope:.3f}x + {intercept:.3f}')

# 添加方程式标签
plt.text(1, 4, f'y = {slope:.3f}x + {intercept:.3f}', fontsize=12, color='red')

# 设置图形标题和标签
plt.title('$E_x$ vs. t')
plt.xlabel('t(\u2103)')
plt.ylabel('$E_x$(mV)')

# 显示图例
plt.legend()

# 展示图形
plt.show()
