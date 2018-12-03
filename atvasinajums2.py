import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sinh, linspace
def f(x):
    return sinh(x/2)

x=linspace(0,4,11)
print(x)
#y=sinh(x/2)
y=f(x)
print(y)

legend=[]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("$sinh(x/2)$ funkcija un tās atvasinājumi")
plt.plot(x,y,"k")
legend.append("$sinh(x/2) funkcija$")
plt.plot(x,y,"go")
legend.append("$sinh(x/2) funkcija (daži punkti)$")

deltax=x[1]-x[0]
N=len(x)
derivative=[]

for i in range(N):
    temp=(f(x[i]+deltax)-f(x[i]))/deltax
    derivative.append(temp)
    print(derivative)

plt.plot(x,derivative,"y")
legend.append("atvasinājums")

plt.plot(x, derivative, "ro")
legend.append("atvasinājuma daži punkti")

derivative_through_array=[] #atvasinājums caur massīvu
for i in range(N-1):
    temp=(y[i+1]-y[i])/(x[i+1]-x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1],derivative_through_array,"b")
legend.append("atvasinājums (izmantojot vērtības no masīva)")

plt.plot(x[0:N-1], derivative_through_array, "ko")
legend.append("atvasinājuma (izmantojot vērtības no masīva) daži punkti")

plt.legend(legend, loc = 3)
plt.show()
