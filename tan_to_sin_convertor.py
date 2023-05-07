import matplotlib.pyplot as plt

tan_list_1 = [0.0013,0.0046,0.0093,0.0133,0.0166,0.0210,0.0253,0.0300,0.0333]
tan_list_2 = [0.0060,0.0126,0.0183,0.0253,0.0316,0.0376,0.0433]
tan_list_3 = [0.0030,0.0056,0.0090,0.0113,0.0150,0.0176,0.0210,0.0240,0.0263,0.0290]

def tan_to_sin(tan_theta):
    sin_theta = tan_theta / (1+tan_theta**2)**0.5
    return sin_theta

sin_list_1 = []
for tan_theta in tan_list_1:
    sin_value = tan_to_sin(tan_theta)
    sin_list_1.append(round(sin_value,4))

sin_list_2 = []
for tan_theta in tan_list_2:
    sin_value = tan_to_sin(tan_theta)
    sin_list_2.append(round(sin_value,4))

sin_list_3 = []
for tan_theta in tan_list_3:
    sin_value = tan_to_sin(tan_theta)
    sin_list_3.append(round(sin_value,4))


print(f' for wire 1: {sin_list_1}')
print(f' for wire 2: {sin_list_2}')
print(f' for wire 3: {sin_list_3}')

list_1 = [n for n in range(1,len(sin_list_1)+1)]
list_2 = [n for n in range(1,len(sin_list_2)+1)]
list_3 = [n for n in range(1,len(sin_list_3)+1)]

print(list_1)
print(list_2)
print(list_3)

plt.plot(list_1, sin_list_1, label = "wire 1")
plt.plot(list_2, sin_list_2, label = "wire 2")
plt.plot(list_3, sin_list_3, label = "wire 3")

plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('sin vs order of diffraction minimum graph')

plt.legend()

plt.show()