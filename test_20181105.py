'''
fruit="pen pineapple apple pen"
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index, letter)
    index=index+1
'''
'''
fruit="banana"
for letter in fruit:
    print(letter)
'''
word="banana"
count=0
for letter in word:
    if letter=="a":
        count=count+1
print(count)
if word=="banana":
    print("All right, bananas.")

if word < "banana":
    print("Your word," + word + ", comes defore banana.")
elif word > "banana":
    print("Your word," + word + ", comes after banana.")
else:
    print("All right, bananas.")
