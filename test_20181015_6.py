#hrs = input("Enter Hours : ")
try:
    hrs = input("Enter Hours : ")
    #hr = int(hrs)
except:
    hr = "Error, please enter numeric input"
    print(hr)
#rate = input("Enter Rate per hour : ")
try:
    rate = input("Enter Rate per hour : ")
    #rt = int(rate)
except:
    rt = "Error, please enter numeric input"
    print(rt)



if hr>40:
    pay = 40 * rt + (hr - 40) * rt * 1.5
else:
	pay = hr * rt
print(pay)
