x = input("x")

old =[]
new= []

total= int(input("Number"))

for i in range(total):
    old.append(input("old character"))
    new.append(input("new c"))

for i in range(total):
    user= x.replace(old[i], new[i])
print(user)
