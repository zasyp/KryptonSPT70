import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Ваши данные
years = list(range(1999, 2026))
publications = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 7, 8, 
                10, 13, 26, 48, 42, 67, 91]

# Настройка шрифта Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 22

# Создание фигуры
plt.figure(figsize=(14, 8))

# Построение линейного графика с маркерами
plt.plot(years, publications, marker='o', linewidth=2.5, markersize=8, 
         color='crimson', markeredgecolor='black', markeredgewidth=1)

# Настройка осей и заголовка
plt.xlabel('Год', fontsize=22, fontweight='bold')
plt.ylabel('Количество публикаций', fontsize=22, fontweight='bold')
plt.title('Динамика публикаций по годам (1999-2025)', fontsize=22, fontweight='bold')

# Настройка делений на осях
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Добавление сетки
plt.grid(True, alpha=0.3, linestyle='--')

# Добавление аннотаций для пиковых значений
peak_year = 2025
peak_value = 91

plt.annotate(
    f'Пик: {peak_value} (2025)',
    xy=(peak_year, peak_value),
    xycoords='data',
    xytext=(0.18, 0.85),
    textcoords='axes fraction',
    arrowprops=dict(arrowstyle='->', lw=1),
    fontsize=22,
    fontweight='bold',
    ha='right',
    va='center'
)

# Автоматическая настройка отступов
plt.tight_layout()

# Сохранение и отображение
plt.savefig('publications_trend.png', dpi=200, bbox_inches='tight')
plt.show()
