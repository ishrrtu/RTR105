'''
fland=open("mbox.txt")
count=0
for line in fland:
    count=count+1
print("Line Count:",count)
'''
'''
fland=open("mbox.txt")
for line in fland:
    if line.startswith("From:"):
        print(line)
'''
'''
fland=open("mbox.txt")
for line in fland:
    line=line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
'''
fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count=0
for line in fhand:
    if line.startswith("Subject:"):
        count=count+1
print("There were", count, "subject lines in", fname)
