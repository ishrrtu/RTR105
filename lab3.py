import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from math import sinh, fabs
from time import sleep

def f(x):
    return sinh(x)

k = 0
a = -4.0
b = 4.0

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print("Dotajā intervālā [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()
else:
    print("Dotajā intervālā sakne ir!")

deltax = 0.1

while(fabs(b-a)>deltax):
    k=k+1
    x = (a+b)/2; funx = f(x)
    if (funa*funx<0.):
        b=x
    else:
        a=x

print("Sakne ir: ", x)
print("Y koordināta ir: ",sinh(x))
print("Iterāciju skaits: ", k)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija sinh(x/2)')
plt.plot(x, f(x), "ko")
plt.plot(x, f(x), color = "#FF00AA")
plt.legend(["$sinh(x/2)$"])
plt.show()
