from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = [-3, 1, 2, -2, 3, -1]
ax.plot(x, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

ex_b = [2 - i for i in x]
ax.plot(ex_b, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

ex_c = [(i / 3) * 2 + 1 for i in x]
ax.plot(ex_c, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

ex_d = [i * i for i in x]
ax.plot(ex_d, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

ex_e = [2 ** i for i in x]
ax.plot(ex_e, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

ex_f = [(2 ** i) - (i ** 3) for i in x]
ax.plot(ex_f, 'o-')
ax.set_xlabel('X', fontsize=16)
ax.set_ylabel('Y', fontsize=16)

plt.show()
