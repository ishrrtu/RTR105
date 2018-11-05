Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1="Hello"
>>> str2='there'
>>> bob=str1+str2
>>> print(bob)
Hellothere
>>> str3="123"
>>> str3=str3+1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3=str3+1
TypeError: must be str, not int
>>> x=int(str3)+1
>>> print(x)
124
>>> name=raw_input("Enter:")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name=raw_input("Enter:")
NameError: name 'raw_input' is not defined
>>> 
>>> name=raw_input("Enter:")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=raw_input("Enter:")
NameError: name 'raw_input' is not defined
>>> name=raw_input("Enter:")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name=raw_input("Enter:")
NameError: name 'raw_input' is not defined
>>> name=input("Enter:")
Enter:Shrek
>>> print(name)
Shrek
>>> apple=input("Enter")
Enter100
>>> x=apple-10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x=apple-10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x=int(apple)-10
>>> print(x)
90
>>> fruit="banana"
>>> letter=fruit[1]
>>> print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> zot="abc"
>>> print(zot[5])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> print(zot[2])
c
>>> print(len(fruit))
6
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
0 b
1 a
2 n
3 a
4 n
5 a
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
0 h
1 a
2 v
3 a
4 n
5 a
6  
7 u
8 -
9 n
10 a
11 -
12 n
13 a
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
0 p
1 e
2 n
3  
4 p
5 i
6 n
7 e
8 a
9 p
10 p
11 l
12 e
13  
14 a
15 p
16 p
17 l
18 e
19  
20 p
21 e
22 n
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
b
a
n
a
n
a
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181105.py", line 14, in <module>
    word-"banana"
NameError: name 'word' is not defined
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
3
>>> s="Monty Python"
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[0:11])
Monty Pytho
>>> print(s[3:20])
ty Python
>>> print(s[:2])
Mo
>>> print(s[:])
Monty Python
>>> a="Hello"
>>> a="Privetstvuju"
>>> b=a+" žalkie ljudiški"
>>> print(b)
Privetstvuju žalkie ljudiški
>>> 
>>> c=a+""+"There"
>>> print(c)
PrivetstvujuThere
>>> fruit="banana"
>>> "n" in fruit
True
>>> "m" in fruit
False
>>> "nan" in fruit
True
>>> if "a" in fruit:
	print("Found it!")

Found it!
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181105.py", line 22, in <module>
    if word=="banana":
NameError: name 'word' is not defined
>>> 
================ RESTART: /home/user/RTR105/test_20181105.py ================
3
All right, bananas.
All right, bananas.
>>> greet="Hello Bob"
>>> zap=greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("Hi There".lower())
hi there
>>> stuff="Hello world"
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fruit="banana"
>>> pos=fruit.find("na")
>>> print(pos)
2
>>> aa=fruit.find("z")
>>> print(aa)
-1
>>> greet="Hello Valerija"
>>> nnn=greet.upper()
>>> print(nnn)
HELLO VALERIJA
>>> www=greet.lower()
>>> print(www)
hello valerija
>>> greet="Hello bob"
>>> nstr=greet.replace("Bob","Jane")
>>> print(nstr)
Hello bob
>>> greet="Hello bob"
>>> nstr=greet.replace("bob","Jane")
>>> print(nstr)
Hello Jane
>>> nstr=greet.replace("o","y")
>>> print(nstr)
Helly byb
>>> greet="Hello Bob"
>>> greet.lstrip()
'Hello Bob'
>>> greet="   Hello Bob"
>>> greet.lstrip()
'Hello Bob'
>>> greet.rstrip()
'   Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line=("Please God I want more than 4 for my math exam")
>>> line.startwith("Please")
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    line.startwith("Please")
AttributeError: 'str' object has no attribute 'startwith'
>>> line.startswith("Please")
True
>>> print(line)
Please God I want more than 4 for my math exam
>>> line.startswith("p")
False
>>> data= 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos=data.find("@")
>>> print(atpos)
21
>>> sppos=data.find(","atpos)
SyntaxError: invalid syntax
>>> sppos=data.find(" ",atpos)
>>> sppos=data.find(" ",atpos)
>>> print(sppos)
31
>>> host=data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>> x="이광춘"
>>> type(x)
<class 'str'>
>>> x=u"이광춘"
>>> type(x)
<class 'str'>
>>> 
