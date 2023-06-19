a={}
print(type(a))

b={1:"vivek", 2:"sheela"}
print(b[1])

b[1]="vivek.n"
print(b)

b[3]="manju"
print(b)

print(b.keys())

print(b.values())

e=["id", 123]
f=["name", "vivek"]
g=["role", "tester"]

h=dict([e, f, g])
print(h)

i=h.keys()
print(i)

g=h.fromkeys(i, "unassigned")
print(g)

print(b.items())

for key, value in b.items():
    if value=="manju":
        print(key)




