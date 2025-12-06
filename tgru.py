import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from scipy.optimize import fsolve
import matplotlib.patches as patches

# Константы
e = constants.e  # Заряд электрона, Кл
k = constants.k  # Постоянная Больцмана, Дж/К
eV_to_J = e     # 1 эВ в Джоулях

# Данные для варианта 3
T_k = 1000      # Температура катода, K
N_i = 1e16      # Поток атомов цезия, см^{-2}·с^{-1}
T_Cs = 340      # Температура паров цезия, K
E_k = 8e5       # Внешнее электрическое поле, В/см

# Параметры материалов
A = 60          # Постоянная Ричардсона, А/(см²·К²)
phi_W = 4.52    # Работа выхода вольфрама, эВ
phi_Cs = 1.69   # Работа выхода цезия, эВ
n0 = 1e15       # Плотность атомов в монослое, см^{-2}

print("=== РАСЧЕТ ЭМИССИОННЫХ ХАРАКТЕРИСТИК W-Cs ===\n")
print(f"Исходные данные:")
print(f"T_k = {T_k} K, N_i = {N_i:.1e} см⁻²·с⁻¹")
print(f"T_Cs = {T_Cs} K, E_k = {E_k:.1e} В/см")

# Пункт 1: Определение плотности тока по S-образной диаграмме
print("\n--- ПУНКТ 1: Определение плотности тока ---")

# Для построения S-образной кривой используем типичные значения для системы W-Cs
def S_shaped_curve(T, E):
    """Модель S-образной характеристики для системы W-Cs"""
    # Типичные параметры для аппроксимации
    j_sat = 1.0  # А/см² - ток насыщения
    T_opt = 1200 # K - оптимальная температура
    width = 200  # K - ширина пика
    
    # S-образная зависимость
    j = j_sat * np.exp(-((T - T_opt)/width)**2) * (1 + 0.1 * np.log10(E/1e5))
    return j

# Строим S-образную диаграмму
T_range = np.linspace(800, 2000, 100)
j_S = S_shaped_curve(T_range, E_k)

plt.figure(figsize=(10, 6))
plt.semilogy(T_range, j_S, 'b-', linewidth=2)
plt.axvline(T_k, color='red', linestyle='--', alpha=0.7, label=f'T_k = {T_k} K')
plt.xlabel('Температура T (K)', fontsize=12)
plt.ylabel('Плотность тока j (А/см²)', fontsize=12)
plt.title('S-образная диаграмма для системы W-Cs', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Определяем j_e для заданной температуры
j_e = S_shaped_curve(T_k, E_k)
print(f"Плотность тока по S-диаграмме: j_e = {j_e:.3f} А/см²")

# Пункт 2: Определение снижения работы выхода
print("\n--- ПУНКТ 2: Определение Δφ ---")

def calculate_delta_phi(j_e, T, A, phi_W):
    """Вычисляет снижение работы выхода из уравнения Ричардсона"""
    kT_eV = k * T / e  # kT в эВ
    
    # Решаем уравнение: j_e = A*T²*exp(-(phi_W - Δφ)/(kT))
    # => phi_W - Δφ = -kT * ln(j_e/(A*T²))
    
    exponent_arg = j_e / (A * T**2)
    if exponent_arg <= 0:
        return phi_W  # Нет снижения
    
    delta_phi = phi_W + kT_eV * np.log(exponent_arg)
    return max(0, delta_phi)  # Δφ не может быть отрицательным

delta_phi = calculate_delta_phi(j_e, T_k, A, phi_W)
print(f"Снижение работы выхода: Δφ = {delta_phi:.3f} эВ")

# Пункт 3: Определение степени покрытия θ
print("\n--- ПУНКТ 3: Определение степени покрытия θ ---")

def calculate_theta(delta_phi, phi_W, phi_Cs):
    """Вычисляет степень покрытия из уравнения баланса работ выхода"""
    if phi_W == phi_Cs:
        return 0
    theta = delta_phi / (phi_W - phi_Cs)
    return min(max(theta, 0), 1)  # Ограничиваем от 0 до 1

theta = calculate_theta(delta_phi, phi_W, phi_Cs)
print(f"Степень покрытия: θ = {theta:.3f}")

# Строим зависимость φ_W - Δφ = f(θ)
theta_range = np.linspace(0, 1, 100)
phi_difference = phi_W - delta_phi * np.ones_like(theta_range)  # Константа для данного Δφ

plt.figure(figsize=(10, 6))
plt.plot(theta_range, phi_difference, 'g-', linewidth=2)
plt.axhline(phi_W - delta_phi, color='red', linestyle='--', 
           label=f'φ_W - Δφ = {phi_W - delta_phi:.2f} эВ')
plt.xlabel('Степень покрытия θ', fontsize=12)
plt.ylabel('φ_W - Δφ (эВ)', fontsize=12)
plt.title('Зависимость φ_W - Δφ от степени покрытия', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Пункт 4: Скорость адсорбции
print("\n--- ПУНКТ 4: Скорость адсорбции ---")
v_ads = N_i * (1 - theta)
print(f"Скорость адсорбции: v_ads = {v_ads:.2e} см⁻²·с⁻¹")

# Пункт 5: Плотность атомов при степени покрытия θ
print("\n--- ПУНКТ 5: Плотность атомов ---")
n = theta * n0
print(f"Плотность атомов: n = {n:.2e} см⁻²")

# Пункт 6: Определение плеча диполя d
print("\n--- ПУНКТ 6: Определение плеча диполя ---")

def calculate_dipole_length(delta_phi, n):
    """Вычисляет длину плеча диполя"""
    # Δφ = 8.9e-14 * n * e * d
    # d = Δφ / (8.9e-14 * n * e)
    
    # Переводим Δφ из эВ в В
    delta_phi_V = delta_phi  # 1 эВ = 1 В для потенциала
    
    # Вычисляем d в см
    d = delta_phi_V / (8.9e-14 * n * e)
    return d

d = calculate_dipole_length(delta_phi, n)
print(f"Плечо диполя: d = {d:.2e} см")

# Строим картину изолированного диполя
fig, ax = plt.subplots(figsize=(8, 4))

# Металлическая поверхность
ax.axhline(y=0, color='gray', linewidth=4, label='Поверхность металла')

# Диполь
dipole_length = d * 1e8  # Масштабируем для наглядности (в Å)
ax.arrow(0.5, 0, 0, dipole_length, head_width=0.05, head_length=0.1, 
         fc='red', ec='red', linewidth=2, label='Дипольный момент')

ax.set_xlim(0, 1)
ax.set_ylim(-0.5, dipole_length + 0.5)
ax.set_xlabel('x')
ax.set_ylabel('z (Å)')
ax.set_title('Картина изолированного диполя на поверхности', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()

# Пункт 7: Давление насыщенных паров цезия
print("\n--- ПУНКТ 7: Давление паров цезия ---")

def calculate_Cs_pressure(T_Cs):
    """Вычисляет давление насыщенных паров цезия"""
    # p_Cs = 2.45e8 * exp(-8910/T_Cs) [мм рт.ст.]
    p_Cs = 2.45e8 * np.exp(-8910 / T_Cs)
    return p_Cs

p_Cs = calculate_Cs_pressure(T_Cs)
print(f"Давление паров цезия: p_Cs = {p_Cs:.2e} мм рт.ст.")

# Пункт 8: Ток эмиссии с учетом внешнего поля
print("\n--- ПУНКТ 8: Ток эмиссии с учетом поля ---")

def emission_current_with_field(T, E, phi_W, delta_phi, A):
    """Вычисляет ток эмиссии с учетом шотки-эффекта"""
    # j = A*T² * exp(-e(φ_W - Δφ - 3.62e-4*sqrt(E))/(kT))
    
    kT_eV = k * T / e  # kT в эВ
    
    # Снижение барьера за счет поля (эффект Шоттки)
    delta_phi_field = 3.62e-4 * np.sqrt(E)  # в эВ
    
    # Эффективная работа выхода
    phi_eff = phi_W - delta_phi - delta_phi_field
    
    # Плотность тока
    j = A * T**2 * np.exp(-phi_eff / kT_eV)
    
    return j, phi_eff

j_emission, phi_eff = emission_current_with_field(T_k, E_k, phi_W, delta_phi, A)
print(f"Ток эмиссии с учетом поля: j = {j_emission:.3f} А/см²")
print(f"Эффективная работа выхода: φ_eff = {phi_eff:.3f} эВ")

# Строим зависимость тока эмиссии от поля
E_range = np.logspace(4, 7, 100)  # В/см
j_vs_E = [emission_current_with_field(T_k, E, phi_W, delta_phi, A)[0] for E in E_range]

plt.figure(figsize=(10, 6))
plt.loglog(E_range, j_vs_E, 'b-', linewidth=2)
plt.axvline(E_k, color='red', linestyle='--', alpha=0.7, label=f'E_k = {E_k:.1e} В/см')
plt.xlabel('Электрическое поле E (В/см)', fontsize=12)
plt.ylabel('Плотность тока j (А/см²)', fontsize=12)
plt.title('Зависимость тока эмиссии от электрического поля', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Итоговые результаты
print("\n=== ИТОГОВЫЕ РЕЗУЛЬТАТЫ ===")
print(f"1. Плотность тока (S-диаграмма): {j_e:.3f} А/см²")
print(f"2. Снижение работы выхода: Δφ = {delta_phi:.3f} эВ")
print(f"3. Степень покрытия: θ = {theta:.3f}")
print(f"4. Скорость адсорбции: {v_ads:.2e} см⁻²·с⁻¹")
print(f"5. Плотность атомов: {n:.2e} см⁻²")
print(f"6. Плечо диполя: {d:.2e} см")
print(f"7. Давление паров Cs: {p_Cs:.2e} мм рт.ст.")
print(f"8. Ток эмиссии (с полем): {j_emission:.3f} А/см²")

# Дополнительный анализ: зависимость от температуры
print("\n--- ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ: Зависимость от температуры ---")

T_range_analysis = np.linspace(800, 1500, 50)
j_vs_T = [emission_current_with_field(T, E_k, phi_W, delta_phi, A)[0] for T in T_range_analysis]

plt.figure(figsize=(10, 6))
plt.semilogy(T_range_analysis, j_vs_T, 'purple', linewidth=2)
plt.axvline(T_k, color='red', linestyle='--', alpha=0.7, label=f'T_k = {T_k} K')
plt.xlabel('Температура T (K)', fontsize=12)
plt.ylabel('Плотность тока j (А/см²)', fontsize=12)
plt.title('Зависимость тока эмиссии от температуры', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()