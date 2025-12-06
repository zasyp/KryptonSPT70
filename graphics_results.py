import matplotlib.pyplot as plt
from calculations import *
from matplotlib import rcParams

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

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']       # для всех обычных надписей
rcParams['mathtext.fontset'] = 'stix'              # math-формулы в стиле Times
rcParams['mathtext.default'] = 'it'                # курсив по умолчанию
rcParams['axes.unicode_minus'] = False
rcParams['font.size'] = 18
rcParams['axes.titlesize'] = 20
rcParams['axes.labelsize'] = 18
rcParams['xtick.labelsize'] = 16
rcParams['ytick.labelsize'] = 16
rcParams['legend.fontsize'] = 16
rcParams['figure.titlesize'] = 24
rcParams['figure.autolayout'] = True
def plot_results():

    # -------- Список графиков для автоматической обработки --------
    plots = [
        # 1
        {
            "title": "Концентрации частиц",
            "ylabels": r'Концентрация, м$^{-3}$',
            "yscale": "log",
            "series": [
                (electron_concentration, r'$n_e$', 'ro'),
                (ion_concentration, r'$n_i$', 'bo'),
                (neutral_concentration, r'$n_n$', 'go')
            ]
        },
        # 2
        {
            "title": "Температуры частиц",
            "ylabels": "Температура, эВ",
            "series": [
                (electron_temperature, r'$T_e$', 'ro'),
                (ion_temperature, r'$T_i$', 'bo')
            ]
        },
        # 3
        {
            "title": "Скорости частиц",
            "ylabels": "Скорость, м/с",
            "yscale": "log",
            "series": [
                (electron_velocity, r'$v_e$', 'ro'),
                (ion_velocity, r'$v_i$', 'bo')
            ]
        },
        # 4
        {
            "title": "Параметры Холла",
            "ylabels": "Параметр Холла",
            "yscale": "log",
            "series": [
                (electron_hall_parameter, r'$\beta_e$', 'ro'),
                (ion_hall_parameter, r'$\beta_i$', 'bo')
            ]
        },
        # 5
        {
            "title": "Частоты столкновений",
            "ylabels": "Частота столкновений, с⁻¹",
            "yscale": "log",
            "series": [
                (overall_electron_collision_frequency, r'$\nu_e$', 'ro'),
                (overall_ion_collision_frequency, r'$\nu_i$', 'bo'),
                (overall_neutral_collision_frequency, r'$\nu_n$', 'go')
            ]
        },
        # 6
        {
            "title": "Длины свободного пробега",
            "ylabels": "Длина свободного пробега, м",
            "yscale": "log",
            "series": [
                (electron_free_path, r'$\lambda_e$', 'ro'),
                (ion_free_path, r'$\lambda_i$', 'bo'),
                (neutral_free_path, r'$\lambda_n$', 'go')
            ]
        },
        # 7
        {
            "title": "Электропроводность",
            "ylabels": "Электропроводность, См/м",
            "yscale": "log",
            "series": [
                (electric_conductivity_longitudal, r'$\sigma_\parallel$', 'ro'),
                (electric_conductivity_transversal, r'$\sigma_\perp$', 'bo')
            ]
        },
        # 8
        {
            "title": "Радиусы Лармора частиц",
            "ylabels": "Радиус Лармора, м",
            "yscale": "log",
            "series": [
                (electron_larmor_radius, r'$r_{Le}$', 'ro'),
                (ion_larmor_radius, r'$r_{Li}$', 'bo')
            ]
        },
        # 9
        {
            "title": "Потенциал плазмы и магнитное поле",
            "ylabels": "Потенциал плазмы, В",
            "series": [
                (plasm_potential, r'$\varphi$', 'ro')
            ],
            "magnet": True  # особая обработка
        }
    ]

    # =================== генерация по 4 графика на картинку ===================
    page = 1
    for i in range(0, len(plots), 4):
        part = plots[i:i+4]
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f"Параметры плазмы (лист {page})", fontsize=18, fontweight='bold')

        for ax, plot in zip(axes.flat, part):

            # стандартные графики
            if "magnet" not in plot:

                for data, label, style in plot["series"]:
                    ax.plot(distances, data, style, marker='o', linestyle='none', label=label)

                if "yscale" in plot:
                    ax.set_yscale(plot["yscale"])
                ax.set_title(plot["title"])
                ax.set_ylabel(plot["ylabels"])
                ax.set_xlabel("Расстояние, мм")
                ax.grid(True, alpha=0.3)
                ax.legend()

            # последний график с двумя осями
            else:
                ax.plot(distances, plasm_potential, 'ro', marker='o', linestyle='none', label=r'$\varphi$')
                ax.set_ylabel("Потенциал плазмы, В", color='r')
                ax.tick_params(axis='y', labelcolor='r')
                ax.set_xlabel("Расстояние, мм")
                ax.set_title(plot["title"])
                ax.grid(True, alpha=0.3)

                ax2 = ax.twinx()
                ax2.plot(distances, magnet_field, 'bo', marker='o', linestyle='none', label=r'$B$')
                ax2.set_ylabel("Магнитное поле, Гс", color='b')
                ax2.tick_params(axis='y', labelcolor='b')

        plt.tight_layout()
        fname = f"plasma_plots_page_{page}.png"
        plt.savefig(fname, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Сохранено: {fname}")
        page += 1


# запуск
plot_results()
print("Графики сохранены в файлы 'plasma_parameters_plots.png'")