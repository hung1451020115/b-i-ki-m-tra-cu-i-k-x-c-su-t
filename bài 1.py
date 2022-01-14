m = input("nhập tên của bạn")
n = len(m)

d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print(m)
print(d)