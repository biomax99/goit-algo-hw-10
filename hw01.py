from pulp import LpMaximize, LpProblem, LpVariable

# Оголошуємо модель
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні для кількості виробленого лимонаду і фруктового соку
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Функція цілі: максимізація загальної кількості продукції
model += lemonade + fruit_juice, "Total Production"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon Juice"
model += 2 * fruit_juice <= 40, "Fruit Puree"

# Розв'язуємо модель
model.solve()

# Вивід результатів
print("Оптимальна кількість Лимонаду:", lemonade.varValue)
print("Оптимальна кількість Фруктового соку:", fruit_juice.varValue)
print("Загальна кількість продукції:", model.objective.value())
