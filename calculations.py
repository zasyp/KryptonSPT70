import numpy as np
import math

# Параметры СПД
distances =     np.array([10, 20, 30])
plasm_potential = np.array([199.3, 186.1, 75.5])
magnet_field = np.array([5.56, 38.6, 154.8])
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

magnet_field_tesla = magnet_field / 10000
# Параметры канала
mean_diameter = 56e-3
large_diameter = 70
channel_width = 28e-3
square_of_channel = (np.pi * (mean_diameter + channel_width) ** 2) / 4

# Физические константы
k = 1.38e-23
electron_mass = 9.11e-31
elementary_charge = 1.6e-19
dielectric_constant  = 8.85e-12
krypton_mass = 83.798 * 1.66e-27
krypton_atom_radius = 198e-10
krypton_ionisation_potential = 13.99
a0 = 0.529e-8

# Скорости частиц (м/с)
electron_velocity = ((8*k*electron_temperature*11600)/(np.pi*electron_mass)) ** 0.5
ion_velocity = (elementary_charge*plasm_potential/(2*krypton_mass)) ** 0.5
neutral_velocity = (3*k*neutral_temperature/krypton_mass) ** 0.5

# Температура ионов
ion_temperature = (krypton_mass * ion_velocity ** 2 / (2 * k)) / 11600

# Концентрации частиц
electron_concentration = electron_current/(electron_velocity*elementary_charge)  # м⁻³
ion_concentration = ion_current/(ion_velocity*elementary_charge)  # м⁻³

# Концентрация нейтралов: массовый расход нейтралов / (масса частицы * скорость * площадь)
neutral_mass_flow = mass_flow - ion_current * krypton_mass / elementary_charge  # кг/с
neutral_concentration = neutral_mass_flow / (krypton_mass * neutral_velocity * square_of_channel)  # м⁻³

# Параметры плазмы
debye_radius = ((dielectric_constant * k * electron_temperature) / 
                (electron_concentration * elementary_charge ** 2)) ** 0.5  # м
number_of_particles_in_debye_sphere = (electron_concentration * debye_radius ** 3) * np.pi * (4 / 3)  # безразмерная
plasm_frequency = ((electron_concentration * elementary_charge ** 2) / 
                   (dielectric_constant * electron_mass)) ** 0.5  # рад/с
                   
ion_qoulon_logarithm_arg = 1.24e7 * (((electron_temperature*11600) ** 3) / electron_concentration)  # безразмерная
electron_qoulon_logarithm_arg = 1.24e7 * (((ion_temperature*11600) ** 3) / ion_concentration)  # безразмерная
electron_qoulon_logarithm = np.log(electron_qoulon_logarithm_arg)  # безразмерная
ion_qoulon_logarithm = np.log(ion_qoulon_logarithm_arg)  # безразмерная

# Параметры движения частиц
electron_cycle_frequency = (elementary_charge*magnet_field_tesla)/electron_mass  # рад/с
ion_cycle_frequency = (elementary_charge*magnet_field_tesla)/krypton_mass  # рад/с
electron_cycloid_radius = (electron_mass * electron_velocity) / (elementary_charge * magnet_field_tesla)  # м
ion_cycloid_radius = (krypton_mass * ion_velocity) / (elementary_charge * magnet_field_tesla)  # м
electron_cycloid_height = 2 * electron_mass * plasm_potential / (elementary_charge * magnet_field_tesla ** 2)  # м
ion_cycloid_height = 2 * krypton_mass * plasm_potential / (elementary_charge * magnet_field_tesla ** 2)  # м

# Поляризумость атома (из формулы r_at=0.62(alpha)*1/3)
alpha = (krypton_atom_radius/0.62) ** 3  # м³

# Вычисление относительной энергии движения иона и атома
relative_energy = ((krypton_mass * (ion_velocity - neutral_velocity) ** 2) / 2) * 6.24e18  # эВ

# Сечения столкновений (м²)
neutral_neutral_collision_cross_section = np.pi*kinetic_diameter_krypton**2
qoulon_collision_cross_section_electron = 2.87e-14 * electron_qoulon_logarithm / (electron_temperature ** 2)
qoulon_collision_cross_section_ion = 2.87e-14 * ion_qoulon_logarithm / (ion_temperature ** 2)
transport_cross_section_ions = 2 * np.pi * (2 ** 0.5) * (a0 ** 2) * ((alpha / (a0 ** 3)) * (krypton_ionisation_potential/relative_energy)) ** 0.5
recharge_cross_section = transport_cross_section_ions / 2

# Частоты столкновений для электронов (с⁻¹)
electron_electron_collision_frequency = (2)  ** 0.5 * (qoulon_collision_cross_section_electron * electron_concentration * electron_velocity)
electron_ion_collision_frequency = (qoulon_collision_cross_section_ion * ion_concentration * electron_velocity)
electron_neutral_collision_frequency = 1  / (elastic_en_time + nonelastic_en_time)

overall_electron_collision_frequency = electron_electron_collision_frequency + electron_ion_collision_frequency + electron_neutral_collision_frequency

# Частоты столкновений для ионов (с⁻¹)
ion_ion_collision_frequency = (2)  ** 0.5 * (qoulon_collision_cross_section_ion * ion_concentration * ion_velocity)
ion_electron_collision_frequency = (qoulon_collision_cross_section_ion * electron_concentration * ion_velocity)
ion_neutral_collision_frequency = 3/2 * (ion_velocity * neutral_concentration * recharge_cross_section)

overall_ion_collision_frequency = ion_ion_collision_frequency + ion_electron_collision_frequency + ion_neutral_collision_frequency

# Частоты столкновений для нейтральных частиц (с⁻¹)
neutral_electron_collision_frequency = 1  / (elastic_en_time + nonelastic_en_time)
neutral_ion_collision_frequency = (neutral_neutral_collision_cross_section * ion_concentration * neutral_velocity)
neutral_neutral_collision_frequency = neutral_concentration * neutral_velocity * neutral_neutral_collision_cross_section

overall_neutral_collision_frequency = neutral_electron_collision_frequency + neutral_ion_collision_frequency + neutral_neutral_collision_frequency

# Длины свободного пробега (м)
electron_free_path = electron_velocity / overall_electron_collision_frequency
ion_free_path = ion_velocity / overall_ion_collision_frequency
neutral_free_path = neutral_velocity / overall_neutral_collision_frequency

# Параметры Холла (безразмерные)
# β = ωc / ν, где ωc - циклотронная частота, ν - частота столкновений
# Параметр Холла показывает отношение времени между столкновениями к периоду циклотронного вращения
electron_hall_parameter = electron_cycle_frequency / overall_electron_collision_frequency
ion_hall_parameter = ion_cycle_frequency / overall_ion_collision_frequency

# Электропроводность (См/м)
electric_conductivity_longitudal = (electron_concentration * elementary_charge ** 2) / (electron_mass * (electron_neutral_collision_frequency + electron_ion_collision_frequency))
electric_conductivity_transversal = electric_conductivity_longitudal * (electron_hall_parameter / (electron_hall_parameter ** 2 + 1))

# Функция для записи всех результатов в файл
def save_results_to_file(filename="plasma_calculations_results.txt"):
    """
    Сохраняет все вычисленные параметры плазмы в текстовый файл
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("РЕЗУЛЬТАТЫ РАСЧЕТОВ ПАРАМЕТРОВ ПЛАЗМЫ СПД\n")
        f.write("=" * 50 + "\n\n")
        
        # Исходные параметры
        f.write("ИСХОДНЫЕ ПАРАМЕТРЫ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Расстояния (мм): {distances}\n")
        f.write(f"Потенциал плазмы (В): {plasm_potential}\n")
        f.write(f"Магнитное поле (Гс): {magnet_field}\n")
        f.write(f"Ток электронов (А): {electron_current}\n")
        f.write(f"Ток ионов (А): {ion_current}\n")
        f.write(f"Температура электронов (эВ): {electron_temperature}\n")
        f.write(f"Температура ионов (эВ): {ion_temperature}\n")
        f.write(f"Время упругого взаимодействия (с): {elastic_en_time}\n")
        f.write(f"Время неупругого взаимодействия (с): {nonelastic_en_time}\n")
        f.write(f"Температура нейтралов (К): {neutral_temperature}\n")
        f.write(f"Кинетический диаметр криптона (м): {kinetic_diameter_krypton}\n")
        f.write(f"Объемный расход криптона (м³/с): {volume_flow}\n")
        f.write(f"Плотность криптона (кг/м³): {krypton_density}\n")
        f.write(f"Массовый расход (кг/с): {mass_flow}\n")
        f.write(f"Массовый расход нейтралов (кг/с): {neutral_mass_flow}\n")
        
        # Константы
        f.write("ФИЗИЧЕСКИЕ КОНСТАНТЫ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Постоянная Больцмана (Дж/К): {k}\n")
        f.write(f"Масса электрона (кг): {electron_mass}\n")
        f.write(f"Элементарный заряд (Кл): {elementary_charge}\n")
        f.write(f"Диэлектрическая постоянная (Ф/м): {dielectric_constant}\n")
        f.write(f"Масса криптона (кг): {krypton_mass}\n")
        f.write(f"Радиус атома криптона (м): {krypton_atom_radius}\n")
        f.write(f"Потенциал ионизации криптона (эВ): {krypton_ionisation_potential}\n")
        f.write(f"Боровский радиус (м): {a0}\n\n")
        
        # Скорости частиц
        f.write("СКОРОСТИ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Скорость электронов (м/с): {electron_velocity}\n")
        f.write(f"Скорость ионов (м/с): {ion_velocity}\n")
        f.write(f"Скорость нейтралов (м/с): {neutral_velocity}\n\n")
        
        # Концентрации частиц
        f.write("КОНЦЕНТРАЦИИ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Концентрация электронов (м^-3): {electron_concentration}\n")
        f.write(f"Концентрация ионов (м^-3): {ion_concentration}\n")
        f.write(f"Концентрация нейтралов (м^-3): {neutral_concentration}\n\n")
        
        # Параметры плазмы
        f.write("ПАРАМЕТРЫ ПЛАЗМЫ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Радиус Дебая (м): {debye_radius}\n")
        f.write(f"Число частиц в сфере Дебая: {number_of_particles_in_debye_sphere}\n")
        f.write(f"Плазменная частота (рад/с): {plasm_frequency}\n")
        f.write(f"Кулоновский Логарифм для электронов: {electron_qoulon_logarithm}\n")
        f.write(f"Кулоновский Логарифм для ионов: {ion_qoulon_logarithm}\n\n")

        
        # Параметры движения частиц
        f.write("ПАРАМЕТРЫ ДВИЖЕНИЯ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Циклотронная частота электронов (рад/с): {electron_cycle_frequency}\n")
        f.write(f"Циклотронная частота ионов (рад/с): {ion_cycle_frequency}\n")
        f.write(f"Поляризуемость атома (м^3): {alpha}\n")
        f.write(f"Относительная энергия движения иона и атома (эВ): {relative_energy}\n")
        f.write(f"Радиус циклоиды электронов (м): {electron_cycloid_radius}\n")
        f.write(f"Радиус циклоиды ионов (м): {ion_cycloid_radius}\n")
        f.write(f"Высота циклоиды электронов (м): {electron_cycloid_height}\n")
        f.write(f"Высота циклоиды ионов (м): {ion_cycloid_height}\n\n")
        
        # Сечения столкновений
        f.write("СЕЧЕНИЯ СТОЛКНОВЕНИЙ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Сечение столкновения нейтрал-нейтрал (м^2): {neutral_neutral_collision_cross_section}\n")
        f.write(f"Сечение кулоновского столкновения для электронов (м^2): {qoulon_collision_cross_section_electron}\n")
        f.write(f"Сечение кулоновского столкновения для ионов (м^2): {qoulon_collision_cross_section_ion}\n")
        f.write(f"Транспортное сечение ионов (м^2): {transport_cross_section_ions}\n")
        f.write(f"Сечение перезарядки (м^2): {recharge_cross_section}\n\n")
        
        # Частоты столкновений для электронов
        f.write("ЧАСТОТЫ СТОЛКНОВЕНИЙ ДЛЯ ЭЛЕКТРОНОВ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Частота столкновений электрон-электрон (с^-1): {electron_electron_collision_frequency}\n")
        f.write(f"Частота столкновений электрон-ион (с^-1): {electron_ion_collision_frequency}\n")
        f.write(f"Частота столкновений электрон-нейтрал (с^-1): {electron_neutral_collision_frequency}\n")
        f.write(f"Общая частота столкновений электронов (с^-1): {overall_electron_collision_frequency}\n\n")
        
        # Частоты столкновений для ионов
        f.write("ЧАСТОТЫ СТОЛКНОВЕНИЙ ДЛЯ ИОНОВ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Частота столкновений ион-ион (с^-1): {ion_ion_collision_frequency}\n")
        f.write(f"Частота столкновений ион-электрон (с^-1): {ion_electron_collision_frequency}\n")
        f.write(f"Частота столкновений ион-нейтрал (с^-1): {ion_neutral_collision_frequency}\n")
        f.write(f"Общая частота столкновений ионов (с^-1): {overall_ion_collision_frequency}\n\n")
        
        # Частоты столкновений для нейтральных частиц
        f.write("ЧАСТОТЫ СТОЛКНОВЕНИЙ ДЛЯ НЕЙТРАЛЬНЫХ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Частота столкновений нейтрал-электрон (с^-1): {neutral_electron_collision_frequency}\n")
        f.write(f"Частота столкновений нейтрал-ион (с^-1): {neutral_ion_collision_frequency}\n")
        f.write(f"Частота столкновений нейтрал-нейтрал (с^-1): {neutral_neutral_collision_frequency}\n")
        f.write(f"Общая частота столкновений нейтралов (с^-1): {overall_neutral_collision_frequency}\n\n")
        
        # Длины свободного пробега
        f.write("ДЛИНЫ СВОБОДНОГО ПРОБЕГА:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Длина свободного пробега электронов (м): {electron_free_path}\n")
        f.write(f"Длина свободного пробега ионов (м): {ion_free_path}\n")
        f.write(f"Длина свободного пробега нейтралов (м): {neutral_free_path}\n\n")

        # Параметры Холла
        f.write("ПАРАМЕТРЫ ХОЛЛА:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Параметр Холла для электронов: {electron_hall_parameter}\n")
        f.write(f"Параметр Холла для ионов: {ion_hall_parameter}\n\n")


        # Электропроводность
        f.write("ЭЛЕКТРОПРОВОДНОСТЬ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Электропроводность вдоль магнитного поля (См/м): {electric_conductivity_longitudal}\n")
        f.write(f"Электропроводность поперек магнитного поля (См/м): {electric_conductivity_transversal}\n\n")

# Вызов функции для сохранения результатов
save_results_to_file()
print("Все результаты сохранены в файл 'plasma_calculations_results.txt'")
