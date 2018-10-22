Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print("Hello")
	print("Fun")
thing()
SyntaxError: invalid syntax
>>> thing()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    thing()
NameError: name 'thing' is not defined
>>> 
>>> thing()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    thing()
NameError: name 'thing' is not defined
>>> def thing():
	print("Hello")
	print("Fun")
	thing()
	print("Zip")
	thing()

	
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_1.py ===============
Hello
Fun
Zip
Hello
Fun
>>> 
>>> big = max("Hello world")
>>> print(big)
w
>>> tiny = min("Hello world")
>>> print(Tiny)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(Tiny)
NameError: name 'Tiny' is not defined
>>> print(tiny)
 
>>> print(float(99)/100)
0.99
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1+2*float(3)/4-5)
-2.5
>>> sval="123"
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv="hello bob"
>>> niv=int)nsv)
SyntaxError: invalid syntax
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_2.py ===============
Hello
Yo
7
I'm a lumperjack, and i'm okay.
I sleep all night and I work all day.
>>> def greet(lang):
	if lang=="es":
		print("Hola")
	elif lang=="fr":
		print("Bonjour")
	else:
		print("Hello")

		
>>> greet("en)
      
SyntaxError: EOL while scanning string literal
>>> greet("en")
Hello
>>> greet("es")
Hola
>>> greet("fr")
Bonjour
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_3.py ===============
('Hello', 'Povelitel')
('Hello', 'Igors')
>>> def greet(lang):
	if lang=="es":
		return "Hola"
	elif lang=="fr"
	
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang=="es":
		return "Hola"
	elif lang=="fr":
		return "Bonjour"
	else:
		return "Hello"

	
>>> print(greet("en"), " Povelitel")
('Hello', ' Povelitel')
>>> print(greet("es"), "Igors")
('Hola', 'Igors')
>>> print(greet("fr"), "Bagete")
('Bonjour', 'Bagete')
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_4.py ===============
8
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_5.py ===============
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_5.py ===============
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_5.py ===============
>>> big=max("Hello World")

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    big=max("Hello World")
  File "/home/user/RTR105/test_20181022_5.py", line 2, in max
    blah
NameError: global name 'blah' is not defined
>>> print(big)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(big)
NameError: name 'big' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_5.py ===============
>>> big=max("Hello World")
Hello World
H
e
l
l
o
 
W
o
r
l
d
>>> print(big)
w
>>> big=max("Ja krokodil, krokozhu i budu krokodit")
Ja krokodil, krokozhu i budu krokodit
J
a
 
k
r
o
k
o
d
i
l
,
 
k
r
o
k
o
z
h
u
 
i
 
b
u
d
u
 
k
r
o
k
o
d
i
t
>>> 
=============== RESTART: /home/user/RTR105/test_20181022_6.py ===============
Enter Hours: 45
Enter Rate: 10.50
Pay: 498.75
>>> 
