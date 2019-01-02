#print(vars())

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

#print(vars())

from numpy import sinh, linspace

#x = linspace(0, 7, 70) #solis = (7-0)/(70-1)
x = linspace(-4, 4, 11) #solis = (4-0)(11-1)
y = sinh(x/2)
#print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija sinh(x/2)')
plt.plot(x, y, "ko")
plt.plot(x, y, color = "#FF00AA")
plt.legend(["$sinh(x/2)$"])
plt.show()
