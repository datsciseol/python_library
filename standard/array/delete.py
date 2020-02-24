x = ["a", "b", "c", "d", 'e', "f"]
ran = len(x)
idxDelete = 3
y = list(range(5))
elemDelete = "d"
for i in range(0, idxDelete):
    y[i] = x[i]
for j in range(idxDelete + 1, len(x)):
    y[j - 1] = x[j]
x = y
print(x)
