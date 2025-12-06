import numpy as np
import math

# Физические константы
k = 1.38e-23
electron_mass = 9.11e-31
elementary_charge = 1.6e-19
dielectric_constant  = 8.85e-12
krypton_atom_radius = 198e-12
krypton_ionisation_potential = 13.99
a0 = 0.529e-10

# Параметры СПД
distances = np.array([10, 20, 30])

plasm_potential = np.array([199.3, 186.1, 75.5])
magnet_field = np.array([4.59, 29.2, 117.2])

electron_current = np.array([2.59, 2.23, 0.5])
ion_current = np.array([0.108, 0.475, 2.19])
electron_temperature = np.array([4, 7.01, 2.47])
elastic_en_time = np.array([0.764e-7, 0.506e-7, 1.84e-7])
nonelastic_en_time =  np.array([7.23e-6,  1.44e-6, 2.44e-6])
neutral_temperature = 400
kinetic_diameter_krypton = 360e-12

# Расход криптона в м³/с (объемный расход)
volume_flow = 0.55e-6  # м³/с

# Плотность криптона при нормальных условиях (кг/м³)
krypton_density = 3.749  # кг/м³ при 0°C и 1 атм

# Преобразование объемного расхода в массовый расход
mass_flow = volume_flow * krypton_density  # кг/с

print(f"Объемный расход криптона: {volume_flow:.6e} м³/с")
print(f"Плотность криптона: {krypton_density} кг/м³")
print(f"Массовый расход: {mass_flow:.6e} кг/с")
krypton_mass = 83.798 * 1.66e-27

magnet_field_tesla = magnet_field / 10000

# Параметры канала
mean_diameter = 56e-3
large_diameter = 70
channel_width = 28e-3
square_of_channel = ((np.pi * (mean_diameter + channel_width) ** 2) / 4) - ((np.pi * (mean_diameter - channel_width) ** 2) / 4)
neutral_mass_flow = mass_flow - ion_current * krypton_mass / elementary_charge  # кг/с

electron_current = np.array([2.59, 2.23, 0.5]) / square_of_channel
print(electron_current)
ion_current = np.array([0.108, 0.475, 2.19]) / square_of_channel
print(square_of_channel)
print(f'Ионный ток: {ion_current}')
print(elastic_en_time+nonelastic_en_time)

# Скорости частиц (м/с)
electron_velocity = ((8*k*electron_temperature*11600)/(np.pi*electron_mass)) ** 0.5
ion_velocity = ((elementary_charge*(200 - plasm_potential))/(2*krypton_mass)) ** 0.5
neutral_velocity = (3*k*neutral_temperature/krypton_mass) ** 0.5

# Температура ионов
ion_temperature = (krypton_mass * ion_velocity ** 2 / (2 * k)) / 11600

# Концентрации частиц
ion_concentration = ion_current/(ion_velocity*elementary_charge)  # м⁻³
electron_concentration = ion_concentration

# Концентрация нейтралов: массовый расход нейтралов / (масса частицы * скорость * площадь)
neutral_concentration = np.array([3.62e19, 3.03e19, 2.84e18])
# Параметры плазмы
debye_radius = ((dielectric_constant * k * electron_temperature * 11600) / (electron_concentration * (elementary_charge ** 2))) ** 0.5  # м
number_of_particles_in_debye_sphere = (electron_concentration) * (debye_radius ** 3) * np.pi * (4 / 3)  # безразмерная
plasm_frequency = ((electron_concentration * elementary_charge ** 2) / (dielectric_constant * electron_mass)) ** 0.5  # рад/с
                   
# Кулоновский логарифм для электронов (и электрон-ионных): ln(λ_D/b_min)
b_min = (elementary_charge ** 2)/(4*np.pi*dielectric_constant*electron_temperature * elementary_charge)
electron_qoulon_logarithm = np.log(debye_radius/b_min)

# циклотронные частоты (рад/с)
electron_cycle_frequency = (elementary_charge * magnet_field_tesla) / electron_mass     # ω_ce
ion_cycle_frequency = (elementary_charge * magnet_field_tesla) / krypton_mass           # ω_ci

# используем тепловые скорости, которые вы уже вычислили:
# electron_velocity и ion_velocity у вас — это средняя/thermal speeds
# принять поперечную компоненту v_perp = v_th / sqrt(2) для изотропного распределения
v_perp_e = electron_velocity / np.sqrt(2)
v_perp_i = ion_velocity / np.sqrt(2)

# Larmor radii (м)
electron_larmor_radius = (electron_mass * v_perp_e) / (elementary_charge * magnet_field_tesla)
ion_larmor_radius = (krypton_mass * v_perp_i) / (elementary_charge * magnet_field_tesla)

# Поляризуемость атома (из формулы r_at=0.62(alpha)*1/3)
alpha = (krypton_atom_radius/0.62) ** 3  # м³
# Вычисление относительной энергии движения иона и атома
relative_energy = ((krypton_mass * (ion_velocity - neutral_velocity) ** 2) / 2) * 6.24e18  # эВ
print(f"rel:{relative_energy}")

# Сечения столкновений (м²)
neutral_neutral_collision_cross_section = np.pi*kinetic_diameter_krypton**2
qoulon_collision_cross_section_electron = 2.87e-18 * electron_qoulon_logarithm / ((electron_temperature) ** 2)
transport_cross_section_ions = 2 * np.pi * (2 ** 0.5) * (a0 ** 2) * ((alpha / (a0 ** 3)) * (krypton_ionisation_potential/relative_energy)) ** 0.5
recharge_cross_section = transport_cross_section_ions / 2

# Частоты столкновений для электронов (с⁻¹)
electron_electron_collision_frequency = (2) ** 0.5 * (qoulon_collision_cross_section_electron * electron_concentration * electron_velocity)
electron_ion_collision_frequency = (qoulon_collision_cross_section_electron * ion_concentration * electron_velocity)
electron_neutral_collision_frequency = (1 / elastic_en_time) + (1 /nonelastic_en_time)

overall_electron_collision_frequency = electron_electron_collision_frequency + electron_ion_collision_frequency + electron_neutral_collision_frequency

# Частоты столкновений для ионов (с⁻¹)
ion_ion_collision_frequency = (2) ** 0.5 * (qoulon_collision_cross_section_electron * ion_concentration * ion_velocity)
ion_neutral_collision_frequency = 3/2 * ((ion_velocity - neutral_velocity) * neutral_concentration * recharge_cross_section)
overall_ion_collision_frequency = ion_ion_collision_frequency + ion_neutral_collision_frequency + electron_ion_collision_frequency

# Частоты столкновений для нейтральных частиц (с⁻¹)
neutral_neutral_collision_frequency = neutral_concentration * neutral_velocity * neutral_neutral_collision_cross_section

overall_neutral_collision_frequency = electron_neutral_collision_frequency +  + ion_neutral_collision_frequency + neutral_neutral_collision_frequency
# Длины свободного пробега (м)
electron_free_path = electron_velocity / overall_electron_collision_frequency
ion_free_path = ion_velocity / overall_ion_collision_frequency
neutral_free_path = neutral_velocity / overall_neutral_collision_frequency

# Параметры Холла (безразмерные)
# β = ωc / ν, где ωc - циклотронная частота, ν - частота столкновений
# Параметр Холла показывает отношение времени между столкновениями к периоду циклотронного вращения
electron_hall_parameter = electron_cycle_frequency / (overall_electron_collision_frequency)
ion_hall_parameter = ion_cycle_frequency / overall_ion_collision_frequency

# Электропроводность (См/м)
electric_conductivity_longitudal = (electron_concentration * elementary_charge ** 2) / (electron_mass * (electron_neutral_collision_frequency + electron_ion_collision_frequency))
electric_conductivity_transversal = electric_conductivity_longitudal * (electron_hall_parameter / (electron_hall_parameter ** 2 + 1))

# Тяга и тяговый КПД
thrust = (ion_current[2] * square_of_channel) * (2 * krypton_mass * 200 / elementary_charge) ** (1/2)
nu_thrust = thrust * ion_velocity[2] / (540)

print(thrust)
print(nu_thrust)