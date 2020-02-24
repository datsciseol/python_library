x = ["a", "b", "c", "d", "e"]
search = "f"
cnt = 0
for elem in range(len(x)):
    if x[elem] == search:
        cnt += 1

if cnt:
    print("True")
else:
    print("False")