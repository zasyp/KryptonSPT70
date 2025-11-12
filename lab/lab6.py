import matplotlib.pyplot as plt
import numpy as np

# Данные из таблицы
data = """
-202,2	-0,15
-177,2	-0,14
-160,5	-0,13
-139,7	-0,12
-127,2	-0,10
-98,1	-0,08
-80,1	-0,06
-78,5	-0,06
-77,9	-0,06
-41,6	1,1
-40,6	1,4
-36,5	3,6
-32,3	4,1
-26,1	5,1
-23,3	5,6
-21,6	6,0
-19,0	5
-18,2	5
-17,4	6
-10,1	13
-8,5	14
-7,4	13
-6,5	12
-2	15
-0,5	15
0,2	28
1	28
3	28
7,2	28
11,3	29
15,6	27
23,8	27
32,1	28
36,3	27
44,6	29
57,1	31
61,3	31
65,4	32
69,6	33
77,9	34
82,1	35
86,3	37
94,6	38
98,8	39
102,9	41
103,1	45
111,2	48
115,4	50
123,7	50
127,9	49
132,1	49
140,4	48
141,5	47
148,7	47
161,2	48
"""

# Преобразование данных в числовой формат
lines = data.strip().split('\n')
voltage = []
current = []

for line in lines:
    v, c = line.replace(',', '.').split('\t')
    voltage.append(float(v))
    current.append(float(c))

# Построение графика
plt.figure(figsize=(12, 8))
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.plot(voltage, np.log(current), 'b-', linewidth=2)  # Логарифмическая шкала для тока
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.xlabel('Напряжение, В', fontsize=16)
plt.ylabel('Логарифм тока', fontsize=16)
plt.title('Логарифмическая ВАХ', fontsize=16)

plt.tight_layout()
plt.show()