Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> stuff="Hello\nWorld!"
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff="X\nY\nZ\nkoordinatas"
>>> print(stuff)
X
Y
Z
koordinatas
>>> len(stuff)
17
>>> fland=open("mbox.txt","r")
>>> print(fland)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
>>> fland = open("stuff.txt")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fland = open("stuff.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Line Count: 7
>>> fland=open("mbox.txt")
>>> inp=fland.read()
>>> print(len(inp))
333
>>> print(inp[:20])
From stephen.marquar
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181112.py", line 10, in <module>
    if line.startwith("From:"):
AttributeError: 'str' object has no attribute 'startwith'
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
From: stephen.marquard@uct.ac.za

>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
From: stephen.marquard@uct.ac.za
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
From stephen.marquard@uct.ac.zaSat Jan  5 09:14:16 2008
From: stephen.marquard@uct.ac.za
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Enter the file name: mbox.txt
There were 1 subject lines in mbox.txt
>>> 
