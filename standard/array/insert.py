x = ["a", "b", "d", "e", "f"]
ins = "c"
idxInsert = 2
y = list(range(6))

for i in range(0, idxInsert):
    y[i] = x[i]
y[idxInsert] = "c"
for j in range(idxInsert, len(x)):
    y[j + 1] = x[j]
x = y
print(x)
print(x[2])