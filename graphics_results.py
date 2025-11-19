import matplotlib.pyplot as plt
from calculations import *

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
        f.write(f"Магнитное поле (Тл): {magnet_field_tesla}\n")
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
        f.write(f"Массовый расход нейтралов (кг/с): {neutral_mass_flow}\n\n")
        
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
        f.write(f"Кулоновский Логарифм электрон: {electron_qoulon_logarithm}\n\n")

        # Параметры движения частиц
        f.write("ПАРАМЕТРЫ ДВИЖЕНИЯ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Циклотронная частота электронов (рад/с): {electron_cycle_frequency}\n")
        f.write(f"Циклотронная частота ионов (рад/с): {ion_cycle_frequency}\n")
        f.write(f"Радиус Лармора электронов (м): {electron_larmor_radius}\n")
        f.write(f"Радиус Лармора ионов (м): {ion_larmor_radius}\n")
        
        # Сечения столкновений
        f.write("СЕЧЕНИЯ СТОЛКНОВЕНИЙ:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Сечение столкновения нейтрал-нейтрал (м^2): {neutral_neutral_collision_cross_section}\n")
        f.write(f"Сечение кулоновского столкновения для электронов (м^2): {qoulon_collision_cross_section_electron}\n")
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
        f.write(f"Частота столкновений ион-нейтрал (с^-1): {ion_neutral_collision_frequency}\n")
        f.write(f"Общая частота столкновений ионов (с^-1): {overall_ion_collision_frequency}\n\n")
        
        # Частоты столкновений для нейтральных частиц
        f.write("ЧАСТОТЫ СТОЛКНОВЕНИЙ ДЛЯ НЕЙТРАЛЬНЫХ ЧАСТИЦ:\n")
        f.write("-" * 30 + "\n")
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

# Вызов функции
save_results_to_file()
print("Все результаты сохранены в файл 'plasma_calculations_results.txt'")

# Функция для построения графиков
def plot_results():
    """
    Строит графики основных параметров плазмы в зависимости от расстояния
    """
    # Настройка стиля графиков
    plt.style.use('default')
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    fig.suptitle('Параметры плазмы СПД в зависимости от расстояния', fontsize=16, fontweight='bold')
    
    # График 1: Концентрации частиц
    ax1 = axes[0, 0]
    ax1.semilogy(distances, electron_concentration, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax1.semilogy(distances, ion_concentration, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax1.semilogy(distances, neutral_concentration, 'go-', label='Нейтралы', linewidth=2, markersize=8)
    ax1.set_xlabel('Расстояние (мм)')
    ax1.set_ylabel('Концентрация (м⁻³)')
    ax1.set_title('Концентрации частиц')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # График 2: Температуры
    ax2 = axes[0, 1]
    ax2.plot(distances, electron_temperature, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax2.plot(distances, ion_temperature, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax2.set_xlabel('Расстояние (мм)')
    ax2.set_ylabel('Температура (эВ)')
    ax2.set_title('Температуры частиц')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # График 3: Скорости частиц
    ax3 = axes[0, 2]
    ax3.semilogy(distances, electron_velocity, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax3.semilogy(distances, ion_velocity, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax3.set_xlabel('Расстояние (мм)')
    ax3.set_ylabel('Скорость (м/с)')
    ax3.set_title('Скорости частиц')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # График 4: Параметры Холла
    ax4 = axes[1, 0]
    ax4.semilogy(distances, electron_hall_parameter, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax4.semilogy(distances, ion_hall_parameter, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax4.set_xlabel('Расстояние (мм)')
    ax4.set_ylabel('Параметр Холла')
    ax4.set_title('Параметры Холла')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # График 5: Частоты столкновений
    ax5 = axes[1, 1]
    ax5.semilogy(distances, overall_electron_collision_frequency, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax5.semilogy(distances, overall_ion_collision_frequency, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax5.semilogy(distances, overall_neutral_collision_frequency, 'go-', label='Нейтралы', linewidth=2, markersize=8)
    ax5.set_xlabel('Расстояние (мм)')
    ax5.set_ylabel('Частота столкновений (с⁻¹)')
    ax5.set_title('Общие частоты столкновений')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # График 6: Длины свободного пробега
    ax6 = axes[1, 2]
    ax6.semilogy(distances, electron_free_path, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax6.semilogy(distances, ion_free_path, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax6.semilogy(distances, neutral_free_path, 'go-', label='Нейтралы', linewidth=2, markersize=8)
    ax6.set_xlabel('Расстояние (мм)')
    ax6.set_ylabel('Длина свободного пробега (м)')
    ax6.set_title('Длины свободного пробега')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # График 7: Электропроводность
    ax7 = axes[2, 0]
    ax7.semilogy(distances, electric_conductivity_longitudal, 'ro-', label='Продольная', linewidth=2, markersize=8)
    ax7.semilogy(distances, electric_conductivity_transversal, 'bo-', label='Поперечная', linewidth=2, markersize=8)
    ax7.set_xlabel('Расстояние (мм)')
    ax7.set_ylabel('Электропроводность (См/м)')
    ax7.set_title('Электропроводность')
    ax7.legend()
    ax7.grid(True, alpha=0.3)
    
    # График 8: Радиусы Лармора
    ax8 = axes[2, 1]
    ax8.semilogy(distances, electron_larmor_radius, 'ro-', label='Электроны', linewidth=2, markersize=8)
    ax8.semilogy(distances, ion_larmor_radius, 'bo-', label='Ионы', linewidth=2, markersize=8)
    ax8.set_xlabel('Расстояние (мм)')
    ax8.set_ylabel('Радиус Лармора (м)')
    ax8.set_title('Радиусы Лармора')
    ax8.legend()
    ax8.grid(True, alpha=0.3)
    
    # График 9: Потенциал плазмы и магнитное поле
    ax9 = axes[2, 2]
    ax9_primary = ax9
    ax9_primary.plot(distances, plasm_potential, 'ro-', label='Потенциал плазмы', linewidth=2, markersize=8)
    ax9_primary.set_xlabel('Расстояние (мм)')
    ax9_primary.set_ylabel('Потенциал плазмы (В)', color='red')
    ax9_primary.tick_params(axis='y', labelcolor='red')
    
    ax9_secondary = ax9_primary.twinx()
    ax9_secondary.plot(distances, magnet_field, 'bo-', label='Магнитное поле', linewidth=2, markersize=8)
    ax9_secondary.set_ylabel('Магнитное поле (Гс)', color='blue')
    ax9_secondary.tick_params(axis='y', labelcolor='blue')
    
    ax9_primary.set_title('Потенциал плазмы и магнитное поле')
    lines1, labels1 = ax9_primary.get_legend_handles_labels()
    lines2, labels2 = ax9_secondary.get_legend_handles_labels()
    ax9_primary.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    ax9_primary.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('plasma_parameters_plots.png', dpi=300, bbox_inches='tight')
    plt.show()
    

# Вызов функции построения графиков после сохранения результатов
plot_results()
print("Графики сохранены в файлы 'plasma_parameters_plots.png'")