import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Параметри для методу Монте-Карло
N = 100000  # Кількість точок для методу Монте-Карло

# Метод Монте-Карло для обчислення інтегралу
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
under_curve = y_random < f(x_random)
mc_integral = (b - a) * f(b) * np.sum(under_curve) / N

print("Метод Монте-Карло:", mc_integral)

# Аналітичне обчислення інтегралу з функцією quad
result, error = spi.quad(f, a, b)
print("Аналітичний результат з quad:", result)
print("Похибка:", abs(result - mc_integral))

# Побудова графіка функції та області під кривою
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
