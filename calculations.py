import numpy as np
import math

# Параметры СПД
distances = np.array([10, 20, 30])
plasm_potential = np.array([199.3, 186.1, 75.5])
magnet_field = np.array([5.56, 38.6, 154.8])
electron_current = np.array([2.59, 2.23, 0.5])
ion_current = np.array([0.108, 0.475, 2.19])
electron_temperature = np.array([4, 7.01, 2.47])
elastic_en_time = np.array([0.764e-7, 0.506e-7, 1.84e-7])
nonelastic_en_time =  np.array([7.23e-6,  1.44e-6, 2.44e-6])
neutral_temperature = 400
kinetic_diameter_krypton = 360e-12
mass_flow = 0.55e-6

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
# Скорости частиц
electron_velocity = ((8*k*electron_temperature*11600)/(np.pi*electron_mass)) ** 0.5
ion_velocity = (elementary_charge*plasm_potential/(2*krypton_mass)) ** 0.5
neutral_velocity = (3*k*neutral_temperature/krypton_mass) ** 0.5

# Концентрации частиц
electron_concentration = electron_current/(electron_velocity*elementary_charge)
ion_concentration = ion_current/(ion_velocity*elementary_charge)
neutral_concentration = (mass_flow - ion_current)/(elementary_charge*neutral_velocity*square_of_channel)

# Параметры плазмы
debye_radius = ((dielectric_constant * k * electron_temperature) / 
                (electron_concentration * elementary_charge ** 2)) ** 0.5
number_of_particles_in_debye_sphere = (electron_concentration * debye_radius ** 3) * np.pi * (4 / 3)
plasm_frequency = ((electron_concentration * elementary_charge ** 2) / 
                   (dielectric_constant * electron_mass)) ** 0.5
qoulon_logarithm_arg = 1.24e7 * (((electron_temperature*11600) ** 3) / electron_concentration)
qoulon_logarithm = np.log(qoulon_logarithm_arg)

# Параметры движения частиц
electron_cycle_frequency = (elementary_charge*magnet_field_tesla)/electron_mass
ion_cycle_frequency = (elementary_charge*magnet_field_tesla)/krypton_mass
electron_hall_parameter = electron_cycle_frequency * (elastic_en_time + nonelastic_en_time)

# Поляризумость атома (из формулы r_at=0.62(alpha)*1/3)
alpha = (krypton_atom_radius/0.62) ** 3
print(alpha)

# Вычисление относительной энергии движения иона и атома
relative_energy = ((krypton_mass * (ion_velocity - neutral_velocity) ** 2) / 2) * 6.24e18

# Сечения столкновений
neutral_neutral_collision_cross_section = np.pi*kinetic_diameter_krypton**2
qoulon_collision_cross_section = 2.87e-14 * qoulon_logarithm / (electron_temperature ** 2)
transport_cross_section_ions = 2 * np.pi * (2 ** 0.5) * (a0 ** 2) * ((alpha / (a0 ** 3)) * (krypton_ionisation_potential/relative_energy)) ** 0.5
recharge_cross_section = transport_cross_section_ions / 2

