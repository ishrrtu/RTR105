hrs = input("Enter Hours : ")
h = float(hrs)
rate = input("Enter Rate per hour : ")
r = float(rate)
if h>40:
    pay = 40 * r + (h - 40) * r * 1.5
else:
	pay = h * r
print(pay)
