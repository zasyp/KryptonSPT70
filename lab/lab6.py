import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from matplotlib import font_manager, rcParams

# ================== НАСТРОЙКА ШРИФТА ==================
# Убедитесь, что Times New Roman установлен в системе
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 18
rcParams['axes.labelsize'] = 20
rcParams['axes.titlesize'] = 20
rcParams['legend.fontsize'] = 16
rcParams['xtick.labelsize'] = 16
rcParams['ytick.labelsize'] = 16

# ================== ДАННЫЕ ==================
# Таблица А1 — без магнитного поля
U1 = np.array([
-202.2,-177.2,-160.5,-139.7,-127.2,-98.1,-80.1,-78.5,-77.9,
-41.6,-40.6,-36.5,-32.3,-26.1,-23.3,-21.6,-19.0,-18.2,-17.4,
-10.1,-8.5,-7.4,-6.5,-2.0,-0.5,
0.2,1.0,3.0,7.2,11.3,15.6,23.8,32.1,36.3,44.6,57.1,61.3,
65.4,69.6,77.9,82.1,86.3,94.6,98.8,102.9,103.1,111.2,
115.4,123.7,127.9,132.1,140.4,141.5,148.7,161.2
])

I1 = np.array([
-0.15,-0.14,-0.13,-0.12,-0.10,-0.08,-0.06,-0.06,-0.06,
1.1,1.4,3.6,4.1,5.1,5.6,6.0,5.0,5.0,6.0,
13,14,13,12,15,15,
28,28,28,28,29,27,27,28,27,29,31,31,
32,33,34,35,37,38,39,41,45,48,
50,50,49,49,48,47,47,48
])

# Таблица А2 — с магнитным полем
U2 = np.array([
-201.5,-193.2,-184.9,-176.4,-168.2,-155.7,-147.4,-130.7,
-114.1,-105.8,-97.4,-84.9,-68.3,-64.5,-61.4,-56.5,-56.3,
-55.7,-54.9,-54.7,-54.5,
-54.2,-53.0,-48.8,-40.5,-36.3,-34.0,-27.3,-24.1,-19.5,
-15.0,-9.8,-5.6,-1.4,-0.4,
0.2,4.3,8.4,16.8,29.3,41.7,54.2,62.6,75.1,87.5,
104.2,112.5,120.9,
125.0,133.3,141.7,145.8,150.0,154.2,158.3,166.6,
175.1,183.3,191.6,199.9,204.1,216.6
])

I2 = np.array([
-0.16,-0.15,-0.15,-0.14,-0.13,-0.12,-0.11,-0.10,
-0.8,-0.8,-0.7,-0.5,-0.4,-0.3,-0.2,0.03,0.01,
0.04,0.08,0.12,0.18,
0.4,1.2,2.3,3.4,3.9,4.8,5.4,7,8,
10,10,12,13,12,
24,26,27,27,26,27,29,30,32,34,
35,36,38,
41,45,48,55,65,50,49,48,
47,47,47,47,47,48
])

# ================== ФУНКЦИИ ПОСТРОЕНИЯ ==================
def plot_iv(U, I, title, filename):
    idx = np.argsort(U)
    U = U[idx]
    I = I[idx]

    spline = UnivariateSpline(U, I, s=10)
    U_dense = np.linspace(U.min(), U.max(), 1000)
    I_dense = spline(U_dense)

    plt.figure(figsize=(9, 6))
    plt.scatter(U, I, s=50, marker='o', label='Эксперимент')
    plt.plot(U_dense, I_dense, linewidth=2.5, label='Сплайн')
    plt.xlabel('Напряжение, подаваемое на зонд, В')
    plt.ylabel('Ток на зонд, А')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    plt.close()

def plot_semilog(U, I, title, filename):
    mask = I > 0
    U = U[mask]
    I = I[mask]

    idx = np.argsort(U)
    U = U[idx]
    lnI = np.log(I[idx])

    spline = UnivariateSpline(U, lnI, s=0.5)
    U_dense = np.linspace(U.min(), U.max(), 1000)
    lnI_dense = spline(U_dense)

    plt.figure(figsize=(9, 6))
    plt.scatter(U, lnI, s=50, marker='o', label='Эксперимент')
    plt.plot(U_dense, lnI_dense, linewidth=2.5, label='Сплайн')
    plt.xlabel('Напряжение, подаваемое на зонд, В')
    plt.ylabel('Логарифм тока')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()
    plt.close()

# ================== ПОСТРОЕНИЕ ГРАФИКОВ ==================
plot_iv(U1, I1, 'ВАХ без магнитного поля', 'VAH_no_field.png')
plot_iv(U2, I2, 'ВАХ в магнитном поле', 'VAH_with_field.png')

plot_semilog(U1, I1, 'Полулогарифмическая ВАХ без магнитного поля',
             'VAH_semilog_no_field.png')
plot_semilog(U2, I2, 'Полулогарифмическая ВАХ в магнитном поле',
             'VAH_semilog_with_field.png')
