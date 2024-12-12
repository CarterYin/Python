import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 示例数据
x = np.array([303, 308, 313, 318, 323])
y = np.array([2315.1, 1892.0, 1594.9, 1352.7, 1145.6])

# 将 x 数据转换为倒数
reciprocal_x = 1.0 / x

# 将 y 数据转换为对数（自然对数）
log_y = np.log(y)

# 进行线性拟合
p = np.polyfit(reciprocal_x, log_y, 1)

# 拟合后的斜率和截距
slope = p[0]
intercept = p[1]

# 绘制原始数据和拟合直线
plt.figure()
plt.scatter(reciprocal_x, log_y, color='red', label='数据点')
plt.plot(reciprocal_x, np.polyval(p, reciprocal_x), color='blue', label='拟合线')
plt.xlabel('$\\frac{1}{T}$')
plt.ylabel('$\\ln R_T$')

# 格式化横坐标的小数位数为4
formatter = FuncFormatter(lambda x, _: f'{x:.5f}')
plt.gca().xaxis.set_major_formatter(formatter)

# 在图形旁边显示拟合直线的方程
equation = f'$\\ln R_T = {slope:.4f}\\left(\\frac{{1}}{{T}}\\right) + {intercept:.4f}$'
plt.text(min(reciprocal_x) + 0.00005, max(log_y) - 0.005, equation, fontsize=12, color='blue')

plt.title('$\\ln R_T - \\frac{1}{T}$')
plt.show()