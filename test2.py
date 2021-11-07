import numpy as np
import matplotlib.pyplot as plt


# read_dictionary = np.load(r'my_file.npy', allow_pickle=True).item()
# y1 = []
# y2 = []
# y3 = []
# for idx, item in enumerate(read_dictionary.items()):
#     y1.append(item[1][0])
#     y2.append(item[1][1])
#     y3.append(item[1][2])

#
# x = [i for i in range(1531)]
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()

# x = [i for i in range(700)]
x = []
y1 = []
y2 = []
# with open('kl') as f:
#     for item in f.readlines():
#         x.append(float(item))

with open('/Users/jhchen/acc_rot.txt') as f:
    for item in f.readlines():
        x.append(float(item))

with open('/Users/jhchen/acc_cls.txt') as f:
    for item in f.readlines():
        y1.append(float(item))

plt.scatter(x, y1)
plt.grid()
# plt.scatter(x, y2)
plt.show()