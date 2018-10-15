Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> if x==5 :
	print("equals 5")

	
equals 5
>>> if x>4:
	print('Greater than 4')

	
Greater than 4
>>> x=5
>>> if x<10:
	print('Smaller')

	
Smaller
>>> if x>20
SyntaxError: invalid syntax
>>> if x>20:
	print('Bigger')

	
>>> print('Finis')
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_1.py ===============
10
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_2.py ===============
Smaller
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_3.py ===============
Enter X : 7
Greater than 4
Greater than or Equals 5
Not equal 6
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
More than one
Less than 100
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 6
More than one
Less than 100
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 1209
More than one
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 7
Bigger than 5
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 3
Smaller than 5
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 98
Huge, please stop
>>> 2
2
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 22
Large
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter X : 1
Small
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_5.py ===============
Enter Hours : 45
Enter Rate per hour : 10.50
498.75
>>> 
============== RESTART: /home/user/RTR105/test_20181015_4,1.py ==============
('First', -1)
('Second', 123)
>>> 
============== RESTART: /home/user/RTR105/test_20181015_4,1.py ==============
('First', -1)
('Second', 123)
>>> 
============== RESTART: /home/user/RTR105/test_20181015_4,1.py ==============
('First', -1)
('Second', 123)
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_5.py ===============
Enter Hours : 40
Enter Rate per hour : 10
400.0
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_5.py ===============
Enter Hours : 45
Enter Rate per hour : 10
475.0
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Enter Hours : nine
Enter Rate per hour : 10.50

Traceback (most recent call last):
  File "/home/user/RTR105/test_20181015_6.py", line 14, in <module>
    pay = 40 * rt + (hr - 40) * rt * 1.5
NameError: name 'rt' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Enter Hours : nine
Error, please enter numeric input
Enter Rate per hour : 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Enter Hours : nine
Error, please enter numeric input
Enter Rate per hour : one
Error, please enter numeric input

Traceback (most recent call last):
  File "/home/user/RTR105/test_20181015_6.py", line 16, in <module>
    pay = 40 * rt + (hr - 40) * rt * 1.5
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_5.py ===============
Enter Hours : 45
Enter Rate per hour : 10.50
498.75
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Enter Hours : 35
Enter Rate per hour : 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Enter Hours : 45
Enter Rate per hour : ten
Error, please enter numeric input

Traceback (most recent call last):
  File "/home/user/RTR105/test_20181015_6.py", line 18, in <module>
    if hr>40:
NameError: name 'hr' is not defined
>>> 
